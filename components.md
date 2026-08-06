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
