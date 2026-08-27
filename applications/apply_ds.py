# -*- coding: utf-8 -*-
"""
적용본 HTML 안의 디자인시스템 사본을 최신 tokens.css / components.css 로 갱신한다.

적용본은 공유용 독립 HTML 한 장이라 DS를 파일 안에 인라인으로 품고 있다.
DS를 고친 뒤 이 스크립트만 돌리면 적용본이 최신 토큰을 따라간다.

    python applications/apply_ds.py            # applications/*.html 전부
    python applications/apply_ds.py a.html     # 특정 파일만

앱 레이어 CSS(마커 바깥)는 건드리지 않는다.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS = os.path.join(ROOT, "applications")

BLOCKS = [("YB:TOKENS", "tokens.css"), ("YB:COMPONENTS", "components.css")]


def inject(html, marker, css):
    """마커 사이 내용을 css 로 교체. 마커가 없으면 그대로 돌려준다."""
    pattern = re.compile(
        r"(/\* ==== %s START ==== \*/\n).*?(\n/\* ==== %s END ==== \*/)" % (marker, marker),
        re.S,
    )
    if not pattern.search(html):
        return html, False
    return pattern.sub(lambda m: m.group(1) + css.rstrip() + m.group(2), html), True


def apply_to(path):
    html = io.open(path, encoding="utf-8").read()
    before = html
    done = []
    for marker, filename in BLOCKS:
        css = io.open(os.path.join(ROOT, filename), encoding="utf-8").read()
        html, ok = inject(html, marker, css)
        if ok:
            done.append(filename)
    if not done:
        print("건너뜀 (DS 마커 없음): %s" % os.path.basename(path))
        return
    if html == before:
        print("이미 최신: %s (%s)" % (os.path.basename(path), ", ".join(done)))
        return
    io.open(path, "w", encoding="utf-8").write(html)
    print("갱신함: %s (%s)" % (os.path.basename(path), ", ".join(done)))


def main():
    targets = sys.argv[1:]
    if targets:
        paths = [t if os.path.isabs(t) else os.path.join(APPS, os.path.basename(t)) for t in targets]
    else:
        paths = sorted(
            os.path.join(APPS, f) for f in os.listdir(APPS) if f.endswith(".html")
        )
    if not paths:
        print("적용본이 없습니다.")
        return
    for p in paths:
        apply_to(p)


if __name__ == "__main__":
    main()
