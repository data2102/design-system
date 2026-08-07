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

for label, txt in (("tokens.css", tokens), ("components.css", components)):
    if '"""' in txt:
        raise SystemExit(f"{label} 에 三중따옴표(\"\"\") 가 있어 번들 불가. 확인 필요.")

VERSION = "1.4.0"

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

CSS = TOKENS + "\\n" + COMPONENTS


def style_tag(full=True):
    """<style>...</style> 문자열. full=False 면 토큰(변수)만."""
    return "<style>\\n" + (CSS if full else TOKENS) + "\\n</style>"
'''

with open(os.path.join(BASE, "yeobaek.py"), "w", encoding="utf-8") as f:
    f.write(out)

print(f"생성 완료: yeobaek.py  (v{VERSION}, {len(out):,} bytes)")
print(f"  TOKENS {len(tokens):,}자 · COMPONENTS {len(components):,}자")
