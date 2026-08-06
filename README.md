# 여백(Yeobaek) Design System

내 모든 도구·리포트·대시보드가 "한 사람이 만든 것"처럼 보이게 하는 공통 기초.
철학은 **여백** — 정보를 더하는 게 아니라 빼는 것이 디자인이다.

베이스는 **토스류 미니멀**(밝은 화면), 모니터링·자동화 도구에는 **다크 옵션**을 쓴다.

## 구성

| 파일 | 역할 |
|---|---|
| [`design-system.md`](design-system.md) | 원칙 + 토큰 + 컴포넌트 규칙 (기준서) |
| [`tokens.css`](tokens.css) | 웹/HTML용 CSS 변수 |
| [`tokens.py`](tokens.py) | Python(GUI·HTML 생성)용 상수 |
| [`components.css`](components.css) | 컴포넌트 (폼·입력 등). tokens.css 다음에 로드 |
| [`components.md`](components.md) | 컴포넌트 사용법 문서 |
| [`showcase.html`](showcase.html) | 컴포넌트 미리보기 (더블클릭해서 열기) |
| [`references.md`](references.md) | 참고 디자인 시스템 + 훔칠 것 |
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

**Python**
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
https://raw.githubusercontent.com/data2102/design-system/main/tokens.py
https://raw.githubusercontent.com/data2102/design-system/main/design-system.md
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

- **v1.0** (2026-08) — 초기 토큰(라이트/다크) + 기본 컴포넌트(버튼·카드·메트릭·배지·리스트)
