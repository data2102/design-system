"""
여백(Yeobaek) Design System — tokens.py
토스류 미니멀(기본) + 다크 모니터링(옵션) 하이브리드.

Python 도구에서 쓰는 법:
    from tokens import LIGHT, DARK, FONT, SP, RADIUS, css_vars

    T = LIGHT                      # 또는 DARK (모니터링 화면)
    label.config(fg=T["text_primary"], bg=T["surface"])

HTML을 문자열로 생성할 때:
    html = f"<style>{css_vars(LIGHT)}</style>..."

tokens.css 와 값이 1:1로 같습니다. 한쪽만 고치지 말 것.
"""

# ── 폰트 ─────────────────────────────────────────────
FONT = {
    "sans": "Noto Sans KR",        # 기본 (부드럽고 인간적). 없으면 아래 폴백
    "sans_fallback": "Malgun Gothic",   # 맑은 고딕 (Windows 기본 한글)
    "mono": "Consolas",            # 숫자/모노 (D2Coding 있으면 그걸로)
}

# ── 타이포 크기(px) ──────────────────────────────────
FS = {
    "display": 30, "title": 22, "heading": 18, "subhead": 16,
    "body": 15, "caption": 13, "footnote": 12,
}
FW = {"regular": 400, "medium": 500, "bold": 700}

# ── 간격(px), 4배수 스케일 ───────────────────────────
SP = {1: 4, 2: 8, 3: 12, 4: 16, 5: 20, 6: 24, 8: 32, 10: 40, 12: 48}

# ── 둥글기(px) ───────────────────────────────────────
RADIUS = {"sm": 8, "md": 12, "lg": 16, "xl": 20, "pill": 999}

# ── 색: 기본(라이트) — 토스류 미니멀 ─────────────────
LIGHT = {
    "accent": "#3182f6", "accent_hover": "#2b74dc", "accent_pressed": "#2264c4",
    "accent_bg": "#e8f3ff", "on_accent": "#ffffff",
    "warm": "#a8522f", "warm_bg": "#faece7",
    "text_primary": "#191f28", "text_secondary": "#4e5968",
    "text_tertiary": "#5f6a78", "text_disabled": "#b0b8c1",
    "bg": "#f2f4f6", "surface": "#ffffff", "surface_sunken": "#f9fafb",
    "border": "#eef1f4", "border_strong": "#d1d6db",
    "success": "#12b886", "success_bg": "#e6fcf5",
    "warning": "#f59f00", "warning_bg": "#fff9db",
    "danger": "#f03e3e", "danger_bg": "#fff0f0",
    "info": "#3182f6", "info_bg": "#e8f3ff",
}

# ── 색: 옵션(다크) — 모니터링/자동화 ─────────────────
DARK = {
    "accent": "#22d3ee", "accent_hover": "#38dcf0", "accent_pressed": "#0fb9d4",
    "accent_bg": "#10313a", "on_accent": "#06232a",
    "warm": "#e0a58a", "warm_bg": "#2a1c14",
    "text_primary": "#e6e8ee", "text_secondary": "#c5c9d3",
    "text_tertiary": "#8a90a2", "text_disabled": "#565b68",
    "bg": "#0f1117", "surface": "#181b24", "surface_sunken": "#12141b",
    "border": "#1e2129", "border_strong": "#262a35",
    "success": "#34d399", "success_bg": "#0f2e26",
    "warning": "#fbbf24", "warning_bg": "#2e2408",
    "danger": "#f87171", "danger_bg": "#2e1414",
    "info": "#22d3ee", "info_bg": "#10313a",
}


def css_vars(theme: dict) -> str:
    """색 dict을 :root { --key: value } CSS 문자열로. HTML 생성용."""
    lines = [f"  --{k.replace('_', '-')}: {v};" for k, v in theme.items()]
    return ":root {\n" + "\n".join(lines) + "\n}"


def font_stack(mono: bool = False) -> str:
    """Tkinter/Qt font 이름 선택. 설치 안 된 폰트는 OS가 폴백."""
    return FONT["mono"] if mono else FONT["sans"]
