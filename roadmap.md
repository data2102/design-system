# 발전 로드맵 (L2 → L3)

여백 디자인 시스템을 "실제 템플릿에 바로 쓸 수 있는" 수준으로 키우는 계획.
원칙: **한 번에 다 만들지 않는다.** 실제 도구를 만들다 필요한 컴포넌트가 나오면 그때 이 백로그에서 꺼내 채우고 버전업.

## 현재 상태 (v1.0 · L2)

- ✅ Foundations: 색(라이트/다크)·타이포·간격·둥글기·그림자 일부
- ✅ Components: 버튼, 카드, 메트릭, 배지, 리스트 행 (5개)
- ❌ 없음: 폼/입력 컴포넌트, 오버레이(모달·토스트), 테이블, 탐색, 모션·아이콘·접근성 규칙, Patterns 층 전체

## Foundations 보강 (컴포넌트의 토대) ✅ v1.2.0 → [`foundations.md`](foundations.md)

- [x] **상호작용 상태 규칙** — default / hover / focus / active / disabled / error / loading
- [x] **모션 토큰** — duration(fast/base/slow), easing. `prefers-reduced-motion` 대응
- [x] **아이콘 세트 규칙** — 아웃라인 한 벌(Tabler/Lucide 권장)
- [x] **접근성 기준** — 대비 4.5:1, 포커스 링, 터치 44px, ARIA
- [x] **z-index / breakpoints** 스케일 명문화
- [x] **데이터 시각화 팔레트** — `--viz-1~6`

## 컴포넌트 백로그 (우선순위 = 업무 도구에 필요한 순)

### Phase 1 — 폼 · 입력 (업무 자동화 도구의 핵심) ✅ v1.1.0
- [x] TextInput (label / help / error)
- [x] Textarea
- [x] Select · Dropdown
- [x] Checkbox · Radio · Switch(토글)
- [x] Search 입력
- [ ] DatePicker (또는 date input 스타일) — 남음
- [x] Form 레이아웃 규칙 (라벨 위치, 필수 표시, 에러 노출)

### Phase 2 — 피드백 · 오버레이 ✅ v1.2.0
- [x] Toast (성공/경고/오류, 자동 사라짐)
- [x] Modal · Dialog (ESC 닫기, aria-modal)
- [x] Tooltip
- [x] Banner · Alert (인라인 상태 메시지, 4종)
- [x] Loading · Skeleton · Progress
- [x] EmptyState (빈 화면 = 사과 말고 초대)
- [ ] Popover — 남음 (Phase 3에서)

### Phase 3 — 데이터 · 탐색 ✅ v1.3.0
- [x] Table (정렬 / hover / 고정 헤더)
- [x] Tabs
- [x] Pagination
- [x] Breadcrumb
- [x] Sidebar · Nav
- [x] Chip · Filter
- [x] Accordion
- [x] Avatar · Stepper
- [x] Popover (Phase 2 잔여분 완료)

### Phase 4 — 데이터 시각화
- [ ] KPI 카드 확장, Sparkline, 막대/선 차트 스타일, 상태 뱃지 확장

## Patterns 층 (컴포넌트 조합)
- [ ] 폼 검증 흐름 (입력 → 에러 → 성공)
- [ ] 빈 상태 / 로딩 / 에러 3종 세트
- [ ] 리스트 → 상세 이동
- [ ] 대시보드 레이아웃 (KPI + 목록 + 사이드)
- [ ] 필터링 & 검색 패턴

## 컴포넌트 하나 추가할 때의 규칙 (매번 이 틀로)

1. **해부(anatomy)** — 구성 요소와 각 부분이 쓰는 토큰
2. **variants** — 종류 (예: 버튼 primary/secondary/ghost)
3. **states** — default / hover / focus / active / disabled / error / loading
4. **접근성** — 키보드 조작, ARIA, 포커스, 대비
5. **마이크로카피** — 이 컴포넌트에서의 말투 예시
6. **코드** — `tokens.css` 클래스 + `tokens.py` 반영 + showcase.html에 추가

## 버전 규칙

- Foundation 보강·컴포넌트 추가 = minor (v1.1, v1.2 …)
- 색·간격 등 토큰 값 변경(기존 화면에 영향) = major (v2.0)
- 기록은 [`CHANGELOG.md`](CHANGELOG.md)에.
