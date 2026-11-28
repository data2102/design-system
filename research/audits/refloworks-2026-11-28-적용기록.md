# refloworks.com — 사본에 먼저 적용한 것 (2026-11-26 ~ 11-28)

> **상태: 조사 기록 (검토 전).** 여백 DS 본체는 바꾸지 않았다. 반영 여부는 [`../review.md`](../review.md) 에서 정한다.
> refloworks.com 은 여백 DS의 `tokens.css` · `marketing.css` 를 **복사해서** 쓴다(리플로 작업 저장소의 `docs/사이트/`). 아래는 그 사본에서 먼저 바꾼 것이다. 지금 본체와 사본이 다르다.

## 왜 기록하나

사이트를 고치면서 본체와 다른 값이 생겼다. 그대로 두면 「여백 디자인 시스템으로 만들어 줘」 했을 때 사이트와 다른 모양이 나온다. 무엇이 달라졌는지 적어 두고, 본체로 가져올지는 검토에서 정한다.

## 재서 확인한 것 (주요 8~9쪽, PC 1280 · 휴대폰 390)

| 무엇 | 고치기 전 | 고친 뒤 | 기준 |
|---|---|---|---|
| 회색 안내 글 `--text-tertiary` on 흰 바탕 | 3.0 : 1 (#8b95a1) | 5.5 : 1 (#5f6a78) | 4.5 |
| 알약 버튼 흰 글자 on `--accent` | 3.7 : 1 | 5.7 : 1 (`--accent-strong` 바탕) | 4.5 |
| 주황 글자·꼬리표 `--warm` | 3.1 ~ 3.6 : 1 (#c96f4c) | 5.4 : 1 (#a8522f) | 4.5 |
| 가장 작은 글자 | 10 ~ 11px | 12px | — |
| 휴대폰에서 누르는 것의 높이 | 19 ~ 30px | 40px 넘게 | — |
| 본문 한 줄 | 한글 70 ~ 95자 | 46자 안팎 (`max-width: 46em`) | — |

본체의 `a11y_check.py` 는 `text-tertiary/surface` 를 UI 기준 3 : 1 로 본다. 그런데 사이트에서는 이 색을 안내 **문장**(맨 아래 글, 파일 안내)에 쓰고 있어서 본문 기준 4.5 가 맞았다.

## 사본에서 바꾼 것

**tokens.css**
- `--text-tertiary` #8b95a1 → #5f6a78, `--warm` #c96f4c → #a8522f
- 제목 `text-wrap: balance`, 본문 `text-wrap: pretty`, 둘 다 `word-break: keep-all`
- `::selection` 을 `--accent-strong` 바탕 + 흰 글자, `body { overflow-wrap: break-word }`
- 밖으로 나가는 글 링크(`a[target="_blank"]`)에 ↗ 가 저절로 붙음 (타일·카드·버튼 제외)
- 휴대폰에서 메뉴 링크·칩의 `min-height: 40px`, 안내 줄의 `max-width: 46em`

**marketing.css**
- `.ds-btn-pill.primary`: 색 그림자 제거, 바탕 `--accent` → `--accent-strong`, hover 는 `--accent-pressed`
- `.ds-hero-wrap`, `.ds-cta-band`: 틴트 그라디언트 → 단색
- `.ds-hero h1 .accent`: 한 구절만 파랗게 칠하던 것을 제목과 같은 색으로
- `.ds-hero .eyebrow`: 알약 → 글씨만
- `.ds-feature-ico`: 제목 위 둥근 상자 → 상자 없이 제목 옆
- 카드 hover 의 떠오름(`translateY`) 제거, 테두리 색만
- 새 부품 「허브」: `.ds-hub` `.ds-search` `.ds-chip` `.ds-tile` (찾기 + 갈래 칩 + 타일)

**마크업 관습**
- 버튼·링크 글 끝의 「→」 를 뺌 (메뉴 경로 안내 「설정 → 기능」 은 둠)
- 위 메뉴와 겹치는 제목 위 꼬리표를 뺌. 정보가 있는 것(「체험판 · 예시 데이터」)만 남김
- 같은 일을 하는 버튼은 어디서나 같은 이름

## 재는 도구 (리플로 작업 저장소에 있음)

- `tools/site-build/ux_check.js` — 대비 · 글자 크기 · 누르는 높이 · 줄 길이 · 제목 단계 · 가로 넘침 · 오류
- `tools/site-build/link_check.py` — 안쪽 링크가 죽지 않았는지

본체의 `a11y_check.py` 가 토큰 쌍만 본다면, 이 둘은 **실제 화면에서** 잰다. 본체로 옮길 만하다(R-017).

## 읽은 자료

- Anthropic `frontend-design` 스킬 (Apache-2.0) — github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design
- Impeccable 규칙 목록 (Paul Bakaus, Apache-2.0) — impeccable.style/anti-patterns · 검사기는 실행 파일을 내려받는 구조라 돌리지 않음
- unslop (Damir Sokolovsky, CC BY 4.0) — github.com/heydamir/unslop
- orr.design 노션 「AI가 만든 홈페이지, 디자이너가 만든 것처럼 바꾸는 작은 팁」
- UI UX Pro Max (MIT) — 디자인 시스템을 새로 정해 주는 도구라 쓰지 않음

## 사이트에 남은 것 (11/28)

휴대폰에서 누르기 작은 링크 4곳, 한 줄이 조금 긴 곳 3곳. 점검 결과는 refloworks.com/log 에 공개.
