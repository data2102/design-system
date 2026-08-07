"""
build_yeobaek.py — tokens.css + components.css 를 묶어 배포용 yeobaek.py 를 생성.

여백 DS의 '단일 소스(Python 배포 번들)'를 만든다. 파이썬 도구(serve.py 등)는
  import yeobaek
  html = f"<style>{yeobaek.CSS}</style> ..."   # 또는 yeobaek.TOKENS 만
로 가져다 쓴다. 웹 도구는 계속 tokens.css / components.css 를 링크해도 된다.

CSS의 진짜 원본은 tokens.css / components.css 이고, 이 스크립트는 그걸 파이썬으로
포장만 한다. → DS를 고칠 땐 css를 고치고 이 스크립트를 재실행하면 yeobaek.py 가 갱신됨.

실행:  python build_yeobaek.py
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))


def read(name):
    with open(os.path.join(BASE, name), encoding="utf-8") as f:
        return f.read()


# 토큰: 웹폰트 @import 줄은 제거(오프라인 파이썬 도구는 font-family 폴백으로 처리)
tokens = "\n".join(
    ln for ln in read("tokens.css").splitlines() if not ln.strip().startswith("@import")
).strip("\n")
components = read("components.css").strip("\n")
dashboard = read("dashboard.css").strip("\n")
charts = read("charts.js").strip("\n")

for label, txt in (("tokens.css", tokens), ("components.css", components),
                   ("dashboard.css", dashboard), ("charts.js", charts)):
    if '"""' in txt:
        raise SystemExit(f"{label} 에 三중따옴표(\"\"\") 가 있어 번들 불가. 확인 필요.")

# 레거시 변수 호환 레이어 — 기존 도구들의 변수명(--plane/--bg/--panel/--ink…)을
# 캐논 토큰(var(--surface) 등)에 연결. 캐논 변수를 참조하므로 다크 전환도 자동으로 따라감.
# 도구가 import yeobaek 로 편입될 때  TOKENS + COMPAT  를 함께 주입한다.
COMPAT = """:root{
  --plane:var(--bg); --panel:var(--surface);
  --ink:var(--text-primary); --ink2:var(--text-secondary); --muted:var(--text-secondary);
  --line:var(--border-strong); --line2:var(--border); --line3:var(--border-strong);
  --grid:var(--border); --axis:var(--text-tertiary);
  --accent-soft:var(--accent-bg);
  --up:var(--success); --up-bg:var(--success-bg); --good:var(--success); --good-ink:var(--success); --ok-bg:var(--success-bg);
  --down:var(--danger); --down-bg:var(--danger-bg); --crit:var(--danger); --crit-bg:var(--danger-bg);
  --warn:var(--warning); --warn-bg:var(--warning-bg); --wait:var(--warning); --wait-bg:var(--warning-bg);
  --s1:var(--accent); --s2:var(--success); --s3:var(--warning);
  --yA:var(--accent-bg); --yB:var(--accent); --yC:var(--accent);
  --bar:var(--accent); --target:var(--text-tertiary);
  --track:var(--surface-sunken);
  --shadow-pop:var(--shadow-popover); --shadow-card:var(--shadow-card);
  --radius:var(--radius-md); --num-font:var(--font-mono);
  --sans:var(--font-sans); --mono:var(--font-mono);
}"""

VERSION = "1.7.0"

out = f'''"""
여백(Yeobaek) Design System — 파이썬 배포 번들  (AUTO-GENERATED)

build_yeobaek.py 가 tokens.css + components.css 로부터 생성합니다. 직접 편집하지 마세요.
(고칠 땐 css 를 고치고  python build_yeobaek.py  재실행)

사용법:
    import yeobaek
    html = f"<style>{{yeobaek.CSS}}</style> ..."     # 전체(토큰+컴포넌트)
    html = f"<style>{{yeobaek.TOKENS}}</style> ..."  # 토큰(색·폰트 변수)만

테마: 기본 라이트. 다크는 <html> 또는 상위요소에 class="theme-dark" 또는
      data-theme="dark". 시스템 다크도 자동(prefers-color-scheme).
"""

__version__ = "{VERSION}"

TOKENS = r"""
{tokens}
"""

COMPONENTS = r"""
{components}
"""

# 대시보드 키트(Phase 6) — 표준 부품(.yb-kpi/.yb-panel/.yb-table…). 새 도구는 이걸 조립.
DASHBOARD = r"""
{dashboard}
"""

# 레거시 변수 호환(--plane/--bg/--panel/--ink… → 캐논 토큰). 기존 도구 편입용.
COMPAT = """{COMPAT}"""

CSS = TOKENS + "\\n" + COMPONENTS + "\\n" + DASHBOARD

# 차트 헬퍼 JS (Phase 7) — window.YB.line/spark/donut/bars
CHARTS_JS = r"""
{charts}
"""

# 기존 도구(자체 변수명 사용)를 위한 토큰+호환 묶음.
TOKENS_COMPAT = TOKENS + "\\n" + COMPAT


def style_tag(full=True):
    """<style>...</style> 문자열. full=False 면 토큰(변수)만."""
    return "<style>\\n" + (CSS if full else TOKENS) + "\\n</style>"


def script_tag():
    """<script>...</script> 문자열 — 차트 헬퍼(window.YB) 주입용."""
    return "<script>\\n" + CHARTS_JS + "\\n</script>"
'''

with open(os.path.join(BASE, "yeobaek.py"), "w", encoding="utf-8") as f:
    f.write(out)

print(f"생성 완료: yeobaek.py  (v{VERSION}, {len(out):,} bytes)")
print(f"  TOKENS {len(tokens):,}자 · COMPONENTS {len(components):,}자")
