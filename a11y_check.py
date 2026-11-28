"""
a11y_check.py — 여백 DS 색 대비(WCAG) 자동 점검.

tokens.css 의 라이트/다크 값을 읽어, 주요 텍스트·배경 쌍의 명도 대비를 계산하고
WCAG AA 기준(본문 4.5:1, 큰 글자/UI 3:1) 통과 여부를 표로 출력한다.

실행:  python a11y_check.py
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))


def parse_vars(css, selector_regex):
    """selector { --a:#hex; ... } 블록에서 {name: '#hex'} 추출."""
    m = re.search(selector_regex + r"\s*\{([^}]*)\}", css, re.S)
    out = {}
    if not m:
        return out
    for name, val in re.findall(r"(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})", m.group(1)):
        out[name[2:]] = val
    return out


def lum(hexstr):
    hexstr = hexstr.lstrip("#")
    if len(hexstr) == 3:
        hexstr = "".join(c * 2 for c in hexstr)
    rgb = [int(hexstr[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4) for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contrast(fg, bg):
    a, b = lum(fg), lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


# (전경, 배경, 최소기준, 설명)  — 기준: 본문 4.5, UI/큰글자 3.0
PAIRS = [
    ("text-primary", "surface", 4.5, "본문(카드 위)"),
    ("text-primary", "bg", 4.5, "본문(페이지 위)"),
    ("text-secondary", "surface", 4.5, "보조 텍스트"),
    ("text-tertiary", "surface", 4.5, "힌트/캡션 — 안내 문장에도 쓰므로 본문 기준"),
    ("text-tertiary", "bg", 4.5, "힌트/캡션(페이지 위)"),
    ("warm", "surface", 4.5, "따뜻한 포인트 글자"),
    ("on-accent", "warm", 4.5, "따뜻한 포인트 바탕 위 흰 글자"),
    ("on-accent", "accent-strong", 4.5, "채운 버튼 글자"),
    ("success-strong", "success-bg", 4.5, "성공 배지 글자"),
    ("danger-strong", "danger-bg", 4.5, "위험 배지 글자"),
    ("warning-strong", "warning-bg", 4.5, "경고 배지 글자"),
    ("accent-strong", "surface", 3.0, "링크/액센트(UI 3:1)"),
    ("accent", "surface", 3.0, "액센트 경계(UI)"),
]


def run():
    css = open(os.path.join(BASE, "tokens.css"), encoding="utf-8").read()
    light = parse_vars(css, r":root")
    dark = parse_vars(css, r"\.theme-dark[^{]*")

    fails = 0
    for mode, vals in (("라이트", light), ("다크", dark)):
        print(f"\n=== {mode} ===")
        print(f"{'쌍':<26}{'대비':>7}  기준  판정  설명")
        for fg, bg, thr, desc in PAIRS:
            if fg not in vals or bg not in vals:
                print(f"{fg}/{bg:<14} {'--':>7}   —    (토큰 없음)  {desc}")
                continue
            r = contrast(vals[fg], vals[bg])
            ok = r >= thr
            if not ok:
                fails += 1
            mark = "✅" if ok else "❌"
            print(f"{fg + '/' + bg:<26}{r:>6.2f}:1  {thr:>3}   {mark}   {desc}")

    print("\n" + ("✅ 모든 쌍 통과" if fails == 0 else f"❌ 미달 {fails}건 — 위 표에서 확인"))
    return fails


if __name__ == "__main__":
    run()
