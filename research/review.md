# 검토 목록

조사에서 나온 **"DS에 반영할까?" 후보**를 모아 두는 곳. 여기 있는 것은 아직 규칙이 아니다.

## 규칙

- 조사(주간 리서치, 점검)는 이 표에 **행을 추가만** 한다. DS 본체 파일은 건드리지 않는다
- 사용자와 검토해서 상태를 정한다. **채택**된 것만 본체에 반영하고 CHANGELOG에 적는다
- 비슷한 후보가 이미 있으면 새 행을 만들지 않고 그 행의 출처에 덧붙인다
- 한 번에 많이 반영하지 않는다. 검토 한 번에 채택 1~3개

상태: `대기` → `채택`(반영함) / `보류`(나중에 다시) / `버림`(안 함, 이유 적기)

DS 본체 = `tokens.css` `components.css` `dashboard.css` `marketing.css` `charts.js` `design-system.md` `foundations.md` `components.md` `yeobaek.py`

## 후보

| ID | 제안 | 근거 | 영향 파일 | 상태 | 결정일 | 결정 이유 |
|---|---|---|---|---|---|---|
| R-001 | 알약 버튼 `.ds-btn-pill.primary` 의 파란 색 그림자 제거 | [ai-tells](ai-tells.md) V11 | marketing.css | 대기 | | |
| R-002 | 히어로 `.ds-hero-wrap` 틴트 그라디언트를 선택 옵션으로 (기본은 단색) | V1 | marketing.css | 대기 | | |
| R-003 | `.ds-feature-card` 기본 그림자 제거, 테두리만. 주인공 카드 변형(`--lead`) 추가 | V4, V7 | marketing.css | 대기 | | |
| R-004 | 마케팅 섹션 제목 정렬 기본을 왼쪽으로 (가운데는 옵션) | V6 | marketing.css | 대기 | | |
| R-005 | 제목 전용 굵기·자간 토큰(또는 제목 서체) 분리 | V2 | tokens.css | 대기 | | |
| R-006 | "갱신 날짜" 표기 패턴 (카드·표 위 기준일 한 줄) 컴포넌트화 | T3, T4 · [ASAP 리더보드](https://asapai.co.kr/leaderboard/) | components.css, components.md | 대기 | | |
| R-007 | 화면 완성 전 점검 단계로 AI 티 체크리스트를 foundations 에 연결 | ai-tells 전체 | foundations.md | 대기 | | |
| R-008 | 문구 규칙에 C2~C5 (대구·셋 나열·대시·슬로건 반복 피하기) 추가 | C2~C5 | design-system.md | 대기 | | |
