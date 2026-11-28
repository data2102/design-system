# CHANGELOG

여백(Yeobaek) 디자인 시스템 변경 기록. 최신이 위로.

## [Unreleased]
### Changed — 검토에서 채택 (2026-11-28, [`research/review.md`](research/review.md) R-009 · R-010 · R-011)
- `--text-tertiary` #8b95a1 → **#5f6a78**. 안내 문장에 쓰면 흰 바탕 대비가 3.0 : 1 이었다 → 5.5 : 1 (R-009)
- `--warm` #c96f4c → **#a8522f**. 글자·흰 글자 바탕 모두 3.1~3.6 : 1 → 5.4 : 1 (R-010). `--viz-4` 는 그대로
- `.ds-btn-pill.primary` 바탕 `--accent` → **`--accent-strong`**, hover 는 `--accent-pressed`. 흰 글자 3.7 : 1 → 5.7 : 1 (R-011)
- `a11y_check.py`: `text-tertiary` 기준을 3.0 → 4.5 로, `text-tertiary/bg` · `warm/surface` · `on-accent/warm` 쌍 추가. 라이트/다크 전 항목 통과
- `tokens.py` · `yeobaek.py` · `scaffold/yeobaek.py` 같이 갱신. 예시 HTML(`index.html` · `examples.html`)에 직접 적힌 옛 색은 아직 그대로
- 근거와 잰 값: [`research/audits/refloworks-2026-11-28-적용기록.md`](research/audits/refloworks-2026-11-28-적용기록.md). 후보 R-012~R-018 은 `대기`
- **조사 기록 폴더** [`research/`](research/) 추가 — 조사를 모아 두고, DS 반영은 검토 후 채택분만
  - [`research/review.md`](research/review.md): 검토 목록. 후보 R-001~R-008 (모두 `대기`). DS 본체는 아직 안 바꿈
  - [`research/ai-tells.md`](research/ai-tells.md): AI 티 체크리스트 조사 자료(화면 V1~V11·문구 C1~C7·신뢰 T1~T6·코드) + `marketing.css` 자체 점검
  - [`research/weekly/`](research/weekly/): 주간 AI 활용 리서치 요약 (매주 월요일 자동 추가)
  - [`research/audits/refloworks-2026-11-27.md`](research/audits/refloworks-2026-11-27.md): refloworks.com 구조·문구 점검
### Added
- **사이트 유형별 커버리지 조사** [`research/site-types.md`](research/site-types.md) — 12개 유형 × 필요한 페이지·부품·레퍼런스, 공통 부품 6묶음. 검토 후보 R-021~R-034 추가(모두 `대기`, 본체는 안 바꿈). [`references.md`](references.md)에 사이트 유형별 1차 레퍼런스 표
- **무드·이미지 레퍼런스 사이트** 3곳(세이비·코스모스·디자인스퍼레이션)을 [`references.md`](references.md)에 추가 — 용도와 "영감만, 색은 토큰으로" 규칙
- **AI 워크플로우 로드맵** [`ai-workflow.md`](ai-workflow.md) 추가 — 피그마 요소 4종(컴포넌트·프로퍼티·베리어블·스타일) ↔ 여백 코드 대응, CLAUDE.md/DESIGN.md·에이전트·Figma MCP·Code Connect 현황, 시스템 기반 프롬프트 체크리스트, QA. roadmap Phase 9로 연결
- **화면 효과 규칙** [`effects.md`](effects.md) 추가 — 리퀴드 로고·리퀴드 글래스·셰이더 그라디언트·3D(React Three Fiber)를 랜딩 히어로에 한 개만 쓰는 예외 규칙, 토큰 색·reduced-motion·정적 대체·라이선스 체크리스트, Claude 요청 문구. ui-dictionary "움직임"·안티패턴과 연결
- fix: 가로 막대 차트 막대가 안 보이던 문제(`.ds-bar-fill` display:block)
- **UI 이름 사전** [`ui-dictionary.md`](ui-dictionary.md) 추가 — 10개 영역(알림과 피드백·로딩·입력 폼·AI 화면·빈 화면·제스처·움직임·이동 구조·다크 패턴·메뉴 아이콘 별명)별 UI 이름 ↔ 여백 DS 클래스 매핑, 고르는 규칙, 여백식 예시 문구. 빈칸은 roadmap "UI 사전 기반 백로그"로
- 고도화 로드맵(Phase 5~8) 완료. 이후는 실제 도구 쓰며 필요분 보강 + (선택) 파이썬 헬퍼·중앙 업데이터

## [1.9.0] — 2026-08-13
### Added
- **마케팅/랜딩 패턴** [`marketing.css`](marketing.css) — 웹 랜딩·브랜드 페이지용(레퍼 서비스 랜딩 "토스 임팩트" 방향에서 추출)
  - 히어로: 은은한 액센트 틴트 배경 블록(`.ds-hero-wrap`) + 중앙 정렬 임팩트(`.ds-hero`, `.ds-hero .accent`)
  - 알약형 CTA `.ds-btn-pill`(primary/ghost, 포커스 링·active 준수)
  - 플로팅 제품 목업 카드 `.ds-shot`, 기능 카드+아이콘칩 `.ds-feature-card`/`.ds-feature-ico`, 마무리 CTA 밴드 `.ds-cta-band`
  - 전부 토큰 기반 → 라이트 기본 + `[data-theme="dark"]` 자동 대응
- 예시: [`marketing-example.html`](marketing-example.html) (라이트/다크 토글 포함)

## [1.8.0] — 2026-08-07
### Added
- **Phase 8(확장·밀도·접근성) 완료**
- 확장 컴포넌트: 세그먼트 컨트롤(`.yb-seg`), 필터바(`.yb-filterbar`), yb 인터랙티브 요소 포커스 링
- `compact` 밀도 옵션(`.yb-compact` — 여백·글자 촘촘)
- **`a11y_check.py`** — tokens.css 색 대비 WCAG 자동점검(라이트/다크). DS 수정 후 회귀 방지
- 접근성 토큰 `--accent-strong`/`--success-strong`/`--warning-strong`/`--danger-strong` (연틴트 위 글자·채운버튼 AA 확보)
### Changed
- `.ds-btn-primary`·`.ds-badge-*`·`.yb-badge-*` 를 `-strong` 토큰으로 → 라이트/다크 **전 항목 WCAG AA 통과**

## [1.7.0] — 2026-08-07
### Added
- **Phase 7(차트 시스템)** — [`charts.js`](charts.js): DS 토큰 쓰는 미니 차트 헬퍼 `window.YB`(`line`/`spark`/`donut`/`bars`). hover 툴팁, 색은 var 토큰이라 라이트/다크·업데이트 자동
- `yeobaek.CHARTS_JS` + `yeobaek.script_tag()` (주입용), `dashboard.css`에 `.yb-chart`/`.yb-tt`
- 스캐폴드에 라인차트·도넛 데모 추가

## [1.6.0] — 2026-08-07
### Added
- **Phase 6(대시보드 키트) 시작** — [`dashboard.css`](dashboard.css): 표준 대시보드 부품 `yb-*`(kpi·panel·table·alert·bars·delta·chip·tabs·badge·legend·empty). `yeobaek.CSS`에 포함(`yeobaek.DASHBOARD`)
- [`scaffold/`](scaffold/) — 복사해서 데이터만 채우는 빈 대시보드(`serve.py` + README). yeobaek import + 다크토글 + HTML내보내기 기본 탑재
- `build_yeobaek.py`가 dashboard.css도 번들에 포함

## [1.5.0] — 2026-08-07
### Added
- **Phase 5(배포/연결) 완료** — 파이썬 도구용 단일 소스 `yeobaek.py`(`build_yeobaek.py`가 css에서 생성) + `update_ds.py`/`DS업데이트.bat`
- `COMPAT` 레이어(레거시 변수명 `--plane/--bg/--panel/--ink…` → 캐논 토큰) + `TOKENS_COMPAT`
### Changed
- 다크 셀렉터를 `.theme-dark, :root[data-theme="dark"]` 로 확장 (toggle 방식 도구 지원)
- 실도구 5종(일통계·트래픽·원가·매출·차단IP)을 `import yeobaek` 로 편입 → DS 수정 시 **`DS업데이트.bat` + 재실행**만으로 전 도구 반영 (도구별 CSS 수동 편집 종료)

## [1.4.0] — 2026-08-06
### Added
- **Phase 4 데이터 시각화** ([`components.css`](components.css)): 확장 KPI(ds-stat), Delta 추세(pos/neg), 가로 막대차트(ds-bars), 범례(ds-legend), 도넛/링(ds-donut), Sparkline·라인/영역 차트 SVG 레시피
- `showcase.html`에 Phase 4 섹션 추가
- 최종 통합 쇼케이스 v1.4 (Foundations + Phase 1~4 한 페이지)

## [1.3.0] — 2026-08-06
### Added
- **Phase 3 데이터·탐색** ([`components.css`](components.css)): Table(정렬·hover·sticky), Tabs, Pagination, Breadcrumb, Nav(사이드바), Chip/Filter, Accordion(details 기반), Avatar, Stepper, Popover
- `showcase.html`에 Phase 2·3 섹션 추가

## [1.2.0] — 2026-08-06
### Added
- **Phase 1 마무리**: DatePicker(date input) 스타일
- **Phase 2 피드백·오버레이** ([`components.css`](components.css)): Banner/Alert(4종), Toast, Modal/Dialog, Tooltip, Spinner, Skeleton, Progress, EmptyState
- **Foundations 보강** ([`foundations.md`](foundations.md)): 상호작용 상태 규칙, 모션 토큰(`--dur-*`,`--ease-*`), z-index 스케일, 데이터 시각화 팔레트(`--viz-1~6`), 아이콘·접근성·breakpoint 기준
- `prefers-reduced-motion` 대응
- 최종 통합 쇼케이스 아트팩트

## [1.1.0] — 2026-08-06
### Added
- **Phase 1 폼·입력 컴포넌트** ([`components.css`](components.css), [`components.md`](components.md)):
  TextInput, Textarea, Select, Search, Checkbox, Radio, Switch + 폼 레이아웃(라벨/도움말/에러)
- 상호작용 상태 규칙: hover / focus / disabled / error 를 모든 폼 요소에 적용
- 토큰 추가: `--shadow-focus-danger` (에러 포커스 링)
- `showcase.html`에 폼 섹션 추가
- 레퍼런스 라이브러리([`references.md`](references.md))·발전 로드맵([`roadmap.md`](roadmap.md)) 추가

## [1.0.1] — 2026-08-06
### Changed
- 기본 폰트를 `Pretendard` → **`Noto Sans KR`**로 변경 (부드럽고 인간적). 폴백: Pretendard → 맑은 고딕.

## [1.0.0] — 2026-08-06
### Added
- Foundations: 색 토큰(라이트/다크), 타이포, 간격(4px 스케일), 둥글기, 그림자
- Components: 버튼(primary/secondary), 카드, 메트릭, 배지, 리스트 행
- `tokens.css`, `tokens.py`, `design-system.md`, `showcase.html`
- GitHub 공개 저장소로 배포: https://github.com/data2102/design-system
