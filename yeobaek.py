"""
여백(Yeobaek) Design System — 파이썬 배포 번들  (AUTO-GENERATED)

build_yeobaek.py 가 tokens.css + components.css 로부터 생성합니다. 직접 편집하지 마세요.
(고칠 땐 css 를 고치고  python build_yeobaek.py  재실행)

사용법:
    import yeobaek
    html = f"<style>{yeobaek.CSS}</style> ..."     # 전체(토큰+컴포넌트)
    html = f"<style>{yeobaek.TOKENS}</style> ..."  # 토큰(색·폰트 변수)만

테마: 기본 라이트. 다크는 <html> 또는 상위요소에 class="theme-dark" 또는
      data-theme="dark". 시스템 다크도 자동(prefers-color-scheme).
"""

__version__ = "1.8.0"

TOKENS = r"""
/* ============================================================
   여백(Yeobaek) Design System — tokens.css
   토스류 미니멀(기본) + 다크 모니터링(옵션) 하이브리드
   사용법: <link rel="stylesheet" href="tokens.css">  또는  @import "tokens.css";
   그 다음 값은 var(--이름) 으로 참조.  절대 하드코딩 색을 쓰지 말 것.
   ============================================================ */

/* ---- 폰트 (Noto Sans KR: 부드럽고 인간적, 무료) ---- */

:root {
  /* ===== 색: 브랜드 / 행동 (파랑은 "누를 수 있는 것"에만) ===== */
  --accent:            #3182f6;   /* 기본 액션색 (토스 블루) */
  --accent-hover:      #2b74dc;
  --accent-pressed:    #2264c4;
  --accent-bg:         #e8f3ff;   /* 연한 배경 틴트 (아이콘칩, 선택 상태) */
  --on-accent:         #ffffff;   /* 파란 버튼 위 글자 */

  /* 따뜻한 포인트(개인 도구/기억비서용 보조 액센트, 선택) */
  --warm:              #c96f4c;
  --warm-bg:           #faece7;

  /* ===== 색: 텍스트 (무채색으로 조용히) ===== */
  --text-primary:      #191f28;   /* 본문/제목 */
  --text-secondary:    #4e5968;   /* 보조 설명 */
  --text-tertiary:     #8b95a1;   /* 힌트/메타/캡션 */
  --text-disabled:     #b0b8c1;

  /* ===== 색: 표면 / 배경 ===== */
  --bg:                #f2f4f6;   /* 페이지 바탕 (살짝 회색) */
  --surface:           #ffffff;   /* 카드 */
  --surface-sunken:    #f9fafb;   /* 카드 안 살짝 눌린 영역 */

  /* ===== 색: 경계선 ===== */
  --border:            #eef1f4;   /* 기본 hairline */
  --border-strong:     #d1d6db;   /* 강조 구분선 */

  /* ===== 색: 상태 (의미가 있을 때만) ===== */
  --success:           #12b886;  --success-bg: #e6fcf5;
  --warning:           #f59f00;  --warning-bg: #fff9db;
  --danger:            #f03e3e;  --danger-bg:  #fff0f0;
  --info:              #3182f6;  --info-bg:    #e8f3ff;

  /* 진한 텍스트용(연한 배경 위 글자·채운 버튼) — WCAG AA 대비 확보 */
  --accent-strong:     #1d63c9;   /* 흰 글자 버튼 배경 */
  --success-strong:    #0a7350;
  --warning-strong:    #7a5300;
  --danger-strong:     #c0261e;

  /* ===== 타이포 ===== */
  --font-sans: "Noto Sans KR", "Pretendard", -apple-system, "Malgun Gothic", "맑은 고딕", sans-serif;
  --font-mono: "JetBrains Mono", "D2Coding", Consolas, monospace;

  --fs-display:  30px;  /* 화면당 주인공 숫자 하나 */
  --fs-title:    22px;
  --fs-heading:  18px;
  --fs-subhead:  16px;
  --fs-body:     15px;
  --fs-caption:  13px;
  --fs-footnote: 12px;

  --fw-regular:  400;
  --fw-medium:   500;   /* 기본 강조는 500 (700은 아껴서) */
  --fw-bold:     700;

  --lh-tight:   1.3;    /* 큰 숫자/제목 */
  --lh-body:    1.6;    /* 본문 */
  --ls-tight:  -0.4px;  /* 한글 큰 숫자는 살짝 좁혀야 예쁨 */

  /* ===== 간격 (4px 배수 스케일) ===== */
  --sp-1: 4px;   --sp-2: 8px;   --sp-3: 12px;  --sp-4: 16px;
  --sp-5: 20px;  --sp-6: 24px;  --sp-8: 32px;  --sp-10: 40px;  --sp-12: 48px;

  /* ===== 둥글기 ===== */
  --radius-sm:   8px;    /* 작은 태그/인풋 */
  --radius-md:   12px;   /* 버튼 */
  --radius-lg:   16px;   /* 카드 */
  --radius-xl:   20px;   /* 큰 카드/시트 */
  --radius-pill: 999px;

  /* ===== 그림자 (아주 절제) ===== */
  --shadow-card:    0 1px 3px rgba(0,0,0,0.06);
  --shadow-popover: 0 8px 24px rgba(0,0,0,0.12);
  --shadow-focus:   0 0 0 3px rgba(49,130,246,0.35);
  --shadow-focus-danger: 0 0 0 3px rgba(240,62,62,0.30);

  /* ===== 모션 (mode 무관) ===== */
  --dur-fast: 120ms;   --dur-base: 200ms;   --dur-slow: 320ms;
  --ease-standard: cubic-bezier(.2,0,0,1);   /* 대부분의 전환 */
  --ease-out:      cubic-bezier(0,0,0,1);    /* 등장(진입) */

  /* ===== z-index 스케일 ===== */
  --z-dropdown: 1000; --z-sticky: 1100; --z-overlay: 1200;
  --z-modal:    1300; --z-toast:  1400; --z-tooltip: 1500;

  /* ===== 데이터 시각화 팔레트 (라이트/다크 공통) ===== */
  --viz-1:#3182f6; --viz-2:#12b886; --viz-3:#f59f00;
  --viz-4:#c96f4c; --viz-5:#845ef7; --viz-6:#f06595;
}

/* ============================================================
   다크 모드 / 모니터링 옵션
   .theme-dark 를 붙이거나, 시스템이 dark면 자동 적용.
   → 모니터링·자동화 도구 화면에서 사용.
   ============================================================ */
.theme-dark, :root[data-theme="dark"] {
  --accent:            #22d3ee;   /* 형광 시안 포인트 */
  --accent-hover:      #38dcf0;
  --accent-pressed:    #0fb9d4;
  --accent-bg:         #10313a;
  --on-accent:         #06232a;

  --text-primary:      #e6e8ee;
  --text-secondary:    #c5c9d3;
  --text-tertiary:     #8a90a2;
  --text-disabled:     #565b68;

  --bg:                #0f1117;
  --surface:           #181b24;
  --surface-sunken:    #12141b;

  --border:            #1e2129;
  --border-strong:     #262a35;

  --success:           #34d399;  --success-bg: #0f2e26;
  --warning:           #fbbf24;  --warning-bg: #2e2408;
  --danger:            #f87171;  --danger-bg:  #2e1414;
  --info:              #22d3ee;  --info-bg:    #10313a;

  /* 진한 텍스트용 — 다크에선 밝은 값이 어두운 틴트 위에서 이미 AA 통과 */
  --accent-strong:     #22d3ee;
  --success-strong:    #34d399;
  --warning-strong:    #fbbf24;
  --danger-strong:     #f87171;

  --shadow-card:    0 1px 3px rgba(0,0,0,0.4);
  --shadow-popover: 0 8px 24px rgba(0,0,0,0.5);
  --shadow-focus:   0 0 0 3px rgba(34,211,238,0.35);
  --shadow-focus-danger: 0 0 0 3px rgba(248,113,113,0.30);
}

/* ============================================================
   바로 쓰는 기본 클래스 (선택) — 없어도 var()로 다 쓸 수 있음
   ============================================================ */
.ds-page   { background: var(--bg); color: var(--text-primary);
             font-family: var(--font-sans); font-size: var(--fs-body); line-height: var(--lh-body); }

.ds-card   { background: var(--surface); border: 1px solid var(--border);
             border-radius: var(--radius-lg); padding: var(--sp-5) var(--sp-6); }

.ds-hero   { font-size: var(--fs-display); font-weight: var(--fw-medium);
             line-height: var(--lh-tight); letter-spacing: var(--ls-tight); }

.ds-num    { font-family: var(--font-mono); font-variant-numeric: tabular-nums; }

.ds-btn    { font-family: var(--font-sans); font-size: var(--fs-subhead); font-weight: var(--fw-medium);
             border: none; border-radius: var(--radius-md); padding: 14px var(--sp-5); cursor: pointer; }
.ds-btn-primary   { background: var(--accent-strong); color: var(--on-accent); }
.ds-btn-primary:hover  { background: var(--accent-hover); }
.ds-btn-secondary { background: transparent; color: var(--text-primary); border: 1px solid var(--border-strong); }

.ds-badge  { display: inline-block; font-size: var(--fs-footnote); font-weight: var(--fw-medium);
             padding: 3px 10px; border-radius: var(--radius-sm); }
.ds-badge-success { background: var(--success-bg); color: var(--success-strong); }
.ds-badge-warning { background: var(--warning-bg); color: var(--warning-strong); }
.ds-badge-danger  { background: var(--danger-bg);  color: var(--danger-strong); }

:focus-visible { outline: none; box-shadow: var(--shadow-focus); }
"""

COMPONENTS = r"""
/* ============================================================
   여백(Yeobaek) Design System — components.css
   tokens.css 를 먼저 로드해야 함 (var(--*) 참조).
   Phase 1: 폼 · 입력 컴포넌트
   모든 색·간격은 토큰 경유 → 라이트/다크(.theme-dark) 자동 대응.
   ============================================================ */

/* ---- 폼 레이아웃 ---------------------------------------- */
.ds-field { display:flex; flex-direction:column; gap:var(--sp-2); margin-bottom:var(--sp-4); }
.ds-label { font-size:var(--fs-caption); font-weight:var(--fw-medium); color:var(--text-secondary); }
.ds-req   { color:var(--danger); margin-left:2px; }          /* 필수 표시 * */
.ds-help  { font-size:var(--fs-footnote); color:var(--text-tertiary); }
.ds-error { font-size:var(--fs-footnote); color:var(--danger); display:none; }
.ds-field.is-error .ds-error { display:block; }
.ds-field.is-error .ds-help  { display:none; }

/* ---- 텍스트 입력 / textarea ---------------------------- */
.ds-input, .ds-textarea, .ds-select select {
  width:100%; font-family:var(--font-sans); font-size:var(--fs-body); color:var(--text-primary);
  background:var(--surface); border:1px solid var(--border-strong); border-radius:var(--radius-md);
  transition:border-color .15s, box-shadow .15s, background .15s;
  -webkit-appearance:none; appearance:none;
}
.ds-input   { height:48px; padding:0 var(--sp-4); }
.ds-textarea{ min-height:104px; padding:var(--sp-3) var(--sp-4); line-height:var(--lh-body); resize:vertical; }
.ds-input::placeholder, .ds-textarea::placeholder { color:var(--text-tertiary); }

.ds-input:hover, .ds-textarea:hover, .ds-select select:hover { border-color:var(--text-tertiary); }
.ds-input:focus, .ds-textarea:focus, .ds-select select:focus {
  outline:none; border-color:var(--accent); box-shadow:var(--shadow-focus);
}
.ds-input:disabled, .ds-textarea:disabled, .ds-select select:disabled {
  background:var(--surface-sunken); color:var(--text-disabled); cursor:not-allowed; border-color:var(--border);
}
/* 에러 상태 (필드에 .is-error) */
.ds-field.is-error .ds-input,
.ds-field.is-error .ds-textarea,
.ds-field.is-error .ds-select select { border-color:var(--danger); }
.ds-field.is-error .ds-input:focus,
.ds-field.is-error .ds-textarea:focus,
.ds-field.is-error .ds-select select:focus { box-shadow:var(--shadow-focus-danger); }

/* ---- Select (chevron) ---------------------------------- */
.ds-select { position:relative; display:block; }
.ds-select select { padding-right:40px; cursor:pointer; }
.ds-select::after {
  content:""; position:absolute; right:14px; top:50%; width:16px; height:16px; transform:translateY(-50%);
  pointer-events:none; background-color:var(--text-tertiary);
  -webkit-mask:var(--icon-chevron) center/contain no-repeat; mask:var(--icon-chevron) center/contain no-repeat;
}

/* ---- Search (leading icon) ----------------------------- */
.ds-search { position:relative; display:block; }
.ds-search .ds-input { padding-left:42px; }
.ds-search::before {
  content:""; position:absolute; left:14px; top:50%; width:18px; height:18px; transform:translateY(-50%);
  pointer-events:none; background-color:var(--text-tertiary);
  -webkit-mask:var(--icon-search) center/contain no-repeat; mask:var(--icon-search) center/contain no-repeat;
}

/* ---- Checkbox / Radio ---------------------------------- */
.ds-check, .ds-radio { display:inline-flex; align-items:center; gap:var(--sp-2); cursor:pointer;
  font-size:var(--fs-body); color:var(--text-primary); user-select:none; }
.ds-check input, .ds-radio input { position:absolute; opacity:0; width:1px; height:1px; }
.ds-check .box, .ds-radio .box {
  flex-shrink:0; width:20px; height:20px; border:1.5px solid var(--border-strong);
  background:var(--surface); transition:background .15s, border-color .15s; position:relative;
}
.ds-check .box { border-radius:6px; }
.ds-radio .box { border-radius:50%; }
.ds-check input:hover + .box, .ds-radio input:hover + .box { border-color:var(--text-tertiary); }
.ds-check input:checked + .box, .ds-radio input:checked + .box { background:var(--accent); border-color:var(--accent); }
.ds-check input:checked + .box::after {
  content:""; position:absolute; inset:0; background-color:var(--on-accent);
  -webkit-mask:var(--icon-check) center/12px no-repeat; mask:var(--icon-check) center/12px no-repeat;
}
.ds-radio input:checked + .box::after {
  content:""; position:absolute; inset:5px; border-radius:50%; background:var(--on-accent);
}
.ds-check input:focus-visible + .box, .ds-radio input:focus-visible + .box { box-shadow:var(--shadow-focus); }
.ds-check input:disabled + .box, .ds-radio input:disabled + .box { background:var(--surface-sunken); border-color:var(--border); }
.ds-check:has(input:disabled), .ds-radio:has(input:disabled) { color:var(--text-disabled); cursor:not-allowed; }

/* ---- Switch (토글) ------------------------------------- */
.ds-switch { display:inline-flex; align-items:center; gap:var(--sp-3); cursor:pointer;
  font-size:var(--fs-body); color:var(--text-primary); user-select:none; }
.ds-switch input { position:absolute; opacity:0; width:1px; height:1px; }
.ds-switch .track {
  flex-shrink:0; width:44px; height:26px; border-radius:var(--radius-pill); background:var(--border-strong);
  position:relative; transition:background .18s;
}
.ds-switch .track::after {
  content:""; position:absolute; top:3px; left:3px; width:20px; height:20px; border-radius:50%;
  background:var(--surface); box-shadow:0 1px 2px rgba(0,0,0,.25); transition:transform .18s;
}
.ds-switch input:checked + .track { background:var(--accent); }
.ds-switch input:checked + .track::after { transform:translateX(18px); }
.ds-switch input:focus-visible + .track { box-shadow:var(--shadow-focus); }
.ds-switch input:disabled + .track { background:var(--border); }

/* ---- 아이콘 정의 (mask용, 색은 background-color가 결정) --- */
:root {
  --icon-chevron: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");
  --icon-search:  url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'/%3E%3C/svg%3E");
  --icon-check:   url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E");
}

/* ---- DatePicker (date input) --------------------------- */
.ds-input[type="date"] { cursor:pointer; }
.ds-input[type="date"]::-webkit-calendar-picker-indicator { opacity:.55; cursor:pointer; }
.ds-input[type="date"]:hover::-webkit-calendar-picker-indicator { opacity:.85; }

/* ============================================================
   Phase 2: 피드백 · 오버레이
   ============================================================ */

/* ---- Banner / Alert (인라인 상태 메시지) --------------- */
.ds-banner { display:flex; gap:10px; align-items:flex-start; padding:12px 14px;
  border-radius:var(--radius-md); font-size:var(--fs-caption); color:var(--text-primary); line-height:var(--lh-body); }
.ds-banner .ico { flex-shrink:0; margin-top:1px; width:18px; height:18px; }
.ds-banner-info    { background:var(--info-bg); }    .ds-banner-info .ico    { color:var(--info); }
.ds-banner-success { background:var(--success-bg); } .ds-banner-success .ico { color:var(--success); }
.ds-banner-warning { background:var(--warning-bg); } .ds-banner-warning .ico { color:var(--warning); }
.ds-banner-danger  { background:var(--danger-bg); }  .ds-banner-danger .ico  { color:var(--danger); }

/* ---- Toast (자동 사라짐 알림, 다크 pill) --------------- */
.ds-toast-wrap { position:fixed; bottom:24px; left:50%; transform:translateX(-50%);
  display:flex; flex-direction:column; gap:10px; z-index:var(--z-toast); }
.ds-toast { display:flex; align-items:center; gap:10px; background:var(--text-primary); color:var(--surface);
  padding:12px 16px; border-radius:var(--radius-md); box-shadow:var(--shadow-popover); font-size:var(--fs-caption);
  animation:ds-toast-in var(--dur-base) var(--ease-out); }
.ds-toast .dot { width:8px; height:8px; border-radius:50%; background:var(--success); flex-shrink:0; }
.ds-toast.is-danger .dot { background:var(--danger); }
.ds-toast.is-warning .dot { background:var(--warning); }

/* ---- Modal / Dialog ------------------------------------ */
.ds-overlay { position:fixed; inset:0; background:rgba(0,0,0,.45); display:flex; align-items:center;
  justify-content:center; padding:20px; z-index:var(--z-modal); animation:ds-fade var(--dur-base) var(--ease-out); }
.ds-modal { background:var(--surface); border-radius:var(--radius-xl); box-shadow:var(--shadow-popover);
  max-width:420px; width:100%; padding:24px; animation:ds-pop var(--dur-base) var(--ease-out); }
.ds-modal h3 { font-size:var(--fs-heading); font-weight:var(--fw-medium); margin:0 0 8px; color:var(--text-primary); }
.ds-modal p  { font-size:var(--fs-caption); color:var(--text-secondary); margin:0 0 20px; line-height:var(--lh-body); }
.ds-modal-actions { display:flex; gap:10px; justify-content:flex-end; }

/* ---- Tooltip (data-tip 속성) --------------------------- */
.ds-tip { position:relative; }
.ds-tip::after { content:attr(data-tip); position:absolute; bottom:calc(100% + 8px); left:50%; transform:translateX(-50%);
  background:var(--text-primary); color:var(--surface); font-size:var(--fs-footnote); white-space:nowrap;
  padding:6px 10px; border-radius:var(--radius-sm); opacity:0; pointer-events:none;
  transition:opacity var(--dur-fast); z-index:var(--z-tooltip); }
.ds-tip:hover::after, .ds-tip:focus-visible::after { opacity:1; }

/* ---- Loading: spinner / skeleton / progress ------------ */
.ds-spinner { width:20px; height:20px; border:2.5px solid var(--border-strong); border-top-color:var(--accent);
  border-radius:50%; animation:ds-spin .7s linear infinite; }
.ds-skeleton { background:var(--surface-sunken); border-radius:var(--radius-sm); position:relative; overflow:hidden; }
.ds-skeleton::after { content:""; position:absolute; inset:0;
  background:linear-gradient(90deg, transparent, rgba(128,128,128,.15), transparent); animation:ds-shimmer 1.3s infinite; }
.ds-progress { height:8px; background:var(--surface-sunken); border-radius:var(--radius-pill); overflow:hidden; }
.ds-progress .bar { height:100%; background:var(--accent); border-radius:var(--radius-pill); transition:width var(--dur-base) var(--ease-standard); }

/* ---- EmptyState (빈 화면 = 초대) ----------------------- */
.ds-empty { text-align:center; padding:40px 20px; }
.ds-empty .ico { color:var(--text-tertiary); width:36px; height:36px; margin:0 auto; }
.ds-empty h3 { font-size:var(--fs-subhead); font-weight:var(--fw-medium); margin:14px 0 4px; color:var(--text-primary); }
.ds-empty p  { font-size:var(--fs-caption); color:var(--text-secondary); margin:0 auto 16px; max-width:280px; }

/* ---- 키프레임 ------------------------------------------ */
@keyframes ds-toast-in { from{ opacity:0; transform:translateY(8px); } to{ opacity:1; transform:translateY(0); } }
@keyframes ds-fade { from{ opacity:0; } to{ opacity:1; } }
@keyframes ds-pop  { from{ opacity:0; transform:scale(.96); } to{ opacity:1; transform:scale(1); } }
@keyframes ds-spin { to{ transform:rotate(360deg); } }
@keyframes ds-shimmer { to{ transform:translateX(100%); } }

@media (prefers-reduced-motion:reduce) {
  .ds-spinner, .ds-skeleton::after, .ds-toast, .ds-overlay, .ds-modal { animation:none !important; }
  .ds-progress .bar { transition:none !important; }
}

/* ============================================================
   Phase 3: 데이터 · 탐색
   ============================================================ */

/* ---- Table --------------------------------------------- */
.ds-table { width:100%; border-collapse:collapse; font-size:var(--fs-caption); }
.ds-table thead th { text-align:left; font-size:var(--fs-footnote); font-weight:var(--fw-medium);
  color:var(--text-tertiary); padding:0 12px 10px; border-bottom:1px solid var(--border); white-space:nowrap; }
.ds-table th.num, .ds-table td.num { text-align:right; font-variant-numeric:tabular-nums; }
.ds-table tbody td { padding:14px 12px; border-bottom:1px solid var(--border); color:var(--text-primary); }
.ds-table tbody tr:last-child td { border-bottom:none; }
.ds-table.hover tbody tr { transition:background .12s; }
.ds-table.hover tbody tr:hover { background:var(--surface-sunken); }
.ds-table th.sortable { cursor:pointer; user-select:none; }
.ds-table th.sortable:hover { color:var(--text-secondary); }
.ds-table th .sort-ind { opacity:.5; margin-left:3px; }
.ds-table.sticky thead th { position:sticky; top:0; background:var(--surface); z-index:1; }

/* ---- Tabs (밑줄 스타일) -------------------------------- */
.ds-tabs { display:flex; gap:4px; border-bottom:1px solid var(--border); }
.ds-tab { font-family:inherit; font-size:var(--fs-caption); font-weight:var(--fw-medium); color:var(--text-tertiary);
  background:none; border:none; padding:10px 14px; cursor:pointer; border-bottom:2px solid transparent;
  margin-bottom:-1px; transition:color .15s; }
.ds-tab:hover { color:var(--text-secondary); }
.ds-tab.on { color:var(--accent); border-bottom-color:var(--accent); }
.ds-tab:focus-visible { outline:none; box-shadow:var(--shadow-focus); border-radius:6px; }

/* ---- Pagination ---------------------------------------- */
.ds-pagination { display:flex; gap:4px; align-items:center; }
.ds-page-btn { font-family:inherit; min-width:36px; height:36px; padding:0 8px; border-radius:10px;
  border:1px solid transparent; background:none; color:var(--text-secondary); font-size:var(--fs-caption);
  cursor:pointer; font-variant-numeric:tabular-nums; transition:background .12s; }
.ds-page-btn:hover { background:var(--surface-sunken); }
.ds-page-btn.on { background:var(--accent); color:var(--on-accent); }
.ds-page-btn:disabled { color:var(--text-disabled); cursor:not-allowed; }

/* ---- Breadcrumb ---------------------------------------- */
.ds-breadcrumb { display:flex; align-items:center; gap:8px; font-size:var(--fs-caption); color:var(--text-tertiary); flex-wrap:wrap; }
.ds-breadcrumb a { color:var(--text-secondary); text-decoration:none; }
.ds-breadcrumb a:hover { color:var(--text-primary); }
.ds-breadcrumb .sep { color:var(--text-disabled); }
.ds-breadcrumb .cur { color:var(--text-primary); font-weight:var(--fw-medium); }

/* ---- Nav (사이드바) ------------------------------------ */
.ds-nav { display:flex; flex-direction:column; gap:2px; }
.ds-nav-item { display:flex; align-items:center; gap:10px; padding:10px 12px; border-radius:10px;
  font-size:var(--fs-caption); color:var(--text-secondary); text-decoration:none; cursor:pointer; transition:background .12s, color .12s; }
.ds-nav-item:hover { background:var(--surface-sunken); color:var(--text-primary); }
.ds-nav-item.on { background:var(--accent-bg); color:var(--accent); font-weight:var(--fw-medium); }
.ds-nav-item .ico { width:18px; height:18px; flex-shrink:0; }

/* ---- Chip / Filter ------------------------------------- */
.ds-chip { font-family:inherit; font-size:var(--fs-caption); font-weight:var(--fw-medium); padding:6px 14px;
  border-radius:var(--radius-pill); cursor:pointer; background:var(--surface-sunken); color:var(--text-secondary);
  border:1px solid transparent; transition:.15s; }
.ds-chip:hover { color:var(--text-primary); }
.ds-chip.on { background:var(--accent-bg); color:var(--accent); }

/* ---- Accordion (details/summary) ----------------------- */
.ds-accordion { border:1px solid var(--border); border-radius:var(--radius-md); overflow:hidden; }
.ds-accordion details { border-bottom:1px solid var(--border); }
.ds-accordion details:last-child { border-bottom:none; }
.ds-accordion summary { list-style:none; cursor:pointer; padding:14px 16px; font-size:var(--fs-caption);
  font-weight:var(--fw-medium); color:var(--text-primary); display:flex; justify-content:space-between; align-items:center; }
.ds-accordion summary::-webkit-details-marker { display:none; }
.ds-accordion summary::after { content:""; width:16px; height:16px; flex-shrink:0; background-color:var(--text-tertiary);
  -webkit-mask:var(--icon-chevron) center/contain no-repeat; mask:var(--icon-chevron) center/contain no-repeat; transition:transform .2s; }
.ds-accordion details[open] summary::after { transform:rotate(180deg); }
.ds-accordion .body { padding:0 16px 14px; font-size:var(--fs-footnote); color:var(--text-secondary); line-height:var(--lh-body); }

/* ---- Avatar -------------------------------------------- */
.ds-avatar { width:40px; height:40px; border-radius:50%; background:var(--accent-bg); color:var(--accent);
  display:inline-flex; align-items:center; justify-content:center; font-size:var(--fs-caption); font-weight:var(--fw-medium); overflow:hidden; flex-shrink:0; }
.ds-avatar img { width:100%; height:100%; object-fit:cover; }
.ds-avatar.sm { width:28px; height:28px; font-size:var(--fs-footnote); }
.ds-avatar.lg { width:56px; height:56px; font-size:var(--fs-subhead); }

/* ---- Stepper ------------------------------------------- */
.ds-stepper { display:flex; align-items:center; }
.ds-step { display:flex; align-items:center; gap:8px; font-size:var(--fs-caption); color:var(--text-tertiary); }
.ds-step .dot { width:26px; height:26px; border-radius:50%; border:1.5px solid var(--border-strong);
  display:flex; align-items:center; justify-content:center; font-size:var(--fs-footnote); font-weight:var(--fw-medium);
  color:var(--text-tertiary); background:var(--surface); flex-shrink:0; }
.ds-step.done .dot { background:var(--accent); border-color:var(--accent); color:var(--on-accent); }
.ds-step.cur .dot  { border-color:var(--accent); color:var(--accent); }
.ds-step.cur, .ds-step.done { color:var(--text-primary); }
.ds-step-line { flex:1; height:1.5px; background:var(--border); margin:0 8px; min-width:20px; }
.ds-step-line.done { background:var(--accent); }

/* ---- Popover ------------------------------------------- */
.ds-popover { background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-md);
  box-shadow:var(--shadow-popover); padding:12px 14px; font-size:var(--fs-caption); color:var(--text-secondary);
  max-width:240px; z-index:var(--z-dropdown); }

/* ============================================================
   Phase 4: 데이터 시각화
   색은 --viz-1~6 (foundations.md) + 상태색. 차트 SVG 레시피는 components.md.
   ============================================================ */

/* ---- Stat tile (확장 KPI) ------------------------------ */
.ds-stat { background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-lg); padding:16px 18px; }
.ds-stat .label { font-size:var(--fs-caption); color:var(--text-tertiary); margin-bottom:6px; display:flex; justify-content:space-between; align-items:center; }
.ds-stat .value { font-size:28px; font-weight:var(--fw-medium); letter-spacing:var(--ls-tight); line-height:1.2; font-variant-numeric:tabular-nums; }
.ds-stat .value small { font-size:15px; color:var(--text-tertiary); margin-left:3px; letter-spacing:0; }
.ds-stat .foot { margin-top:8px; }
.ds-stat .spark { display:block; width:100%; height:36px; margin-top:10px; }

/* ---- Delta (추세 지표) --------------------------------- */
.ds-delta { display:inline-flex; align-items:center; gap:3px; font-size:var(--fs-footnote); font-weight:var(--fw-medium); }
.ds-delta.pos { color:var(--success); }   /* 문맥상 "좋음" */
.ds-delta.neg { color:var(--danger); }    /* 문맥상 "나쁨" */
.ds-delta.neutral { color:var(--text-tertiary); }
/* 참고: 한국 증시 관습(상승=빨강)이 필요하면 pos↔neg 색을 프로젝트에서 스왑 */

/* ---- 가로 막대 차트 ------------------------------------ */
.ds-bars { display:flex; flex-direction:column; gap:10px; }
.ds-bar-row { display:flex; align-items:center; gap:10px; font-size:var(--fs-caption); }
.ds-bar-row .k { width:52px; color:var(--text-secondary); flex-shrink:0; }
.ds-bar-track { display:block; flex:1; height:8px; border-radius:var(--radius-pill); background:var(--surface-sunken); overflow:hidden; }
.ds-bar-fill { display:block; height:100%; border-radius:var(--radius-pill); background:var(--viz-1); transition:width var(--dur-base) var(--ease-standard); }
.ds-bar-row .v { width:28px; text-align:right; color:var(--text-tertiary); font-variant-numeric:tabular-nums; flex-shrink:0; }

/* ---- 범례 (Legend) ------------------------------------- */
.ds-legend { display:flex; flex-wrap:wrap; gap:12px; font-size:var(--fs-footnote); color:var(--text-secondary); }
.ds-legend .item { display:inline-flex; align-items:center; gap:6px; }
.ds-legend .swatch { width:10px; height:10px; border-radius:3px; flex-shrink:0; }

/* ---- 도넛 / 링 (conic-gradient) ------------------------ */
.ds-donut { width:96px; height:96px; border-radius:50%; display:flex; align-items:center; justify-content:center; position:relative;
  background:conic-gradient(var(--viz-1) 0 var(--val,60%), var(--surface-sunken) 0); }
.ds-donut::after { content:""; position:absolute; width:64px; height:64px; border-radius:50%; background:var(--surface); }
.ds-donut .center { position:relative; z-index:1; font-size:var(--fs-subhead); font-weight:var(--fw-medium); font-variant-numeric:tabular-nums; }

/* ---- Sparkline / 라인 차트 컨테이너 -------------------- */
.ds-spark { display:block; width:100%; }
.ds-chart { display:block; width:100%; }
/* SVG 안에서: 선 stroke=var(--accent), 영역 fill=var(--accent-bg),
   격자 stroke=var(--border), 끝점 강조 fill=var(--accent). components.md 레시피 참고. */
"""

# 대시보드 키트(Phase 6) — 표준 부품(.yb-kpi/.yb-panel/.yb-table…). 새 도구는 이걸 조립.
DASHBOARD = r"""
/* ============================================================
   여백(Yeobaek) Design System — dashboard.css  (Phase 6 대시보드 키트)
   대시보드용 표준 부품. tokens.css 를 먼저 로드(또는 yeobaek.CSS 에 포함).
   클래스는 yb- 접두사로 기존 도구의 클래스와 충돌하지 않게 한다.
   색은 전부 캐논 토큰 → 라이트/다크 자동.
   ============================================================ */

/* ---- 페이지 / 헤더 -------------------------------------- */
.yb-wrap { max-width: 1120px; margin: 0 auto; padding: 24px 20px 60px; }
.yb-head { display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; margin-bottom: 20px; }
.yb-head h1 { font-size: 20px; font-weight: var(--fw-medium); margin: 0; letter-spacing: var(--ls-tight); color: var(--text-primary); }
.yb-head .yb-sub { font-size: var(--fs-caption); color: var(--text-tertiary); }
.yb-toolbar { margin-left: auto; display: flex; gap: 8px; }
.yb-tbtn { font-family: var(--font-sans); font-size: var(--fs-caption); font-weight: var(--fw-medium);
  color: var(--text-primary); background: transparent; border: 1px solid var(--border-strong);
  border-radius: var(--radius-md); padding: 7px 12px; cursor: pointer; }
.yb-tbtn:hover { background: var(--surface-sunken); }
.yb-live { display: inline-flex; align-items: center; gap: 6px; font-size: var(--fs-footnote); font-weight: var(--fw-medium);
  color: var(--success); background: var(--success-bg); padding: 4px 10px; border-radius: var(--radius-pill); }
.yb-live .dot { width: 7px; height: 7px; border-radius: 50%; background: var(--success); }

/* ---- 섹션 제목 ----------------------------------------- */
.yb-h2 { font-size: 15px; font-weight: var(--fw-medium); color: var(--text-secondary); margin: 26px 0 10px; }
.yb-h2 .hint { font-weight: var(--fw-regular); color: var(--text-tertiary); font-size: var(--fs-footnote); margin-left: 6px; }

/* ---- KPI ----------------------------------------------- */
.yb-kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; }
.yb-kpi { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
  box-shadow: var(--shadow-card); padding: 16px 18px; }
.yb-kpi .lab { font-size: 12.5px; color: var(--text-tertiary); margin-bottom: 6px; display: flex; justify-content: space-between; align-items: center; }
.yb-kpi .val { font-size: 26px; font-weight: var(--fw-medium); letter-spacing: var(--ls-tight); line-height: 1.15;
  font-variant-numeric: tabular-nums; color: var(--text-primary); }
.yb-kpi .val small { font-size: 14px; color: var(--text-tertiary); font-weight: var(--fw-regular); }
.yb-kpi .foot { margin-top: 8px; font-size: var(--fs-footnote); }

/* ---- Delta (추세) -------------------------------------- */
.yb-delta { display: inline-flex; align-items: center; gap: 2px; font-size: var(--fs-footnote); font-weight: var(--fw-medium); }
.yb-delta.pos { color: var(--success); } .yb-delta.neg { color: var(--danger); } .yb-delta.flat { color: var(--text-tertiary); }

/* ---- 패널 ---------------------------------------------- */
.yb-panel { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
  box-shadow: var(--shadow-card); padding: 18px; }
.yb-panel-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; }
.yb-panel-head h3 { font-size: 15px; font-weight: var(--fw-medium); margin: 0; color: var(--text-primary); }
.yb-panel-head .meta { font-size: var(--fs-footnote); color: var(--text-tertiary); }
.yb-grid2 { display: grid; grid-template-columns: 1fr 340px; gap: 14px; align-items: start; }
@media (max-width: 780px) { .yb-grid2 { grid-template-columns: 1fr; } }

/* ---- 데이터 표 ----------------------------------------- */
.yb-table { width: 100%; border-collapse: collapse; font-size: var(--fs-caption); }
.yb-table thead th { text-align: left; font-size: 11.5px; font-weight: var(--fw-medium); color: var(--text-tertiary);
  padding: 0 10px 9px; border-bottom: 1px solid var(--border); white-space: nowrap; }
.yb-table th.num, .yb-table td.num { text-align: right; font-variant-numeric: tabular-nums; }
.yb-table tbody td { padding: 11px 10px; border-bottom: 1px solid var(--border); color: var(--text-primary); }
.yb-table tbody tr:last-child td { border-bottom: none; }
.yb-table.hover tbody tr { transition: background .12s; }
.yb-table.hover tbody tr:hover { background: var(--surface-sunken); }
.yb-table .up { color: var(--success); font-weight: var(--fw-medium); }
.yb-table .down { color: var(--danger); font-weight: var(--fw-medium); }
.yb-table tr.tot td { border-top: 1.5px solid var(--border-strong); font-weight: var(--fw-medium); background: var(--surface-sunken); }
.yb-table .cap { font-size: 11px; color: var(--text-tertiary); }

/* ---- 이상신호 / 배너 ----------------------------------- */
.yb-alerts { display: flex; flex-direction: column; gap: 8px; }
.yb-alert { display: flex; gap: 10px; align-items: flex-start; padding: 12px 14px; border-radius: var(--radius-md);
  font-size: var(--fs-caption); color: var(--text-primary); line-height: var(--lh-body); }
.yb-alert .ic { flex-shrink: 0; font-weight: var(--fw-medium); }
.yb-alert-crit { background: var(--danger-bg); } .yb-alert-crit .ic { color: var(--danger); }
.yb-alert-warn { background: var(--warning-bg); } .yb-alert-warn .ic { color: var(--warning); }
.yb-alert-info { background: var(--info-bg); } .yb-alert-info .ic { color: var(--info); }
.yb-alert-ok { background: var(--success-bg); } .yb-alert-ok .ic { color: var(--success); }

/* ---- 배지 / 칩 / 탭 ------------------------------------ */
.yb-badge { display: inline-block; font-size: 11px; font-weight: var(--fw-medium); padding: 2px 9px; border-radius: var(--radius-sm); }
.yb-badge-info { background: var(--info-bg); color: var(--accent-strong); }
.yb-badge-success { background: var(--success-bg); color: var(--success-strong); }
.yb-badge-warning { background: var(--warning-bg); color: var(--warning-strong); }
.yb-badge-danger { background: var(--danger-bg); color: var(--danger-strong); }
.yb-badge-mute { background: var(--surface-sunken); color: var(--text-disabled); }
.yb-chip { font-family: var(--font-sans); font-size: var(--fs-caption); font-weight: var(--fw-medium); padding: 6px 14px;
  border-radius: var(--radius-pill); cursor: pointer; background: var(--surface-sunken); color: var(--text-secondary); border: 1px solid transparent; }
.yb-chip.on { background: var(--accent-bg); color: var(--accent); }
.yb-tabs { display: flex; gap: 4px; border-bottom: 1px solid var(--border); margin-bottom: 14px; }
.yb-tab { font-family: var(--font-sans); font-size: var(--fs-caption); font-weight: var(--fw-medium); color: var(--text-tertiary);
  background: none; border: none; padding: 10px 14px; cursor: pointer; border-bottom: 2px solid transparent; margin-bottom: -1px; }
.yb-tab.on { color: var(--accent); border-bottom-color: var(--accent); }

/* ---- 미니 막대 + 범례 ---------------------------------- */
.yb-bars { display: flex; flex-direction: column; gap: 10px; }
.yb-bar { display: flex; align-items: center; gap: 10px; font-size: var(--fs-caption); }
.yb-bar .k { width: 90px; color: var(--text-secondary); flex-shrink: 0; }
.yb-bar .track { flex: 1; height: 8px; border-radius: var(--radius-pill); background: var(--surface-sunken); overflow: hidden; }
.yb-bar .fill { height: 100%; border-radius: var(--radius-pill); background: var(--viz-1); }
.yb-bar .v { width: 52px; text-align: right; color: var(--text-tertiary); font-variant-numeric: tabular-nums; flex-shrink: 0; }
.yb-legend { display: flex; flex-wrap: wrap; gap: 12px; font-size: var(--fs-footnote); color: var(--text-secondary); margin-top: 12px; }
.yb-legend .i { display: inline-flex; align-items: center; gap: 6px; }
.yb-legend .sw { width: 10px; height: 10px; border-radius: 3px; }

/* ---- 빈 상태 / 차트 축 --------------------------------- */
.yb-empty { text-align: center; padding: 36px 20px; color: var(--text-tertiary); }
.yb-empty h3 { font-size: var(--fs-subhead); font-weight: var(--fw-medium); margin: 10px 0 4px; color: var(--text-primary); }
.yb-empty p { font-size: var(--fs-caption); color: var(--text-secondary); margin: 0 0 14px; }
.yb-axt { fill: var(--text-tertiary); font-size: 10.5px; }

/* ---- 차트 (charts.js) ---------------------------------- */
.yb-chart { display: block; width: 100%; height: auto; overflow: visible; }
.yb-tt { position: fixed; pointer-events: none; background: var(--surface); color: var(--text-primary);
  border: 1px solid var(--border); border-radius: var(--radius-md); padding: 8px 11px; font-size: 12px;
  box-shadow: var(--shadow-popover); opacity: 0; transition: opacity .08s; z-index: 50; font-variant-numeric: tabular-nums; }
.yb-tt b { font-weight: var(--fw-medium); }

/* ============================================================
   Phase 8 — 확장 · 밀도 · 접근성
   ============================================================ */

/* ---- 세그먼트 컨트롤 (월별/누적 같은 전환) ------------- */
.yb-seg { display: inline-flex; background: var(--surface-sunken); border-radius: 10px; padding: 2px; gap: 2px; }
.yb-seg button { font-family: var(--font-sans); font-size: 12.5px; font-weight: var(--fw-medium); color: var(--text-secondary);
  background: none; border: none; padding: 6px 14px; border-radius: 8px; cursor: pointer; }
.yb-seg button.on { background: var(--surface); color: var(--text-primary); box-shadow: var(--shadow-card); }

/* ---- 필터바 (검색 + 칩 + 셀렉트 조합) ------------------ */
.yb-filterbar { display: flex; gap: 10px; align-items: center; flex-wrap: wrap; margin-bottom: 14px; }
.yb-filterbar .grow { flex: 1; min-width: 160px; }
.yb-filterbar .yb-chips { display: flex; gap: 8px; flex-wrap: wrap; }

/* ---- 접근성: 키보드 포커스 링 (필수) ------------------- */
.yb-tbtn:focus-visible, .yb-chip:focus-visible, .yb-tab:focus-visible,
.yb-seg button:focus-visible { outline: none; box-shadow: var(--shadow-focus); }

/* ---- 밀도: compact (데이터 밀집 화면용) ---------------- */
/* 상위에 class="yb-compact" 를 붙이면 여백·글자가 촘촘해진다. */
.yb-compact .yb-kpi { padding: 11px 13px; }
.yb-compact .yb-kpi .val { font-size: 22px; }
.yb-compact .yb-panel { padding: 13px 14px; }
.yb-compact .yb-h2 { margin: 18px 0 8px; }
.yb-compact .yb-table td, .yb-compact .yb-table tbody td { padding: 8px 9px; }
.yb-compact .yb-table thead th { padding: 0 9px 7px; }
.yb-compact .yb-alert { padding: 9px 12px; }
.yb-compact .yb-kpis { gap: 8px; }
"""

# 레거시 변수 호환(--plane/--bg/--panel/--ink… → 캐논 토큰). 기존 도구 편입용.
COMPAT = """:root{
  --plane:var(--bg); --panel:var(--surface);
  --ink:var(--text-primary); --ink2:var(--text-secondary); --muted:var(--text-secondary);
  --line:var(--border-strong); --line2:var(--border); --line3:var(--border-strong);
  --grid:var(--border); --axis:var(--text-tertiary);
  --accent-soft:var(--accent-bg);
  --up:var(--success); --up-bg:var(--success-bg); --good:var(--success); --good-ink:var(--success); --ok-bg:var(--success-bg);
  --down:var(--danger); --down-bg:var(--danger-bg); --crit:var(--danger); --crit-bg:var(--danger-bg);
  --warn:var(--warning); --warn-bg:var(--warning-bg); --wait:var(--warning); --wait-bg:var(--warning-bg);
  --s1:var(--accent); --s2:var(--success); --s3:var(--warning);
  --yA:var(--accent-bg); --yB:var(--accent); --yC:var(--accent);
  --bar:var(--accent); --target:var(--text-tertiary);
  --track:var(--surface-sunken);
  --shadow-pop:var(--shadow-popover); --shadow-card:var(--shadow-card);
  --radius:var(--radius-md); --num-font:var(--font-mono);
  --sans:var(--font-sans); --mono:var(--font-mono);
}"""

CSS = TOKENS + "\n" + COMPONENTS + "\n" + DASHBOARD

# 차트 헬퍼 JS (Phase 7) — window.YB.line/spark/donut/bars
CHARTS_JS = r"""
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
"""

# 기존 도구(자체 변수명 사용)를 위한 토큰+호환 묶음.
TOKENS_COMPAT = TOKENS + "\n" + COMPAT


def style_tag(full=True):
    """<style>...</style> 문자열. full=False 면 토큰(변수)만."""
    return "<style>\n" + (CSS if full else TOKENS) + "\n</style>"


def script_tag():
    """<script>...</script> 문자열 — 차트 헬퍼(window.YB) 주입용."""
    return "<script>\n" + CHARTS_JS + "\n</script>"
