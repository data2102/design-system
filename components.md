# 컴포넌트 문서

`components.css`에 구현된 컴포넌트의 사용법. (로드 순서: `tokens.css` → `components.css`)
각 컴포넌트는 **해부 → variants → states → 접근성 → 마이크로카피** 틀로 문서화한다.

---

## Phase 1 — 폼 · 입력

### 공통: 폼 필드 레이아웃

모든 입력은 `.ds-field`로 감싼다. 라벨은 **위**, 도움말/에러는 **아래**.

```html
<div class="ds-field">
  <label class="ds-label" for="org">발주기관<span class="ds-req">*</span></label>
  <input class="ds-input" id="org" type="text" placeholder="예: 조달청">
  <span class="ds-help">공고에 표기된 기관명을 그대로 입력하세요.</span>
  <span class="ds-error">기관명을 입력해 주세요.</span>
</div>
```

- **해부**: `ds-label`(라벨) · `ds-req`(필수 표시 `*`) · 입력요소 · `ds-help`(도움말) · `ds-error`(에러).
- **에러 노출**: 필드에 `.is-error` 클래스를 붙이면 `ds-help`가 숨고 `ds-error`가 나타난다.
- **접근성**: `label[for]` ↔ `input[id]` 연결 필수. 에러 시 입력에 `aria-invalid="true"` 권장.

### TextInput / Textarea

```html
<input class="ds-input" type="text" placeholder="도로 유지관리 용역">
<textarea class="ds-textarea" placeholder="메모를 남겨보세요"></textarea>
```

- **states**: 기본 / hover(테두리 진해짐) / focus(파란 테두리 + 링) / disabled(회색, `disabled` 속성) / error(`.is-error` 필드 안에서 빨간 테두리·빨간 링).
- 높이 48px, radius 12 — 넉넉한 터치 영역(원칙 ⑤ 여백).

### Select

```html
<div class="ds-select">
  <select><option>전체</option><option>용역</option><option>공사</option></select>
</div>
```
- 반드시 `.ds-select` 래퍼로 감싼다 (chevron 아이콘이 래퍼에서 나옴).

### Search

```html
<div class="ds-search">
  <input class="ds-input" type="search" placeholder="공고명·기관 검색">
</div>
```
- 래퍼 `.ds-search`가 왼쪽 돋보기 아이콘을 넣는다.

### Checkbox / Radio

```html
<label class="ds-check"><input type="checkbox" checked><span class="box"></span> 마감 임박만</label>
<label class="ds-radio"><input type="radio" name="cat"><span class="box"></span> 용역</label>
```
- **해부**: 시각적으로 숨긴 진짜 `<input>`(키보드·스크린리더용) + `.box`(보이는 체크박스).
- **states**: hover / checked(파란 배경 + 체크) / focus-visible(포커스 링) / disabled.
- **접근성**: 진짜 input을 쓰므로 키보드·AT 기본 동작 보장. 라벨 텍스트가 곧 접근성 이름.

### Switch (토글)

```html
<label class="ds-switch"><input type="checkbox" checked><span class="track"></span> 실시간 알림</label>
```
- on일 때 액센트색 트랙 + 노브 이동. 즉시 적용되는 설정에 사용(저장 버튼 필요한 값엔 체크박스).

### 마이크로카피 (폼)

- 라벨: 명사, 짧게. "발주기관" (○) / "기관명을 입력하세요" (✕ — 그건 placeholder)
- placeholder: 실제 예시. "예: 조달청" · "도로 유지관리 용역"
- 에러: 무엇을 어떻게. "기관명을 입력해 주세요." — "필수 항목입니다"보다 구체적으로.
- 도움말: 왜/어떻게만 짧게. 당연한 말 반복 금지.

### DatePicker (날짜 입력)

```html
<input class="ds-input" type="date">
```
- 네이티브 date input을 그대로 쓰되 `.ds-input` 스타일 적용(높이·테두리·포커스 통일). 달력 아이콘만 톤 조정.

### 다크 모드

모든 폼 요소는 토큰을 쓰므로, 상위에 `.theme-dark`만 붙이면 그대로 다크로 전환된다.

---

## Phase 2 — 피드백 · 오버레이

### Banner / Alert (인라인 상태 메시지)

```html
<div class="ds-banner ds-banner-warning">
  <svg class="ico">…경고 아이콘…</svg>
  <div>마감이 2일 남았어요. 서류를 확인하세요.</div>
</div>
```
- variants: `-info` `-success` `-warning` `-danger`. 배경은 은은한 틴트, 본문은 기본색, 아이콘만 역할색.
- 페이지에 붙박이로 뜨는 상태 안내에. (일시적 알림은 Toast)

### Toast (자동 사라짐 알림)

```html
<div class="ds-toast-wrap">
  <div class="ds-toast"><span class="dot"></span>저장했어요</div>
</div>
```
- 어두운 pill(역전색), 화면 하단 중앙. variants: 기본(성공) / `.is-warning` / `.is-danger`.
- **접근성**: 컨테이너에 `role="status" aria-live="polite"`. 3~4초 후 JS로 제거.
- 작업 결과 피드백에("저장했어요", "등록했어요"). 되돌리기 버튼을 함께 두면 좋음.

### Modal / Dialog

```html
<div class="ds-overlay">
  <div class="ds-modal" role="dialog" aria-modal="true" aria-labelledby="m-t">
    <h3 id="m-t">이 공고를 삭제할까요?</h3>
    <p>삭제하면 되돌릴 수 없어요.</p>
    <div class="ds-modal-actions">
      <button class="ds-btn ds-btn-secondary">취소</button>
      <button class="ds-btn ds-btn-primary">삭제하기</button>
    </div>
  </div>
</div>
```
- **접근성**: `role="dialog" aria-modal`, ESC 닫기, 포커스 트랩, 닫으면 열기 전 요소로 포커스 복귀.
- 중요한 확인/검토에만. 남발하면 흐름을 끊음.

### Tooltip

```html
<button class="ds-tip" data-tip="나라장터 기준 D-day">마감 ⓘ</button>
```
- hover·focus 시 위쪽에 표시. 짧은 보조 설명만(중요 정보는 툴팁에 숨기지 말 것).

### Loading — spinner / skeleton / progress

```html
<span class="ds-spinner"></span>
<div class="ds-skeleton" style="height:16px; width:70%"></div>
<div class="ds-progress"><div class="bar" style="width:60%"></div></div>
```
- 짧은 대기 = spinner, 콘텐츠 로딩 = skeleton(레이아웃 유지), 진행률 = progress.
- 모두 `prefers-reduced-motion`에서 멈춤.

### EmptyState (빈 화면)

```html
<div class="ds-empty">
  <svg class="ico">…</svg>
  <h3>아직 등록한 공고가 없어요</h3>
  <p>관심 있는 공고를 등록하면 마감 전에 알려드릴게요.</p>
  <button class="ds-btn ds-btn-primary">공고 등록하기</button>
</div>
```
- 사과 말고 초대. 제목은 공간을 명명, 본문 한 줄, CTA는 동사. "데이터 없음" 금지.

---

## Phase 3 — 데이터 · 탐색

### Table

```html
<table class="ds-table hover">
  <thead><tr><th>공고명</th><th class="num sortable">기초금액 <span class="sort-ind">▾</span></th><th class="num">마감</th></tr></thead>
  <tbody>
    <tr><td>도로 유지관리 용역</td><td class="num">4.2억</td><td class="num">D-2</td></tr>
  </tbody>
</table>
```
- `.hover`(행 hover), `.sticky`(헤더 고정) 옵션. 숫자 열엔 `.num`(우측 정렬+tabular).
- 정렬 헤더엔 `.sortable` + `.sort-ind`(방향 표시). 정렬 로직은 JS.
- 열이 많으면 래퍼에 `overflow-x:auto`.

### Tabs

```html
<div class="ds-tabs" role="tablist">
  <button class="ds-tab on" role="tab" aria-selected="true">전체</button>
  <button class="ds-tab" role="tab">진행중</button>
</div>
```
- 밑줄 스타일, 활성 탭만 액센트. `role="tablist"/"tab"`, 패널은 `role="tabpanel"`.

### Pagination

```html
<div class="ds-pagination">
  <button class="ds-page-btn" disabled>‹</button>
  <button class="ds-page-btn on">1</button><button class="ds-page-btn">2</button>
  <button class="ds-page-btn">›</button>
</div>
```

### Breadcrumb

```html
<nav class="ds-breadcrumb" aria-label="위치">
  <a href="#">홈</a><span class="sep">/</span><a href="#">입찰</a><span class="sep">/</span><span class="cur">상세</span>
</nav>
```

### Nav (사이드바)

```html
<nav class="ds-nav">
  <a class="ds-nav-item on"><svg class="ico">…</svg> 대시보드</a>
  <a class="ds-nav-item"><svg class="ico">…</svg> 공고 목록</a>
</nav>
```
- 활성 항목만 `.on`(연한 액센트 배경). 아이콘+라벨.

### Chip / Filter

```html
<button class="ds-chip on">전체</button>
<button class="ds-chip">용역</button>
```
- 선택형 필터. 활성만 액센트 배경. (배지 `ds-badge`는 상태 표시용 — 클릭 X, chip은 클릭 O)

### Accordion

```html
<div class="ds-accordion">
  <details open><summary>입찰 자격이 어떻게 되나요?</summary><div class="body">…</div></details>
  <details><summary>마감은 언제인가요?</summary><div class="body">…</div></details>
</div>
```
- 네이티브 `details/summary` 기반 → 키보드·스크린리더 기본 지원. chevron은 열림 시 회전.

### Avatar

```html
<span class="ds-avatar">소</span>
<span class="ds-avatar lg"><img src="…" alt="소농민"></span>
```
- 이니셜 또는 이미지. 크기 `.sm`(28) / 기본(40) / `.lg`(56).

### Stepper

```html
<div class="ds-stepper">
  <div class="ds-step done"><span class="dot">✓</span> 공고 확인</div>
  <div class="ds-step-line done"></div>
  <div class="ds-step cur"><span class="dot">2</span> 서류 준비</div>
  <div class="ds-step-line"></div>
  <div class="ds-step"><span class="dot">3</span> 제출</div>
</div>
```
- states: `.done`(완료·액센트) / `.cur`(현재) / 기본(예정). 연결선도 `.done`으로 채움.

### Popover

```html
<div class="ds-popover">기초금액은 발주기관이 산정한 예정가격이에요.</div>
```
- 위치 지정은 소비 측/JS. 툴팁보다 긴 내용·상호작용 가능할 때.
