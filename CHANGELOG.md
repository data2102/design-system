# CHANGELOG

여백(Yeobaek) 디자인 시스템 변경 기록. 최신이 위로.

## [Unreleased]
- 다음: Phase 8(확장·밀도·접근성). (선택) 파이썬 컴포넌트 헬퍼 `yeobaek.kpi()`, 중앙 업데이터

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
