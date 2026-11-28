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
| R-014 | 한글 줄바꿈 기본값: 제목 `text-wrap: balance`, 본문 `pretty`, `word-break: keep-all`, `overflow-wrap: break-word` | orr.design 팁 5 · MDN · [site-types](site-types.md) §1 한글 긴 글 타이포(같은 결론) | tokens.css | 대기 | | |
| R-015 | 읽기·누르기 바닥을 foundations 에: 글자 12px, 누르는 높이 40px, 본문 한 줄 46자 | Impeccable 품질 규칙 · 잰 값 · [site-types](site-types.md) §1 — 긴 글 본문은 한 줄 35~40자(36~40em) 제안, R-024와 함께 검토 | foundations.md, tokens.css | 대기 | | |
| R-016 | 밖으로 나가는 글 링크에만 ↗ (버튼·링크 끝의 → 는 쓰지 않음), `::selection` 을 강조색으로 | orr.design 팁 3·4 · frontend-design | tokens.css, foundations.md | 대기 | | |
| R-017 | 실제 화면을 재는 점검 도구(대비·글자·누르는 높이·줄 길이·제목 단계·넘침, 죽은 링크)를 본체로 | 리플로 저장소 `tools/site-build/ux_check.js` · `link_check.py` | 새 파일 | 대기 | | |
| R-018 | 새 부품 「허브」(찾기 + 갈래 칩 + 타일)를 marketing 패턴에 | refloworks 메인(11/26) | marketing.css, components.md | 대기 | | |
| R-019 | 기본 글꼴을 Noto Sans KR → Pretendard (SIL OFL 1.1). 사이트 사본에서 먼저 바꿈 | refloworks 11/28, 후보 다섯 비교 뒤 사용자 선택 | tokens.css, tokens.py, foundations.md, yeobaek.py | 대기 | | |
| R-020 | 새 부품: 모든 쪽 공통 위 메뉴·맨 아래(`.site-nav` `.site-foot`), 머리 옆 화면(`.ds-hub-split`), 진행 절차(`ol.ds-steps`) | refloworks 11/28 · [site-types](site-types.md) §2·§8 — 문서 Steps, 공공 단계 표시와 같은 부품 | marketing.css, components.md | 대기 | | |
| R-021 | **숫자·가격 표기 규칙** — 원·음수·퍼센트·만/억 줄임, 가격(할인율 → 최종가, 정가 취소선 + 읽어 줄 문구), 숫자는 tabular. 문서 규칙 + `.ds-price` | [site-types](site-types.md) §5·§10 · Baymard · HMRC | design-system.md, components.css, components.md | 대기 | | |
| R-022 | **금액 입력 · 결제 금액 요약** — 쉼표 실시간·"원"·한글 보조 표기 입력칸, 항목별 합계 + 버튼에 최종 금액 | §5·§6·§10 · [HMRC 금액 입력](https://design.tax.service.gov.uk/hmrc-design-patterns/currency-input) · TDS Keypad | components.css, components.md | 대기 | | |
| R-023 | **폼 흐름 패턴** — 오류 요약(맨 위, 칸으로 링크), 답변 확인(섹션별 "변경"), 완료 페이지(접수번호 + 다음 할 일), 동의(전체/개별·필수/선택). roadmap Patterns "폼 검증 흐름"을 이것으로 | §8 · [GOV.UK 패턴](https://design-system.service.gov.uk/patterns/) · KRDS 기본 패턴 | components.css, components.md, roadmap.md | 대기 | | |
| R-024 | **긴 글 본문 `.ds-prose`** — 본문 17px·행간 1.7·폭 36~40em, 제목 위 여백 > 아래, 인용·그림+캡션·각주·표 | §1 · [Primer Brand](https://primer.style/brand/) · toss.tech | tokens.css, components.css, components.md | 대기 | | |
| R-025 | **문서 부품** — 강조 박스(`.ds-banner` 문서용 변형), 코드 블록·한 줄 명령어 복사, 우측 목차(scroll-spy), 좌 메뉴 + 본문 + 목차 3단 레이아웃 | §2 · [Nextra](https://nextra.site/docs) · [Geist Snippet](https://vercel.com/geist/snippet) · Docusaurus | components.css, components.md | 대기 | | |
| R-026 | **수량·인원 스테퍼** (− / 숫자 / + + 직접 입력, 최소·최대) — ui-dictionary 입력 폼 백로그 "Number stepper"와 같음 | §5·§6 · Baymard 수량 UI · SEED quantity-picker | components.css, components.md | 대기 | | |
| R-027 | **기간 캘린더 · 시간 슬롯** — 예약 불가/마감은 숨기지 않고 비활성 + 글자, 키보드 이동. roadmap Phase 1 DatePicker 잔여분을 이것으로 | §6 · [W3C APG 날짜 선택](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/datepicker-dialog/) · Baymard · SEED | components.css, components.md, (JS) | 대기 | | |
| R-028 | **모바일 틀** — 상단 바, 하단 탭(5개 이하), 바텀시트(최대 90%·폭 480px·결제 폼은 닫기 버튼만), 하단 고정 버튼 + `env(safe-area-inset-*)` | §9 · [SEED](https://seed-design.io) · [TDS Mobile](https://tossmini-docs.toss.im/tds-mobile/) | components.css, components.md, foundations.md | 대기 | | |
| R-029 | **이미지 갤러리 · 라이트박스 · 캐러셀** (자동 회전 금지 또는 정지 버튼, ESC·방향키·포커스 가두기) | §3·§5 · [W3C 캐러셀](https://www.w3.org/WAI/tutorials/carousels/) | components.css, components.md | 대기 | | |
| R-030 | **평점·리뷰 요약** (평균 숫자 + 개수 + 분포 막대 — `.ds-bars` 재사용) | §4·§5 · Baymard | components.css, components.md | 대기 | | |
| R-031 | **소셜 부품** — 피드(`role="feed"`, 위치 복원, "더 보기"), 반응·팔로우 토글(`aria-pressed`), 댓글 스레드(1~2단계) | §7 · [W3C APG Feed](https://www.w3.org/WAI/ARIA/apg/patterns/feed/) · [NN/g](https://www.nngroup.com/articles/infinite-scrolling-tips/) · SEED | components.css, components.md | 대기 | | |
| R-032 | **건너뛰기 링크** `.ds-skip` 를 기본으로 + 접근성 점검표를 KWCAG 2.2 33개 항목에 맞춰 보기 | §8 · KRDS · USWDS | tokens.css(또는 components.css), foundations.md | 대기 | | |
| R-033 | **다크패턴 금지 명문화** — 전자상거래법 제21조의2 6유형(순차공개 가격·사전선택·잘못된 계층·취소 방해·숨은갱신·반복간섭)을 design-system.md 안티패턴에. 버튼 위계 대칭, 총액 먼저 | §5 · [뉴시스 Q&A](https://www.newsis.com/view/NISX20250213_0003063585) · ui-dictionary §9 | design-system.md | 대기 | | |
| R-034 | **커머스 법정 표시** — 사업자정보 푸터, 상품정보 고시 표 (쇼핑몰 만들 때) | §5 · [공정위 결정문](https://www.law.go.kr/LSW/ftcInfoP.do?ftcSeq=931) | marketing.css 또는 새 commerce 파일, components.md | 대기 | | |
