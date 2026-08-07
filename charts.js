/* ============================================================
   여백(Yeobaek) Design System — charts.js  (Phase 7 차트 시스템)
   DS 토큰을 쓰는 미니 차트 헬퍼. 색은 var(--accent)/var(--viz-*) 라 라이트·다크 자동.
   사용: <script>{yeobaek.CHARTS_JS}</script> 로 주입 → window.YB 사용.
     YB.line("#el", {labels, series:[{name,color,values}], area, yFmt})
     YB.spark("#el", [값...])
     YB.donut("#el", [{label,value,color}])
     YB.bars("#el", [{k, value, v, color}])
   ============================================================ */
(function () {
  var NS = "http://www.w3.org/2000/svg";
  var PAL = ["var(--accent)", "var(--viz-2)", "var(--viz-3)", "var(--viz-4)", "var(--viz-5)", "var(--viz-6)"];
  function el(t, a) { var e = document.createElementNS(NS, t); for (var k in a) e.setAttribute(k, a[k]); return e; }
  function host(x) { return typeof x === "string" ? document.querySelector(x) : x; }
  function fmt(n) { return n == null ? "–" : (Math.round(n * 10) / 10).toLocaleString(); }
  function tip() {
    var t = document.getElementById("yb-tt");
    if (!t) { t = document.createElement("div"); t.id = "yb-tt"; t.className = "yb-tt"; document.body.appendChild(t); }
    return t;
  }

  function line(target, o) {
    o = o || {}; var h = host(target); if (!h) return; h.innerHTML = "";
    var W = 640, H = 220, pl = 54, pr = 16, pt = 12, pb = 26;
    var series = o.series || [], labels = o.labels || [], yFmt = o.yFmt || fmt;
    var all = []; series.forEach(function (s) { all = all.concat(s.values); });
    var ymin = Math.min.apply(null, [0].concat(all)), ymax = Math.max.apply(null, all);
    if (ymax === ymin) ymax = ymin + 1; ymax += (ymax - ymin) * 0.12;
    var N = labels.length || (series[0] ? series[0].values.length : 0);
    var X = function (i) { return pl + (W - pl - pr) * (N <= 1 ? 0.5 : i / (N - 1)); };
    var Y = function (v) { return pt + (H - pt - pb) * (1 - (v - ymin) / (ymax - ymin)); };
    var svg = el("svg", { viewBox: "0 0 " + W + " " + H, class: "yb-chart", width: "100%" });
    for (var g = 0; g <= 4; g++) {
      var gv = ymin + (ymax - ymin) * g / 4, gy = Y(gv);
      svg.appendChild(el("line", { x1: pl, y1: gy, x2: W - pr, y2: gy, stroke: "var(--border)", "stroke-width": 1 }));
      var tx = el("text", { x: pl - 7, y: gy + 4, "text-anchor": "end", class: "yb-axt" }); tx.textContent = yFmt(gv); svg.appendChild(tx);
    }
    var stride = Math.max(1, Math.round(N / 8));
    labels.forEach(function (lb, i) {
      if (i % stride === 0 || i === N - 1) { var t = el("text", { x: X(i), y: H - 8, "text-anchor": "middle", class: "yb-axt" }); t.textContent = lb; svg.appendChild(t); }
    });
    series.forEach(function (s, si) {
      var col = s.color || PAL[si % PAL.length], d = "";
      s.values.forEach(function (v, i) { d += (d ? "L" : "M") + X(i) + " " + Y(v); });
      if (o.area && series.length === 1) {
        svg.appendChild(el("path", { d: d + "L" + X(s.values.length - 1) + " " + Y(ymin) + "L" + X(0) + " " + Y(ymin) + "Z", fill: "var(--accent-bg)", stroke: "none" }));
      }
      svg.appendChild(el("path", { d: d, fill: "none", stroke: col, "stroke-width": 2, "stroke-linejoin": "round" }));
      svg.appendChild(el("circle", { cx: X(s.values.length - 1), cy: Y(s.values[s.values.length - 1]), r: 3.4, fill: col }));
    });
    var cx = el("line", { x1: 0, y1: pt, x2: 0, y2: H - pb, stroke: "var(--border-strong)", "stroke-width": 1, opacity: 0 }); svg.appendChild(cx);
    var hit = el("rect", { x: pl, y: pt, width: W - pl - pr, height: H - pt - pb, fill: "transparent" }); hit.style.cursor = "crosshair"; svg.appendChild(hit);
    var tt = tip();
    hit.addEventListener("mousemove", function (e) {
      var b = svg.getBoundingClientRect(), rx = (e.clientX - b.left) / b.width * W, bi = 0, bd = 1e9;
      for (var i = 0; i < N; i++) { var q = Math.abs(X(i) - rx); if (q < bd) { bd = q; bi = i; } }
      cx.setAttribute("x1", X(bi)); cx.setAttribute("x2", X(bi)); cx.setAttribute("opacity", 1);
      tt.style.opacity = 1;
      tt.innerHTML = "<b>" + (labels[bi] != null ? labels[bi] : bi) + "</b>" +
        series.map(function (s) { return "<div>" + (s.name ? s.name + " " : "") + yFmt(s.values[bi]) + "</div>"; }).join("");
      var x = e.clientX + 14, y = e.clientY + 14;
      tt.style.left = Math.min(x, window.innerWidth - tt.offsetWidth - 8) + "px"; tt.style.top = y + "px";
    });
    hit.addEventListener("mouseleave", function () { cx.setAttribute("opacity", 0); tt.style.opacity = 0; });
    h.appendChild(svg);
    if (series.length > 1) {
      var lg = document.createElement("div"); lg.className = "yb-legend";
      lg.innerHTML = series.map(function (s, si) { return '<span class="i"><span class="sw" style="background:' + (s.color || PAL[si % PAL.length]) + '"></span>' + (s.name || ("계열" + (si + 1))) + "</span>"; }).join("");
      h.appendChild(lg);
    }
  }

  function spark(target, values, o) {
    o = o || {}; var h = host(target); if (!h) return; h.innerHTML = "";
    var W = 120, H = 32, mn = Math.min.apply(null, values), mx = Math.max.apply(null, values); if (mx === mn) mx = mn + 1;
    var X = function (i) { return 2 + (W - 4) * (values.length <= 1 ? 0.5 : i / (values.length - 1)); };
    var Y = function (v) { return 2 + (H - 4) * (1 - (v - mn) / (mx - mn)); };
    var svg = el("svg", { viewBox: "0 0 " + W + " " + H, class: "yb-chart", preserveAspectRatio: "none", style: "height:32px" });
    var d = ""; values.forEach(function (v, i) { d += (d ? "L" : "M") + X(i) + " " + Y(v); });
    if (o.area !== false) svg.appendChild(el("path", { d: d + "L" + X(values.length - 1) + " " + H + "L" + X(0) + " " + H + "Z", fill: "var(--accent-bg)", stroke: "none" }));
    svg.appendChild(el("path", { d: d, fill: "none", stroke: "var(--accent)", "stroke-width": 2, "stroke-linecap": "round", "stroke-linejoin": "round" }));
    svg.appendChild(el("circle", { cx: X(values.length - 1), cy: Y(values[values.length - 1]), r: 2.6, fill: "var(--accent)" }));
    h.appendChild(svg);
  }

  function donut(target, segments, o) {
    o = o || {}; var h = host(target); if (!h) return; h.innerHTML = "";
    var total = 0; segments.forEach(function (s) { total += s.value; }); if (!total) total = 1;
    var R = 54, r = 34, cx = 64, cy = 64, a0 = -Math.PI / 2;
    var svg = el("svg", { viewBox: "0 0 128 128", class: "yb-chart", style: "width:128px;height:128px" });
    segments.forEach(function (s, i) {
      var a1 = a0 + s.value / total * Math.PI * 2, large = (a1 - a0) > Math.PI ? 1 : 0;
      var x0 = cx + R * Math.cos(a0), y0 = cy + R * Math.sin(a0), x1 = cx + R * Math.cos(a1), y1 = cy + R * Math.sin(a1);
      var xi = cx + r * Math.cos(a1), yi = cy + r * Math.sin(a1), xi0 = cx + r * Math.cos(a0), yi0 = cy + r * Math.sin(a0);
      svg.appendChild(el("path", { d: "M" + x0 + " " + y0 + "A" + R + " " + R + " 0 " + large + " 1 " + x1 + " " + y1 + "L" + xi + " " + yi + "A" + r + " " + r + " 0 " + large + " 0 " + xi0 + " " + yi0 + "Z", fill: s.color || PAL[i % PAL.length] }));
      a0 = a1;
    });
    h.appendChild(svg);
  }

  function bars(target, items) {
    var h = host(target); if (!h) return; var mx = 1;
    items.forEach(function (i) { if (i.value > mx) mx = i.value; });
    h.innerHTML = '<div class="yb-bars">' + items.map(function (it, i) {
      var pct = Math.round(it.value / mx * 100), col = it.color || PAL[i % PAL.length];
      return '<div class="yb-bar"><span class="k">' + it.k + '</span><span class="track"><span class="fill" style="width:' + pct + '%;background:' + col + '"></span></span><span class="v">' + (it.v != null ? it.v : it.value) + "</span></div>";
    }).join("") + "</div>";
  }

  window.YB = { line: line, spark: spark, donut: donut, bars: bars };
})();
