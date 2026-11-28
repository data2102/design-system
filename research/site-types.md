# 사이트 유형별 커버리지 조사

> **상태: 조사 자료 (검토 전).** 여백 DS 규칙이 아니다. 반영 여부는 [`review.md`](review.md)에서 정한다 (후보 R-021~R-034).

여백 DS가 지금 잘 다루는 건 **업무 도구 · 대시보드 · 랜딩**이다. 다른 종류의 사이트도 만들 수 있으려면 무엇이 더 필요한지, 유형별로 필요한 페이지와 부품, 참고할 디자인 시스템을 모았다.

- 조사일: 2026-11-28 · 방법: 유형별 웹 조사, 인용한 주소는 직접 열어 확인
- 열지 못한 곳은 **확인 못 함**으로 표시했다. 그런 곳에 적은 내용은 일반 지식이다(29CM·무신사·쿠팡·야놀자는 봇 차단, 요즘IT 405, 카카오뱅크 공개 DS 없음)
- Apple HIG · Material 3 문서는 본문을 못 읽었다. 44pt·48dp는 널리 알려진 값이고 원문은 대조하지 않았다

---

## 0. 한눈에 — 유형 × 여백 DS 상태

✅ 지금 부품으로 됨 · 🟡 일부 · ⬜ 핵심 부품 없음

| 사이트 유형 | 상태 | 가장 큰 빈칸 |
|---|---|---|
| 업무 도구 · 대시보드 · 모니터링 | ✅ | — |
| 랜딩 · 브랜드 | ✅ | (대기 후보 R-001~R-004, R-012, R-013, R-018, R-020) |
| 포트폴리오 · 개인 사이트 | 🟡 | 사례 연구 레이아웃, 갤러리·라이트박스, 타임라인 |
| 블로그 · 매거진 · 뉴스 | ⬜ | **긴 글 본문(Prose)**, 글 카드, 작성자 줄, 그림+캡션, 이전/다음 글 |
| 문서 · 가이드 · 헬프센터 | ⬜ | **3단 레이아웃(좌 메뉴·본문·우 목차)**, 강조 박스, 코드 블록 복사 |
| 교육 · 강의 | 🟡 | 강의 카드, 커리큘럼 아코디언(차시 상태), 진행률 + 이어 학습 |
| 쇼핑몰 · 커머스 | ⬜ | **가격 표기**, 옵션 선택, 수량 스테퍼, 이미지 갤러리, 평점, 결제 금액 요약, 법정 표시 |
| 예약 (숙소·식당·클래스·진료) | ⬜ | **기간 캘린더 · 시간 슬롯**, 인원 선택, 총액 펼침, 취소 정책 |
| 커뮤니티 · 소셜 | ⬜ | 피드, 반응·팔로우 토글, 댓글 스레드, 신고·차단 |
| 공공 · 기관 | 🟡 | 건너뛰기 링크, 공식 배너·식별자, **오류 요약·답변 확인·완료** 흐름, KWCAG 점검 |
| 모바일 우선 · 앱 같은 웹 | ⬜ | 상단 바, 하단 탭, **바텀시트**, 하단 고정 버튼 + safe area |
| 금융 · 핀테크 | 🟡 | **금액 입력·숫자 서식**, 계좌 선택, 거래내역, 송금 확인 |

**결론:** 유형마다 따로 만들 필요는 없다. 아래 **공통 부품 6묶음**을 채우면 대부분의 유형이 열린다(§13).

---

## 1. 블로그 · 매거진 · 뉴스 · 뉴스레터

**페이지:** 글 목록(추천 글 + 카드 격자) · 글 상세 · 태그/카테고리 · 연재(시리즈) · 작성자 · 검색 · 구독/아카이브

| 부품 | 하는 일 | 핵심 규칙 |
|---|---|---|
| Prose (긴 글 본문) | h2~h4, 문단, 목록, 인용, 표, 그림을 한 번에 꾸밈 | 폭 제한. 제목 위 여백 > 아래 여백 |
| 글 카드 | 썸네일·분류·제목·요약·작성자 | 제목 2줄, 요약 2~3줄에서 자름. 썸네일 없어도 안 깨지게 |
| 작성자 줄 (Byline) | 작성자 · 날짜 · 읽는 시간 | 제목 바로 아래 한 줄. 날짜 형식 통일 |
| 그림 + 캡션 | 이미지 설명·출처 | 캡션은 본문보다 작게. 이미지는 본문보다 넓게 펼칠 수 있게 |
| 인용 / 큰 인용 | 인용·강조 | 남발 금지 |
| 각주 | 근거 | 본문 위첨자 ↔ 글 끝 목록 양방향 링크 |
| 연재 표시 · 이전/다음 글 | 이어 읽기 | "3/8" 표기 |
| 관련 글 · 구독 CTA | 다음 행동 | 글 끝에 관련 글 3개, 이메일 입력 하나 |

**참고:** [toss.tech](https://toss.tech)(분야 탭, 연재 카드, 인기 순위) · [브런치](https://brunch.co.kr)(브런치북 묶음, 작가 카드) · [카카오 기술블로그](https://tech.kakao.com/blog)(태그 구조) · [Primer Brand](https://primer.style/brand/)(Prose·Footnotes 구현)

### 한글 긴 글 타이포 (시작값)

| 항목 | 시작값 | 근거 |
|---|---|---|
| 본문 크기 | 데스크톱 17~18px, 모바일 16~17px | 연구 수치 **확인 못 함**. toss.tech CSS에 15·17·20px 많음(추론) |
| 행간 | 본문 1.6~1.8, 제목 1.25~1.35 | 한글은 빽빽해 보여 영문보다 넓게(블로그 권장 요약) |
| 한 줄 길이 | 약 35~40자 → `max-width: 36~40em` | 영문 45~90자([Practical Typography](https://practicaltypography.com/line-length.html)), 동아시아 문자는 그 절반. 한글 실증 수치 **확인 못 함** |
| 줄바꿈 | 본문 `word-break: keep-all; overflow-wrap: break-word; text-wrap: pretty` · 제목 `text-wrap: balance` | [daleseo.com](https://daleseo.com/css-text-wrap/) · [W3C klreq](https://www.w3.org/TR/klreq/) → 대기 후보 **R-014와 같은 내용** |
| 정렬 | 본문 왼쪽 정렬 (양쪽 정렬 + keep-all은 간격이 벌어짐) | CSSWG 이슈 #4285(요약만, 원문 못 엶) |

---

## 2. 문서 · 가이드 · 헬프센터

**페이지:** 문서 홈(제품 카드 + 빠른 시작 + 검색) · 문서 상세(**좌 메뉴 / 본문 / 우 목차** 3단) · 검색(⌘K) · 단계 가이드 · FAQ · 변경 내역 · 404

| 부품 | 핵심 규칙 |
|---|---|
| 좌측 메뉴 | 현재 위치 강조, 접기, 모바일은 서랍 |
| 우측 목차 (TOC) | 고정, 읽는 중인 섹션 강조(scroll-spy), h2~h3만 |
| 제목 앵커 | hover 시 #, 누르면 주소 복사 |
| 강조 박스 (Callout) | note·tip·warning·danger 정도로 종류 제한. 색 + 아이콘 |
| 코드 블록 · 명령어 한 줄 | 언어 표시, 복사 버튼, `$`는 복사 안 되게, 복사 후 체크 |
| 탭(언어·OS별) | 고른 탭 기억 |
| 단계 (Steps) | 번호, 단계마다 할 일 하나 |
| 이전/다음 · "도움이 됐나요?" | 메뉴 순서대로, 응답 후 감사 문구 |

**참고:** [Docusaurus 강조 박스](https://docusaurus.io/docs/markdown-features/admonitions) · [Mintlify Callouts](https://mintlify.com/docs/components/callouts) · [Nextra](https://nextra.site/docs)(문서용 최소 세트) · [Vercel Geist Snippet](https://vercel.com/geist/snippet)(인라인 코드/한 줄/블록 3단계) · [Stripe Docs](https://docs.stripe.com)(문서 홈) · [GOV.UK Step by step](https://design-system.service.gov.uk/patterns/step-by-step-navigation/)

> 여백과의 관계: 강조 박스는 지금 `.ds-banner-*` 4종과 거의 같다 → 새 부품보다 **배너의 문서용 변형**으로 가는 게 맞아 보임.

---

## 3. 포트폴리오 · 브랜드 쇼케이스 · 개인 사이트

**페이지:** 소개(히어로 + 대표 작업) · 작업 목록(필터 + 격자) · 작업 상세(사례 연구) · 이력 · 연락

| 부품 | 핵심 규칙 |
|---|---|
| 작업 카드 | 이미지 비율 통일(예: 4:3) |
| 사례 연구 레이아웃 | 문제 → 과정 → 결과. 위에 역할·기간·팀·도구 요약표, 성과는 큰 숫자(`ds-stat` 재사용) |
| 지그재그 섹션 · 벤토 격자 | 모바일은 세로로 쌓기. 셀 크기 2~3종만 |
| 갤러리 · 라이트박스 | ESC 닫기, 방향키, 포커스 가두기, 캡션 유지 |
| 영상 틀 | 포스터 이미지, 자동재생은 음소거일 때만, 자막 |
| 타임라인 · 추천사 | 최신순 / 실명·소속 |

**참고:** [Primer Brand](https://primer.style/brand/) — River, Bento, Timeline, Testimonial, Statistic, Video player, Prose가 다 있어 목록을 거의 그대로 참고 가능. 국내 사례 **확인 못 함**.

---

## 4. 교육 · 강의

**페이지:** 강의 목록 · 강의 상세(소개/커리큘럼/강사/후기/가격) · 수강 화면(영상 + 목차) · 내 학습 · 수료증 · 결제

| 부품 | 핵심 규칙 |
|---|---|
| 강의 카드 | 제목·강사·난이도·평점(개수)·수강생 수·가격/할인·배지 |
| 커리큘럼 아코디언 | 섹션마다 차시 수·총 시간·미리보기, 모두 펼치기 (`ds-accordion` 확장) |
| 진행률 · 이어 학습 | "12강 중 5강", 이어서 학습 버튼 (`ds-progress` 재사용) |
| 차시 상태 | 완료 / 진행 중 / 잠김 — 색 + 아이콘 |
| 가격 박스 | 데스크톱은 따라다니는 사이드 카드, 정가 취소선 + 할인율 (§5 가격 표기와 같음) |

**참고:** [인프런](https://www.inflearn.com)(카드 정보 구성, 무료/할인 토글) · [패스트캠퍼스](https://fastcampus.co.kr)(수강 조건 표기: 평생소장·사전지식) · [GOV.UK 컴포넌트](https://design-system.service.gov.uk/components/)(Task list)

---

## 5. 쇼핑몰 · 커머스

**페이지:** 홈(기획전) → 목록·검색 → 상품 상세 → 장바구니 → 주문서·결제 → 주문 완료 → 주문·배송 조회 / 취소·반품 → 찜·리뷰

| 부품 | 핵심 규칙 |
|---|---|
| 상품 카드 · 가격 표기 | 할인율 → 최종가 순서. 정가 취소선엔 읽어 줄 문구("정가 ○원"). 숫자는 tabular |
| 필터·정렬 바 | 적용된 필터를 항상 보여 주고 하나씩 해제. 결과 개수 표시 (`yb-filterbar` 확장) |
| 상품 이미지 갤러리 | 썸네일로 추가 이미지. 자동 회전은 금지하거나 정지 버튼 |
| 옵션 선택기 | 품절은 숨기지 말고 비활성 + "품절" 글자. 고른 조합 요약 |
| 수량 스테퍼 | − / 숫자 / + 와 직접 입력 함께, 최소·최대 |
| 결제 금액 요약 | 필수 비용은 총액에 포함. 버튼에 금액("23,900원 결제하기") |
| 평점·리뷰 | 별만 말고 숫자도("4.6점, 리뷰 1,203개"), 분포 막대 (`ds-bars` 재사용) |
| 도착 예정일 | 배송 속도 대신 **도착 날짜**, 주문 마감 카운트다운 |
| 단계형 주문서 | 비회원 구매 허용, 가입은 구매 후. 끝난 단계는 접기 |

**참고:** [Baymard 상품 상세](https://baymard.com/research/product-page) · [Baymard 체크아웃](https://baymard.com/research-articles/current-state-of-checkout-ux) · [Baymard 상품 목록](https://baymard.com/research/ecommerce-product-lists) · [Shopify Dawn](https://themes.shopify.com/themes/dawn) · [Shopify 테마 접근성](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility) · 29CM·무신사·쿠팡 **확인 못 함**(봇 차단)

### 법·신뢰 (한국)
- **사업자정보 표시** (전자상거래법 제10조, 시행규칙 제7조): 상호·대표자·주소·전화·이메일·사업자등록번호·약관·호스팅 사업자를 초기 화면에. 통신판매업 신고번호는 실무상 함께 표시(조문 위치 **확인 못 함**). 출처: [공정위 결정문](https://www.law.go.kr/LSW/ftcInfoP.do?ftcSeq=931)
- **상품정보제공고시**: 품목별 필수 정보 + 거래 조건 → 상품 상세에 "상품정보 고시" 표 필요
- **다크패턴 6유형 금지** (개정 전자상거래법 제21조의2, 2025-02-14 시행): 순차공개 가격책정 · 특정옵션 사전선택 · 잘못된 계층구조 · 취소·탈퇴 방해 · 숨은갱신 · 반복간섭. 과태료 1차 100만 ~ 3차 500만 원([뉴시스](https://www.newsis.com/view/NISX20250213_0003063585)). → [ui-dictionary.md §9 다크 패턴](../ui-dictionary.md)과 연결

---

## 6. 예약 (숙소 · 식당 · 클래스 · 진료)

**페이지:** 검색(장소·날짜·인원) → 결과 목록 + 지도 → 상세(객실·코스·시간) → 요청사항 → 결제·예약금 → 예약 확인 → 내 예약(변경·취소) → 후기

| 부품 | 핵심 규칙 |
|---|---|
| 통합 검색 바 | 장소·날짜·인원 한 줄, 첫 화면에 |
| 기간 캘린더 | 날짜별 최저가, 예약 불가 날짜 확실히 구분, 키보드로 날짜 이동 |
| 시간 슬롯 격자 | 마감 슬롯은 숨기지 말고 비활성 + "마감". 잔여석. 점심/저녁 묶음 |
| 인원 선택 | 성인·아동·유아별 스테퍼(§5 수량 스테퍼 재사용) |
| 지도 ↔ 목록 | 핀에 가격, 목록과 동기화 |
| 요금 펼침 · 취소 정책 | 1박 × 박수 + 세금·수수료. "12월 3일 23:59까지 무료 취소"처럼 **절대 날짜** |
| 예약 확인 카드 | 예약번호·QR·일정·주소·캘린더 추가. 변경·취소는 같은 위계 |

**참고:** [Baymard 숙박 UX](https://baymard.com/research-articles/new-research-travel-accommodations) · [Baymard 날짜 선택 예시](https://baymard.com/ecommerce-design-examples/date-picker) · [Material 3 Date pickers](https://m3.material.io/components/date-pickers) · [SEED date-picker](https://seed-design.io/components/date-picker) · [W3C APG 날짜 선택 대화상자](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/datepicker-dialog/) · [Airbnb](https://www.airbnb.co.kr) · [캐치테이블](https://app.catchtable.co.kr)

---

## 7. 커뮤니티 · 소셜 · UGC

**페이지:** 피드 → 글 상세 + 댓글 → 글쓰기 → 프로필 → 알림 → 검색 → 신고·차단·설정

| 부품 | 핵심 규칙 |
|---|---|
| 무한 피드 | 뒤로가기 시 위치 복원, 푸터 닿게 "더 보기". 검색 결과엔 쓰지 않음([NN/g](https://www.nngroup.com/articles/infinite-scrolling-tips/)). `role="feed"`([W3C APG](https://www.w3.org/WAI/ARIA/apg/patterns/feed/)) |
| 글 카드 | "3분 전" + 절대 시간(툴팁/datetime) |
| 반응 · 팔로우 토글 | `aria-pressed`, 숫자 즉시 반영 후 실패 시 되돌림 |
| 댓글 스레드 | 들여쓰기 1~2단계, 삭제된 댓글은 자리 남김 |
| 이미지 업로더 | 진행률, 대체 텍스트 입력받기 |
| 작성기 | 임시저장, 이탈 경고 |
| 더보기 메뉴 | 신고(사유 선택)·차단·숨기기·공유 |
| 알림 · 숫자 뱃지 | 99+ 상한 (ui-dictionary 백로그와 같음) |

**참고:** [SEED Design 컴포넌트](https://seed-design.io/components)(reaction-button, manner-temp, image-frame, menu-sheet …) · [W3C 캐러셀 튜토리얼](https://www.w3.org/WAI/tutorials/carousels/) · [당근](https://www.daangn.com)

---

## 8. 공공 · 기관

- **KRDS**(범정부 디자인 시스템): 컴포넌트 약 55개 / 11분류, 기본 패턴 12개 + 서비스 패턴 5개(방문·검색·로그인·신청·정책 정보). KWCAG 2.2(원칙 4·지침 14·**검사항목 33**) + 전자정부 누리집 품질관리 지침 + WCAG 2.1 준수
- 의무는 **접근성 준수**(장애인차별금지법 등). 품질인증 마크 취득 의무 근거는 못 찾음 — 발주 조건으로 요구될 수 있음

| 부품 | 핵심 규칙 |
|---|---|
| 건너뛰기 링크 (Skip link) | 첫 포커스 요소 — **모든 사이트에 필요** |
| 공식 배너 · 운영기관 식별자 | 맨 위 / 푸터. 공식 도메인일 때만, 문구 고정 |
| 단계 표시 | 3단계 이상일 때만, 현재 단계 `aria-current` (`ds-stepper` 보강) |
| **오류 요약** | 제출 오류를 맨 위에 모으고 포커스 이동, 각 항목은 해당 칸으로 링크, 제목 앞 "오류:" |
| **답변 확인** | 제출 전 검토, 섹션마다 "변경", 고친 뒤 바로 복귀 |
| **완료 페이지** | 접수번호 + 다음 할 일 |
| 동의(약관) | 전체/개별, 필수/선택 구분, 요약 + 펼침 |
| 글자 크기 · 긴급 공지 띠 | 설정 / 헤더 위 띠 |

**참고:** [KRDS](https://www.krds.go.kr/html/site/index.html) · [KRDS 컴포넌트](https://www.krds.go.kr/html/site/component/component_summary.html) · [KRDS 패턴](https://www.krds.go.kr/html/site/global/global_summary.html) · [GOV.UK 패턴](https://design-system.service.gov.uk/patterns/) · [USWDS](https://designsystem.digital.gov/components/overview/) · [웹접근성 품질마크 안내(문체부)](https://www.mcst.go.kr/kor/s_etc/webAccess/accessibility.jsp)

---

## 9. 모바일 우선 · 앱 같은 웹

| 부품 | 핵심 규칙 |
|---|---|
| 상단 바 | 뒤로가기 왼쪽, 스크롤 시 축소/구분선 |
| 하단 탭 | 5개 이하, 이동 전용(행동 X), 아이콘 + 라벨 |
| **바텀시트** | 최대 높이 90%, 넘치면 페이지로. 결제·복잡한 폼은 핸들 없이 닫기 버튼만(실수로 안 닫히게). 최대 폭 480px (SEED) |
| 하단 고정 버튼 | safe area 더하기, 키보드 열리면 따라 올라감 |
| Safe area | `env(safe-area-inset-*)` |
| 터치 영역 | 최저 24×24px(WCAG 2.2 SC 2.5.8), 권장 44px — 여백 foundations는 이미 44px |
| 휠 선택 · 수량 선택 | SEED·KRDS 모바일 분류 |

**참고:** [SEED Design](https://seed-design.io)(한국어 모바일 웹 54종) · [TDS Mobile](https://tossmini-docs.toss.im/tds-mobile/)(ListRow·BottomSheet·Keypad — **여백과 결이 가장 가까움**) · [Apple HIG 탭바](https://developer.apple.com/design/human-interface-guidelines/tab-bars) · [Material 3 바텀시트](https://m3.material.io/components/bottom-sheets/guidelines)

---

## 10. 금융 · 핀테크

| 부품 | 핵심 규칙 |
|---|---|
| **금액 입력** | 천 단위 쉼표 실시간, "원" 접미사, 아래에 "12만 3,000원" 보조 표기(관행, 공식 근거 **확인 못 함**), `inputmode="numeric"` ([HMRC 금액 입력](https://design.tax.service.gov.uk/hmrc-design-patterns/currency-input)) |
| 빠른 금액 칩 | +1만 · +10만 · 전액, 잔액 초과 경고 (`ds-chip` 재사용) |
| 계좌·카드 선택 | 은행 아이콘, 끝 4자리, 잔액 — 바텀시트 안 라디오 목록 |
| 거래내역 | 날짜별 묶음, 입출금은 **색 + 부호**, 숫자 tabular 오른쪽 정렬 |
| 송금 확인 | 받는 사람 실명·금액·수수료 크게, 버튼 "○○원 보내기" |
| 숫자 서식 규칙 | 원·음수·퍼센트·만/억 줄임을 문서로 |
| 신뢰 신호 | 예금자보호 안내, 마지막 로그인, 자동 로그아웃 예고 |

**참고:** [TDS Mobile](https://tossmini-docs.toss.im/tds-mobile/) · [Wise Design](https://wise.design) · [Monzo 글쓰기 시스템](https://monzo.com/blog/weve-made-our-writing-system-available-to-all) · 카카오뱅크 공개 DS **확인 못 함**

---

## 11. 1차 레퍼런스 (여러 유형을 함께 볼 때)

| 디자인 시스템 | 잘 맞는 유형 |
|---|---|
| [TDS Mobile](https://tossmini-docs.toss.im/tds-mobile/) | 금융 · 모바일 — 여백의 뿌리(토스류)와 같은 결 |
| [SEED Design](https://seed-design.io) | 모바일 · 커뮤니티 · 중고거래/커머스 (한국어) |
| [KRDS](https://www.krds.go.kr) | 공공 · 한국어 폼 · KWCAG |
| [GOV.UK Design System](https://design-system.service.gov.uk) | 폼 흐름(질문 한 페이지에 하나, 오류 요약, 답변 확인) |
| [USWDS](https://designsystem.digital.gov) | 기관 식별, 단계·절차 |
| [Primer Brand](https://primer.style/brand/) | 콘텐츠 · 브랜드 쇼케이스 |
| [Nextra](https://nextra.site/docs) · [Vercel Geist](https://vercel.com/geist/snippet) | 문서 |
| [Baymard Institute](https://baymard.com) | 커머스 · 예약 UX 근거 |
| [Material 3](https://m3.material.io) · [Apple HIG](https://developer.apple.com/design/human-interface-guidelines) | 모바일 동작·상태 정의 |

**여러 DS를 한꺼번에 비교하는 곳**
- [Component Gallery](https://component.gallery) — 컴포넌트 60종 × DS 95개 예시. 부품 이름 정할 때 가장 유용 (한국 DS는 없음)
- [Design Systems Surf](https://designsystems.surf) — 컴포넌트·파운데이션 출처 비교(일부 유료)
- [Design Systems Repo](https://designsystemsrepo.com/design-systems/) — DS 목록

---

## 12. 이미 있는 것 재사용

새로 만들기 전에 기존 부품을 넓히면 되는 것들:

| 필요한 것 | 넓힐 기존 부품 |
|---|---|
| 강조 박스(Callout) | `.ds-banner-*` |
| 평점 분포 | `.ds-bars` |
| 진행률 · 이어 학습 | `.ds-progress` |
| 커리큘럼 | `.ds-accordion` |
| 단계 표시(공공) | `.ds-stepper` (+ `aria-current`) |
| 사례 연구 성과 숫자 | `.ds-stat` / `.yb-kpi` |
| 필터 요약·해제 | `.yb-filterbar` + `.ds-chip` |
| 빠른 금액 칩 | `.ds-chip` |
| 데스크톱의 바텀시트 대안 | `.ds-popover` / `.ds-modal` |

---

## 13. 공통 부품 6묶음 (우선순위)

여러 유형에 동시에 쓰이는 것부터. 묶음마다 review.md 후보 번호를 달았다.

1. **숫자·가격 표기** (커머스·예약·교육·금융) — 가격(할인율·취소선·최종가), 금액 입력, 원·만·억 서식, 결제 금액 요약 → R-021, R-022
2. **폼 흐름** (공공·금융·커머스·예약) — 오류 요약, 답변 확인, 완료 페이지, 동의 패턴 → R-023
3. **긴 글 · 문서** (블로그·문서·교육·포트폴리오) — Prose, 강조 박스, 코드 블록, 우 목차, 3단 레이아웃 → R-024, R-025
4. **선택 입력** (커머스·예약·모바일) — 수량/인원 스테퍼, 기간 캘린더, 시간 슬롯 → R-026, R-027
5. **모바일 틀** (모바일·커머스·커뮤니티·금융) — 상단 바, 하단 탭, 바텀시트, 하단 고정 버튼 → R-028
6. **미디어 · 소셜** (커머스·포트폴리오·커뮤니티) — 갤러리·라이트박스, 평점, 피드·반응·댓글 → R-029, R-030, R-031

규칙 쪽: 건너뛰기 링크(R-032), 다크패턴 금지 명문화(R-033), 커머스 법정 표시(R-034).
