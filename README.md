# 여백(Yeobaek) Design System

내 모든 도구·리포트·대시보드가 "한 사람이 만든 것"처럼 보이게 하는 공통 기초.
철학은 **여백** — 정보를 더하는 게 아니라 빼는 것이 디자인이다.

베이스는 **토스류 미니멀**(밝은 화면), 모니터링·자동화 도구에는 **다크 옵션**을 쓴다.

**🌐 라이브 미리보기 (공유용 링크)**
- 디자인 시스템 소개 → https://data2102.github.io/design-system/
- 작업물 적용 예시 → https://data2102.github.io/design-system/examples.html

---

## 🗣️ Claude에게 요청하는 법

다른 작업물에 이 디자인 시스템을 입히고 싶을 때, 이렇게 요청하면 된다.

**① 가장 간단 (보통 이거면 됨)**
> 여백 디자인 시스템으로 ○○ 만들어줘

**② 확실하게 (새 세션·중요한 작업 — 복붙용)**
```
내 디자인 시스템(github.com/data2102/design-system)을 적용해서 ○○을 만들어줘.
- tokens.css / components.css / foundations.md 기준으로
- 라이트 기본 (모니터링·자동화 화면이면 다크로)
```

**③ 실제 코드 파일에 입힐 때**
> github.com/data2102/design-system 의 tokens.css·components.css를 적용해서 ○○.html(또는 .py)을 우리 디자인으로 바꿔줘

**요청할 때 같이 주면 좋은 것**
- 무엇을: 작업물 이름 / 파일 경로(있으면 첨부)
- 테마: 라이트(기본) vs 다크(모니터링·자동화)
- 형태: ⓐ 실제 도구에 적용(코드에 CSS 연결) / ⓑ 공유용 독립 HTML 한 장(폰트 내장)

> 💡 핵심: **"여백 디자인 시스템으로"** 면 대부분 되고, 확실히 하려면 **이 repo 링크를 같이** 주면 Claude가 실제 최신 파일을 읽어서 정확히 적용한다.

---

## 구성

| 파일 | 역할 |
|---|---|
| [`design-system.md`](design-system.md) | 원칙 + 토큰 + 컴포넌트 규칙 (기준서) |
| [`tokens.css`](tokens.css) | 웹/HTML용 CSS 변수 |
| [`tokens.py`](tokens.py) | Python(GUI·HTML 생성)용 상수 |
| [`components.css`](components.css) | 컴포넌트 (폼·피드백·오버레이). tokens.css 다음에 로드 |
| [`components.md`](components.md) | 컴포넌트 사용법 문서 |
| [`foundations.md`](foundations.md) | 토대 규칙 (상호작용 상태·모션·아이콘·접근성·데이터viz) |
| [`dashboard.css`](dashboard.css) | 대시보드 표준 부품 (`yb-*` 컴포넌트) |
| [`charts.js`](charts.js) | 차트 헬퍼 `window.YB` (line·spark·donut·bars) |
| [`a11y_check.py`](a11y_check.py) | 색 대비 WCAG 자동점검 (라이트/다크) |
| [`scaffold/`](scaffold/) | 새 대시보드 스캐폴드 (복사→데이터만 채우기) |
| [`yeobaek.py`](yeobaek.py) | 파이썬 도구용 단일 소스 (CSS 번들). `import yeobaek` |
| [`build_yeobaek.py`](build_yeobaek.py) | css → yeobaek.py 생성기 |
| [`update_ds.py`](update_ds.py) · `DS업데이트.bat` | 도구 폴더에서 yeobaek.py 최신화 |
| [`showcase.html`](showcase.html) | 컴포넌트 미리보기 (더블클릭해서 열기) |
| [`references.md`](references.md) | 참고 디자인 시스템 + 훔칠 것 |
| [`ai-workflow.md`](ai-workflow.md) | AI 워크플로우 로드맵 — Claude Code × Figma MCP로 DS 자동화(피그마↔코드 대응, CLAUDE.md/DESIGN.md, QA) |
| [`effects.md`](effects.md) | 화면 효과(리퀴드 로고·유리 패널·셰이더 그라디언트·3D) — 랜딩 전용 예외 규칙 + Claude 요청 문구 |
| [`ui-dictionary.md`](ui-dictionary.md) | UI 이름 사전 — 영역별(알림·로딩·폼·AI·빈 화면·제스처·모션·이동·다크패턴·아이콘) 이름 ↔ 여백 DS 매핑 |
| [`roadmap.md`](roadmap.md) | 발전 로드맵 (L2→L3) + 컴포넌트 백로그 |
| [`CHANGELOG.md`](CHANGELOG.md) | 버전 변경 기록 |

## 쓰는 법

**HTML / 웹 리포트**
```html
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="components.css">  <!-- 폼 등 컴포넌트 쓸 때 -->
<div class="ds-page"><div class="ds-card">…</div></div>
<!-- 모니터링 화면이면 상위 요소에 class="theme-dark" -->
```

**Python 도구 (serve.py 등) — 단일 소스 `yeobaek.py`** ⭐
```python
import yeobaek                       # 폴더에 yeobaek.py 를 함께 둠(vendoring)
html = f"<style>{yeobaek.CSS}</style> ..."     # 전체(토큰+컴포넌트)
# 또는 토큰(변수)만:  f"<style>{yeobaek.TOKENS}</style>"
```
- DS를 고칠 때 각 도구를 손볼 필요 없이 **`DS업데이트.bat` 실행 → 도구 재실행**만으로 반영.
- `yeobaek.py` 는 `build_yeobaek.py` 가 tokens.css + components.css 로부터 생성(직접 편집 금지).
- 오프라인에서도 폴더 안 사본으로 동작. 업데이트할 때만 인터넷 필요.

**토큰 값 상수만 필요할 때**
```python
from tokens import LIGHT, DARK, FS, SP, css_vars
T = DARK if 모니터링화면 else LIGHT
```

**Claude에게 시킬 때**
> "여백 디자인 시스템으로 만들어줘"

## 어디서든 불러쓰기 (raw URL)

GitHub에 올려서 아래 주소로 어느 환경에서든 바로 가져올 수 있다.

```
https://raw.githubusercontent.com/data2102/design-system/main/tokens.css
https://raw.githubusercontent.com/data2102/design-system/main/components.css
https://raw.githubusercontent.com/data2102/design-system/main/tokens.py
https://raw.githubusercontent.com/data2102/design-system/main/foundations.md
https://raw.githubusercontent.com/data2102/design-system/main/components.md
```

저장소: https://github.com/data2102/design-system

## 원칙 5줄 요약

1. 한 화면, 한 가지 일 — 중요한 숫자 하나를 크게, 나머지는 조용히
2. 파랑은 "누를 수 있는 것"에만
3. 색은 신호지 장식이 아니다
4. 말하듯 쓴다 ("~했어요")
5. 여백이 곧 고급스러움

---

살아있는 문서. 새 화면 만들다 없는 컴포넌트가 나오면 여기에 역으로 추가하고 버전을 올린다.

## 버전

- **v1.4** (2026-08) — Foundations + Phase 1~4 전체(폼·피드백·오버레이·데이터탐색·시각화). 컴포넌트 세트 완성(L3)
- 상세 이력은 [`CHANGELOG.md`](CHANGELOG.md)
