# -*- coding: utf-8 -*-
"""
새 대시보드 스캐폴드 — 여백(Yeobaek) DS 키트로 시작하는 빈 대시보드.

▶ 새 도구 만드는 법
  1) 이 폴더(scaffold)를 통째로 복사해서 새 도구 폴더로 이름 변경.
  2) 아래 build_data() 를 실제 데이터로 교체 (지금은 데모 데이터).
  3) 필요하면 PAGE 의 표/패널 구성을 조정 (표준 부품 yb- 클래스 사용).
  4) python serve.py   →   http://127.0.0.1:8090  (브라우저 자동 열림)

디자인(색·폰트·컴포넌트)은 전부 yeobaek.py(여백 DS 단일 소스)에서 온다.
→ 디자인 업데이트: DS업데이트.bat 실행 후 도구 재실행. (표준 라이브러리만, 설치 불필요)
"""
import json
import os
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yeobaek  # 여백 DS 단일 소스(vendored)

PORT = 8090


def build_data():
    # ▼▼▼ 여기를 실제 데이터 조회/집계로 교체 ▼▼▼
    return {
        "title": "새 대시보드",
        "sub": "여백 DS 키트 데모 · 여기에 부제(기준일·범위 등)",
        "kpis": [
            {"lab": "오늘 신규", "val": "128", "unit": "건", "delta": "▲ 8.2%", "dir": "pos"},
            {"lab": "처리 완료", "val": "1,876", "unit": "건", "delta": "▲ 3.1%", "dir": "pos"},
            {"lab": "오류율", "val": "0.7", "unit": "%", "delta": "▲ 0.2%", "dir": "neg"},
            {"lab": "예상 매출", "val": "4,820", "unit": "만원", "delta": "▲ 12%", "dir": "pos"},
        ],
        "alerts": [
            {"level": "warn", "ic": "▲", "text": "예시 이상신호 — 특정 항목이 급증했어요. (build_data 에서 채움)"},
        ],
        "rows": [
            {"name": "항목 A", "cur": "328,910", "dod": "▲ 5.3%", "up": True, "mtd": "1,842,300"},
            {"name": "항목 B", "cur": "291,540", "dod": "▲ 2.6%", "up": True, "mtd": "1,640,200"},
            {"name": "항목 C", "cur": "168,050", "dod": "▼ 4.6%", "up": False, "mtd": "980,410"},
        ],
        "bars": [
            {"k": "분류 1", "pct": 100, "v": "24.1", "color": "var(--viz-1)"},
            {"k": "분류 2", "pct": 35, "v": "8.4", "color": "var(--viz-2)"},
            {"k": "분류 3", "pct": 26, "v": "6.2", "color": "var(--viz-3)"},
        ],
    }
    # ▲▲▲ 여기까지 교체 ▲▲▲


PAGE = r"""<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
/*__STYLE__*/
</head><body>
<div class="yb-wrap">
  <div class="yb-head">
    <div><h1 id="t"></h1><div class="yb-sub" id="s"></div></div>
    <div class="yb-toolbar">
      <button class="yb-tbtn" id="exp">📥 HTML</button>
      <button class="yb-tbtn" id="theme">◐ 테마</button>
    </div>
  </div>
  <div id="alerts" class="yb-alerts" style="margin-bottom:16px"></div>
  <div class="yb-kpis" id="kpis"></div>
  <div class="yb-h2">상세 <span class="hint">표준 표 컴포넌트</span></div>
  <div class="yb-panel" style="margin-bottom:14px">
    <table class="yb-table hover">
      <thead><tr><th>항목</th><th class="num">현재</th><th class="num">전일대비</th><th class="num">누적</th></tr></thead>
      <tbody id="rows"></tbody>
    </table>
  </div>
  <div class="yb-h2">분포 <span class="hint">미니 막대</span></div>
  <div class="yb-panel"><div class="yb-bars" id="bars"></div></div>
</div>
<script>
const D = /*__DATA__*/;
const $ = s => document.querySelector(s);
$("#t").textContent = D.title; $("#s").textContent = D.sub;
$("#alerts").innerHTML = D.alerts.map(a=>`<div class="yb-alert yb-alert-${a.level}"><span class="ic">${a.ic}</span><span>${a.text}</span></div>`).join("");
$("#kpis").innerHTML = D.kpis.map(k=>`<div class="yb-kpi"><div class="lab">${k.lab} <span class="yb-delta ${k.dir}">${k.delta}</span></div><div class="val">${k.val} <small>${k.unit}</small></div></div>`).join("");
$("#rows").innerHTML = D.rows.map(r=>`<tr><td>${r.name}</td><td class="num">${r.cur}</td><td class="num ${r.up?'up':'down'}">${r.dod}</td><td class="num">${r.mtd}</td></tr>`).join("");
$("#bars").innerHTML = D.bars.map(b=>`<div class="yb-bar"><span class="k">${b.k}</span><span class="track"><span class="fill" style="width:${b.pct}%;background:${b.color}"></span></span><span class="v">${b.v}</span></div>`).join("");
$("#theme").addEventListener("click",()=>{const r=document.documentElement;r.setAttribute("data-theme", r.getAttribute("data-theme")==="dark"?"light":"dark");});
$("#exp").addEventListener("click",()=>{const h="<!doctype html>\n"+document.documentElement.outerHTML;const b=new Blob([h],{type:"text/html;charset=utf-8"});const a=document.createElement("a");a.href=URL.createObjectURL(b);a.download=D.title+".html";a.click();});
</script>
</body></html>"""


def render():
    data = build_data()
    return (PAGE
            .replace("/*__STYLE__*/", yeobaek.style_tag())
            .replace("__TITLE__", data["title"])
            .replace("/*__DATA__*/", json.dumps(data, ensure_ascii=False)))


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        b = render().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{port}/"
    print(f"● 대시보드 실행 중 → {url}   (종료: Ctrl+C)")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n종료합니다.")


if __name__ == "__main__":
    main()
