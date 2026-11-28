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
| R-001 | 알약 버튼 `.ds-btn-pill.primary` 의 파란 색 그림자 제거 | [ai-tells](ai-tells.md) V11 · refloworks 사본에 먼저 적용(11/26) | marketing.css | 대기 | | |
| R-002 | 히어로 `.ds-hero-wrap` 틴트 그라디언트를 선택 옵션으로 (기본은 단색) | V1 · refloworks 사본은 단색으로 바꿈(11/27, `.ds-cta-band` 도) | marketing.css | 대기 | | |
| R-003 | `.ds-feature-card` 기본 그림자 제거, 테두리만. 주인공 카드 변형(`--lead`) 추가 | V4, V7 | marketing.css | 대기 | | |
| R-004 | 마케팅 섹션 제목 정렬 기본을 왼쪽으로 (가운데는 옵션) | V6 | marketing.css | 대기 | | |
| R-005 | 제목 전용 굵기·자간 토큰(또는 제목 서체) 분리 | V2 | tokens.css | 대기 | | |
| R-006 | "갱신 날짜" 표기 패턴 (카드·표 위 기준일 한 줄) 컴포넌트화 | T3, T4 · [ASAP 리더보드](https://asapai.co.kr/leaderboard/) | components.css, components.md | 대기 | | |
| R-007 | 화면 완성 전 점검 단계로 AI 티 체크리스트를 foundations 에 연결 | ai-tells 전체 | foundations.md | 대기 | | |
| R-008 | 문구 규칙에 C2~C5 (대구·셋 나열·대시·슬로건 반복 피하기) 추가 | C2~C5 | design-system.md | 대기 | | |
| R-009 | `--text-tertiary` 를 #5f6a78 로 (안내 문장에 쓰면 3.0 : 1 → 5.5 : 1). `a11y_check.py` 의 이 쌍 기준도 4.5 로 | [refloworks 적용기록](audits/refloworks-2026-11-28-적용기록.md) — 잰 값 | tokens.css, tokens.py, a11y_check.py, yeobaek.py | 채택 | 2026-11-28 | 안내 문장에 쓰는 색이라 본문 기준(4.5)이 맞음. 사이트에서 잰 값 3.0 → 5.5. a11y_check 기준도 4.5 로, bg 위 쌍 추가 |
| R-010 | `--warm` 을 #a8522f 로 (글자·흰 글자 바탕 3.1~3.6 : 1 → 5.4 : 1) | 같은 기록 | tokens.css, tokens.py | 채택 | 2026-11-28 | 글자·흰 글자 바탕 모두 3.1~3.6 → 5.4. a11y_check 에 warm 쌍 추가 |
| R-011 | `.ds-btn-pill.primary` 바탕을 `--accent-strong` 으로 (흰 글자 3.7 : 1 → 5.7 : 1) | 같은 기록 · v1.8 에서 `.ds-btn-primary` 는 이미 그렇게 함 | marketing.css | 채택 | 2026-11-28 | 흰 글자 3.7 → 5.7. `.ds-btn-primary` 와 같은 방식(v1.8) |
| R-012 | 제목 한 구절만 색칠하는 `.ds-hero h1 .accent` 를 제목과 같은 색으로 (또는 클래스 제거) | frontend-design 「한 낱말만 강조」 · Impeccable | marketing.css, marketing-example.html | 대기 | | |
| R-013 | `.ds-feature-ico` 의 둥근 상자 제거 — 아이콘은 제목 옆에 | Impeccable 「Icon tile stacked above heading」 | marketing.css | 대기 | | |
| R-014 | 한글 줄바꿈 기본값: 제목 `text-wrap: balance`, 본문 `pretty`, `word-break: keep-all`, `overflow-wrap: break-word` | orr.design 팁 5 · MDN | tokens.css | 대기 | | |
| R-015 | 읽기·누르기 바닥을 foundations 에: 글자 12px, 누르는 높이 40px, 본문 한 줄 46자 | Impeccable 품질 규칙 · 잰 값 | foundations.md, tokens.css | 대기 | | |
| R-016 | 밖으로 나가는 글 링크에만 ↗ (버튼·링크 끝의 → 는 쓰지 않음), `::selection` 을 강조색으로 | orr.design 팁 3·4 · frontend-design | tokens.css, foundations.md | 대기 | | |
| R-017 | 실제 화면을 재는 점검 도구(대비·글자·누르는 높이·줄 길이·제목 단계·넘침, 죽은 링크)를 본체로 | 리플로 저장소 `tools/site-build/ux_check.js` · `link_check.py` | 새 파일 | 대기 | | |
| R-018 | 새 부품 「허브」(찾기 + 갈래 칩 + 타일)를 marketing 패턴에 | refloworks 메인(11/26) | marketing.css, components.md | 대기 | | |
