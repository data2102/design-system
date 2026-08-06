# 발전 로드맵 (L2 → L3)

여백 디자인 시스템을 "실제 템플릿에 바로 쓸 수 있는" 수준으로 키우는 계획.
원칙: **한 번에 다 만들지 않는다.** 실제 도구를 만들다 필요한 컴포넌트가 나오면 그때 이 백로그에서 꺼내 채우고 버전업.

## 현재 상태 (v1.0 · L2)

- ✅ Foundations: 색(라이트/다크)·타이포·간격·둥글기·그림자 일부
- ✅ Components: 버튼, 카드, 메트릭, 배지, 리스트 행 (5개)
- ❌ 없음: 폼/입력 컴포넌트, 오버레이(모달·토스트), 테이블, 탐색, 모션·아이콘·접근성 규칙, Patterns 층 전체

## Foundations 먼저 보강 (컴포넌트의 토대)

- [ ] **상호작용 상태 규칙** — 모든 컴포넌트 공통: default / hover / focus / active / disabled / error / loading. (Material의 state layer 참고)
- [ ] **모션 토큰** — duration(fast 120ms / base 200ms / slow 320ms), easing(standard/ease-out). `prefers-reduced-motion` 대응.
- [ ] **아이콘 세트 확정** — 하나의 아웃라인 세트로 통일(예: Tabler / Lucide). 크기·굵기 규칙.
- [ ] **접근성 기준** — 대비 최소 4.5:1, 포커스 링 필수, 터치 타겟 44px, ARIA 기본.
- [ ] **breakpoints / z-index / elevation** 스케일 명문화.
- [ ] **데이터 시각화 팔레트** — 차트용 카테고리 색 + 순차/발산 램프 (Carbon 참고).

## 컴포넌트 백로그 (우선순위 = 업무 도구에 필요한 순)

### Phase 1 — 폼 · 입력 (업무 자동화 도구의 핵심)
- [ ] TextInput (label / help / error / prefix·suffix)
- [ ] Textarea
- [ ] Select · Dropdown
- [ ] Checkbox · Radio · Switch(토글)
- [ ] Search 입력
- [ ] DatePicker (또는 date input 스타일)
- [ ] Form 레이아웃 규칙 (라벨 위치, 필수 표시, 에러 노출)

### Phase 2 — 피드백 · 오버레이
- [ ] Toast (성공/경고/오류, 자동 사라짐)
- [ ] Modal · Dialog (포커스 트랩, ESC 닫기)
- [ ] Tooltip · Popover
- [ ] Banner · Alert (인라인 상태 메시지)
- [ ] Loading · Skeleton · Progress
- [ ] EmptyState (빈 화면 = 사과 말고 초대)

### Phase 3 — 데이터 · 탐색
- [ ] Table (정렬 / 필터 / 페이지네이션 / 고정 헤더)
- [ ] Tabs
- [ ] Pagination
- [ ] Breadcrumb
- [ ] Sidebar · 상단 Nav
- [ ] Chip · Filter
- [ ] Accordion
- [ ] Avatar · Stepper

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
