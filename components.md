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

### 다크 모드

모든 폼 요소는 토큰을 쓰므로, 상위에 `.theme-dark`만 붙이면 그대로 다크로 전환된다.
