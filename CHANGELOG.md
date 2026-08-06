# CHANGELOG

여백(Yeobaek) 디자인 시스템 변경 기록. 최신이 위로.

## [Unreleased]
- 다음: Foundations 보강(상호작용 상태·모션·아이콘) 또는 Phase 2(피드백·오버레이)

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
