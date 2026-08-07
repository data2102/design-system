# 새 대시보드 스캐폴드 (여백 DS 키트)

여백 DS 표준 부품으로 이미 짜여 있는 **빈 대시보드**. 데이터만 채우면 새 도구 완성.

## 새 도구 만드는 법

1. **이 폴더를 통째로 복사** → 새 이름으로 (예: `방문자_대시보드`).
2. `serve.py` 의 **`build_data()`** 를 실제 데이터 조회/집계로 교체 (지금은 데모).
3. 필요하면 `PAGE` 의 표·패널 구성 조정 (표준 부품 `yb-` 클래스 사용).
4. `python serve.py` → 브라우저에서 `http://127.0.0.1:8090` 자동 열림.

## 이미 들어 있는 것

- 여백 DS 디자인 (색·폰트·컴포넌트) — `yeobaek.py` 단일 소스에서
- 라이트/다크 토글 (◐), HTML 내보내기 (📥)
- 표준 부품: `yb-head`·`yb-kpis/yb-kpi`·`yb-panel`·`yb-table`·`yb-alert`·`yb-bars`·`yb-delta` 등
- 설치 불필요(표준 라이브러리만), 오프라인 동작

## 표준 부품 빠른 참고

| 부품 | 클래스 |
|---|---|
| 헤더 | `.yb-head` (h1 + `.yb-sub` + `.yb-toolbar`) |
| KPI | `.yb-kpis` > `.yb-kpi` (`.lab`/`.val`/`.yb-delta pos|neg`) |
| 패널 | `.yb-panel` (+ `.yb-panel-head`) |
| 표 | `.yb-table.hover` (`th.num`/`td.num`, `.up`/`.down`, `tr.tot`) |
| 이상신호 | `.yb-alert.yb-alert-crit|warn|info|ok` |
| 배지 | `.yb-badge-info|success|warning|danger|mute` |
| 칩/탭 | `.yb-chip.on` · `.yb-tab.on` |
| 막대/범례 | `.yb-bars` > `.yb-bar` · `.yb-legend` |

## 디자인 업데이트

DS가 바뀌면 이 폴더에서 **`DS업데이트.bat`** 실행 → 도구 재실행. (yeobaek.py 최신본을 받아옴)
