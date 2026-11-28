# 레퍼런스 라이브러리

여백 디자인 시스템을 발전시킬 때 참고하는 실제 디자인 시스템들과, **각각에서 구체적으로 훔칠 것**.
(디자인 시스템은 보통 **Foundations → Components → Patterns** 3층으로 구성된다. 우리는 지금 Foundations + 기본 Components만 있고 Patterns는 비어 있음.)

## 디자인 시스템의 3층 구조

| 층 | 내용 | 우리 상태 |
|---|---|---|
| **Foundations** | 색·타이포·간격·둥글기·그림자·모션·아이콘·접근성 토큰 | 절반 (모션·아이콘·접근성 규칙 없음) |
| **Components** | 버튼·인풋·카드·모달·토스트·테이블 등 재사용 UI | 5개뿐 (버튼·카드·메트릭·배지·리스트) |
| **Patterns** | 로그인·폼 검증·빈 상태·대시보드 레이아웃 등 "조합된 사용법" | 없음 |

## 참고 시스템 & 훔칠 것

| 시스템 | 강점 | 여백 DS가 훔칠 것 | 링크 |
|---|---|---|---|
| **Toss TDS** | 한국어 서비스, 친근한 톤, 큰 숫자 중심 | 마이크로카피 말투, 컬러 역할 최소화, Flat+Compound API 병행 | [toss.tech](https://toss.tech/article/toss-design-system) · [컬러 업데이트](https://toss.tech/article/tds-color-system-update) · [컴포넌트](https://developers-apps-in-toss.toss.im/design/components.html) |
| **Material 3** | 토큰 3계층, 상태 레이어(hover/press 오버레이), elevation | 토큰 계층화, 상호작용 상태(state layer) 규칙, 모션 토큰 | [m3.material.io](https://m3.material.io) |
| **Shopify Polaris** | 컴포넌트 문서 구조가 모범 | 컴포넌트 페이지 틀: 해부(anatomy)→상태→best practices→content | [polaris.shopify.com](https://polaris.shopify.com) |
| **Ant Design** | 엔터프라이즈 폼·테이블·데이터 밀도 | 업무 도구용 폼/테이블 컴포넌트 설계 | [ant.design](https://ant.design/components/overview) |
| **Radix UI / shadcn/ui** | 접근성 headless 패턴, 코드로 바로 가져다 씀 | 키보드/포커스/ARIA 접근성 로직 — 우리 코드 워크플로우에 직결 | [radix-ui.com](https://www.radix-ui.com/primitives) · [ui.shadcn.com](https://ui.shadcn.com) |
| **IBM Carbon** | 데이터 시각화·그리드·토큰 명명 | 차트 팔레트 규칙, 데이터 viz 가이드 | [carbondesignsystem.com](https://carbondesignsystem.com) |
| **GitLab Pajamas / Nord** | 컴포넌트별 usage·접근성 문서 예시 | 모달·토스트 등 개별 컴포넌트 사용 규칙 서술 방식 | [design.gitlab.com](https://design.gitlab.com) · [nordhealth.design](https://nordhealth.design) |

## 학습용 메타 자료

- DS 자동화 커리큘럼(Claude Code × Figma MCP) — 패스트캠퍼스 교육과정 소개서 → 우리 로드맵은 [`ai-workflow.md`](ai-workflow.md)
- 화면 효과 오픈소스 4종 고르기 — [HANIEE_IM 가이드](https://hani.nioh.cloud/guides/claude-code-site-effects) → 우리 규칙은 [`effects.md`](effects.md)
- UI 이름 사전(영역 분류의 기준) — [우디디자인랩 UI 미니 사전](https://woodydesignlab.com/ui/dict) → 우리 매핑은 [`ui-dictionary.md`](ui-dictionary.md)

- 디자인 시스템 해부 개념 — [The Design System Guide](https://thedesignsystem.guide/foundations)
- 컴포넌트/접근성 체크리스트 — [designsystemchecklist.com](https://www.designsystemchecklist.com)
- 스터디할 실제 시스템 모음 — [UXPin: 15 best design systems](https://www.uxpin.com/studio/blog/best-design-system-examples/)

## 조사에서 얻은 핵심 원칙

1. **컴포넌트 문서에는 "해부도(anatomy)"를 넣는다** — 어느 부분이 어느 토큰의 영향을 받는지 명시하면 구현 모호함이 사라짐.
2. **디자이너·개발자 둘 다 1급 독자**로 다룬다 — 사용 가이드 + 코드 구현을 같은 페이지에.
3. **베이스라인 컴포넌트 세트**: Button, Input, Select, Card, Modal, Table/List, Tabs, Toast, EmptyState. (우리는 이 중 Card만 있음)
4. **큰 시스템도 라이브러리는 ~8개**(tokens, components, icons, docs, patterns, illustrations, themes)로 나뉜다 — 우리는 아직 하나로 충분.
