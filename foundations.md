# Foundations (토대 규칙)

컴포넌트가 딛고 서는 공통 규칙. 값은 [`tokens.css`](tokens.css)/[`tokens.py`](tokens.py)에, 여기엔 "언제·어떻게".

## 상호작용 상태 (모든 컴포넌트 공통)

어떤 컴포넌트든 아래 상태를 이 규칙으로 표현한다. (일관성의 핵심)

| 상태 | 표현 |
|---|---|
| **default** | 기본 |
| **hover** | 테두리/배경 한 단계 진하게 (`--text-tertiary` 테두리, `--surface-sunken` 배경) |
| **focus** | `--shadow-focus` 파란 링. **절대 지우지 않는다**(접근성). 에러 시 `--shadow-focus-danger` |
| **active** | `transform: scale(.98)` 살짝 눌림 |
| **disabled** | `--surface-sunken` 배경 + `--text-disabled` + `cursor:not-allowed`. 남용 금지(가능하면 활성 유지) |
| **error** | `--danger` 테두리 + 아래 에러 메시지. 필드에 `.is-error`, 입력에 `aria-invalid` |
| **loading** | 스피너/스켈레톤. 버튼은 텍스트를 로딩 문구로 바꾸고 비활성 |

## 모션

- **duration**: `--dur-fast`(120ms, hover·툴팁) · `--dur-base`(200ms, 대부분) · `--dur-slow`(320ms, 큰 전환)
- **easing**: `--ease-standard`(대부분) · `--ease-out`(등장)
- **`prefers-reduced-motion`**: 애니메이션은 항상 이 미디어쿼리로 끌 수 있게. (components.css에 반영됨)
- 원칙: 움직임은 **의미 전달용**(등장·상태변화)만. 장식용 애니메이션은 AI스러워 보이니 자제.

## 아이콘

- **하나의 아웃라인 세트로 통일**한다. 권장: **Tabler** 또는 **Lucide**(둘 다 무료·아웃라인·한 벌).
- 채운(filled) 아이콘·이모지와 **혼용 금지**.
- 크기: 인라인 16~20px, 장식 최대 24px. 색은 부모 `color` 상속.
- 웹: Tabler 웹폰트(`<i class="ti ti-bell">`) 또는 인라인 SVG. Python GUI: 같은 세트의 PNG/SVG 에셋.

## 접근성 기준 (최소선)

- **대비**: 본문 텍스트 4.5:1 이상, 큰 텍스트 3:1 이상.
- **포커스**: 키보드 포커스 링 필수(`--shadow-focus`). 마우스에만 의존 금지.
- **터치 타겟**: 최소 44×44px (버튼·체크박스 등).
- **폼**: `label[for]`↔`input[id]` 연결, 에러 시 `aria-invalid`, 도움말은 `aria-describedby`.
- **오버레이**: 모달은 `role="dialog" aria-modal="true"`, ESC 닫기, 포커스 트랩, 열기 전 요소로 포커스 복귀.
- **색만으로 정보 전달 금지**: 상태는 색 + 아이콘/텍스트 함께.

## z-index 스케일

`--z-dropdown:1000` · `--z-sticky:1100` · `--z-overlay:1200` · `--z-modal:1300` · `--z-toast:1400` · `--z-tooltip:1500`.
임의의 큰 숫자(9999) 쓰지 말고 이 스케일만 사용.

## Breakpoints

| 이름 | 폭 | 용도 |
|---|---|---|
| sm | ~640px | 모바일 |
| md | 641–1024px | 태블릿 |
| lg | 1025px~ | 데스크톱 |

- 모바일 우선. 좁은 화면에서 다단 → 1단으로 접기.

## 데이터 시각화 팔레트

- 카테고리 색: `--viz-1`(파랑) `--viz-2`(초록) `--viz-3`(앰버) `--viz-4`(테라코타) `--viz-5`(보라) `--viz-6`(핑크). 라이트/다크 공통으로 무난.
- 색은 **의미에 매핑**(카테고리별 고정), 무지개처럼 순서대로 돌리지 않기.
- 단일 지표 추이는 액센트색 하나 + 영역 채움. 강조점(끝점)만 진하게.
- 상태색(성공/경고/위험)은 데이터 색과 분리해서 쓴다.
