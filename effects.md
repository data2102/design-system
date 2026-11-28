# 화면 효과 (Visual effects) — 쓸 때의 규칙

유리 패널, 흐르는 그러데이션, 녹는 로고, 3D 같은 "비싸 보이는" 화면 효과를 여백 DS에서 쓰는 기준.

- 출처·영감: [HANIEE_IM 가이드 · 클로드 코드로 비싼 사이트 화면 효과 내는 4가지](https://hani.nioh.cloud/guides/claude-code-site-effects) (2026-09-15 기준, 2026-11 확인)
- 도구 정보(버전·라이선스·별 수)는 그 가이드에 적힌 값이다. 실제로 쓰기 전에 각 저장소에서 다시 확인한다.

---

## 0. 여백 원칙과의 관계 — 먼저 읽기

여백 DS는 기본적으로 **그라데이션·글로우·장식용 애니메이션을 금지**한다 ([design-system.md §9](design-system.md#9-하지-말-것-안티패턴), [foundations.md 모션](foundations.md#모션)).
화면 효과는 이 규칙의 **좁은 예외**다.

| 화면 | 효과 |
|---|---|
| 업무 자동화 도구, 대시보드, 모니터링, 보고서, 폼 | **금지** — 정보가 주인공인 화면엔 쓰지 않는다 |
| 랜딩·브랜드 페이지 ([marketing.css](marketing.css)) | **허용** — 첫 화면(히어로)에 **하나만** |
| 발표·SNS용 영상/이미지 | 허용 — 녹화본으로 쓰면 성능 문제도 없음 |

한 줄 요약: **"어떤 효과를 넣느냐"보다 "어디에 하나만 넣느냐".** 여러 개 넣으면 느려지고, 오히려 싸 보인다.

---

## 1. 효과 4종 — 언제 무엇을

| 효과 | 생김새 | 내 페이지가 | 도구 | 라이선스 | 난이도 |
|---|---|---|---|---|---|
| **리퀴드 로고** Liquid logo | 로고가 수은처럼 녹고 굴절 | 무엇이든(로고 PNG만 있으면) | [paper-design/liquid-logo](https://github.com/paper-design/liquid-logo) · 웹 도구 [liquid.paper.design](https://liquid.paper.design) | **PolyForm Shield 1.0.0** — 경쟁 제품 용도 금지 | ★ |
| **리퀴드 글래스** Liquid glass | 뒤가 굴절돼 비치는 유리 패널 | 순수 HTML | [dashersw/liquid-glass-js](https://github.com/dashersw/liquid-glass-js) | MIT | ★★ |
| **셰이더 그라디언트** Shader gradient | 천천히 흐르는 그러데이션 배경 | React / Next | [ruucm/shadergradient](https://github.com/ruucm/shadergradient) (`@shadergradient/react`) | MIT | ★★ |
| **3D** React Three Fiber | 조명 아래 천천히 도는 입체 도형 | React / Next | [pmndrs/react-three-fiber](https://github.com/pmndrs/react-three-fiber) | MIT | ★★★ (Three.js 지식 필요) |

**우리 상황에 맞춘 추천**
- 대부분의 도구는 파이썬이 만드는 HTML이고 React가 아니다 → 실제로 쓸 수 있는 건 **리퀴드 로고(녹화본)** 와 **리퀴드 글래스** 정도.
- React 랜딩을 새로 만들 때만 셰이더 그라디언트를 고려. 3D는 꼭 필요할 때만.

**도구별 주의**
- 리퀴드 로고: 투명 배경 PNG 필요. 웹 도구에서 색·굴절·속도를 조절한 뒤 **화면 녹화(영상)로 쓰면** 방문자 기기 부담이 없다.
- 리퀴드 글래스: 커밋 1개, npm 배포 없음 → 파일을 직접 가져와 **우리 repo에 고정(vendoring)**. 버그 수정은 기대하지 않는다. HTML을 더블클릭으로 열면 WebGL이 안 보이므로 로컬 서버로 확인 (`scaffold/serve.py` 처럼).
- 셰이더 그라디언트: React·three 버전 호환을 맞춰야 한다(Next 15 App Router면 React 19 + fiber 9).
- 3D: 탭이 안 보일 때 렌더링을 멈춘다.

---

## 2. 여백식 적용 규칙 (체크리스트)

1. **한 페이지 한 효과, 한 자리.** 히어로 배경 또는 로고 중 하나. 내비·카드·버튼까지 번지지 않게.
2. **색은 토큰에서.** 임의 색 대신 `--accent`·`--accent-bg`·`--surface`·`--warm` 값을 쓴다. 다크 테마에선 다크 값으로.
   - 예) 셰이더 그라디언트: `--surface`(#ffffff) → `--accent-bg`(#e8f3ff) → `--accent`(#3182f6)를 아주 약하게.
3. **은은하게.** 느리게, 대비 낮게, 입자감 약하게. "와!"가 아니라 "고급스럽네" 수준.
4. **글자 위엔 약하게.** 효과 위에 텍스트가 얹히면 대비 4.5:1을 유지한다(`a11y_check.py` 기준). 안 되면 글자 영역의 세기를 낮추거나 비운다.
5. **`prefers-reduced-motion`이면 정지.** 움직임 없는 정지 화면(첫 프레임 또는 단색 `--accent-bg`)으로 대체.
6. **대체 화면 필수.** WebGL이 안 되거나 느린 기기에선 정적 배경(`.ds-hero-wrap`의 은은한 틴트)으로 떨어지게.
7. **실제 휴대폰에서 확인.** 방문자 기기에서 그래픽을 계산하므로 오래된 폰에서 끊기면 빼는 게 낫다.
8. **라이선스 확인.** 특히 리퀴드 로고는 MIT가 아니다.

---

## 3. Claude에게 시킬 때 (복붙용)

**처음 붙일 때**
```
여백 디자인 시스템(github.com/data2102/design-system)의 effects.md 규칙대로,
○○ 랜딩 페이지의 히어로 배경에만 [셰이더 그라디언트 / 리퀴드 글래스]를 하나 넣어줘.
- 먼저 해당 저장소 README를 읽고, 이미 설치돼 있는지 확인한 뒤 하나만 설치
- 색은 tokens.css의 --surface → --accent-bg → --accent, 아주 느리고 은은하게
- prefers-reduced-motion이면 멈추고, WebGL이 안 되면 .ds-hero-wrap 정적 배경으로
- 기존 파일은 덮어쓰지 말고, 다른 섹션엔 효과를 넣지 마
- 로컬 서버에서 효과가 보이고 콘솔에 WebGL 오류가 없는지 확인한 뒤 5줄로 설명
```

**다듬을 때** — 한 번에 하나씩, 위치·색·세기로 말한다.
- "더 느리게" · "더 은은하게" · "입자감 줄여" · "색 대비 낮춰" · "히어로 뒤에만 남기고 나머지는 지워"
- 위치·색을 안 정하면 Claude가 저장소 기본 예제를 그대로 붙인다.

**되돌릴 때** — 효과를 붙이기 전에 먼저 커밋해 두면, 마음에 안 들 때 그 커밋으로 돌아가면 된다.
(가이드에 나온 `git checkout .` 는 커밋하지 않은 변경을 **전부** 지우니 주의.)

---

## 4. UI 이름 사전과의 연결

[`ui-dictionary.md`](ui-dictionary.md) "7. 움직임" 영역에 이 문서의 효과 4종을 추가했다.
