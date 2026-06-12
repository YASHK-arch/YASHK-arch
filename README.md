<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>YASHK-arch // Terminal Profile</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@300;400;600&display=swap" rel="stylesheet" />
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --void: #030609;
    --deep: #070d14;
    --panel: #0a1422;
    --panel2: #0d1b2e;
    --cyan: #00ffd1;
    --cyan-dim: #00c9a5;
    --cyan-ghost: rgba(0,255,209,0.06);
    --violet: #9b5de5;
    --violet-dim: #7a44c4;
    --amber: #ffb700;
    --amber-dim: #cc9200;
    --ghost: #d6eeff;
    --ghost-dim: #8aadcc;
    --grid-line: rgba(0,255,209,0.04);
    --border: rgba(0,255,209,0.18);
    --border-dim: rgba(0,255,209,0.08);
    --scanline: rgba(0,0,0,0.35);
  }

  html { background: var(--void); color: var(--ghost); font-family: 'Share Tech Mono', monospace; overflow-x: hidden; }

  body { position: relative; min-height: 100vh; }

  /* Grid background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(var(--grid-line) 1px, transparent 1px),
      linear-gradient(90deg, var(--grid-line) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events: none;
    z-index: 0;
  }

  /* Scanline overlay */
  body::after {
    content: '';
    position: fixed;
    inset: 0;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      var(--scanline) 2px,
      var(--scanline) 4px
    );
    pointer-events: none;
    z-index: 1;
    opacity: 0.25;
    animation: scanPulse 8s ease-in-out infinite;
  }

  @keyframes scanPulse { 0%,100%{opacity:.2} 50%{opacity:.35} }

  .wrap { position: relative; z-index: 2; max-width: 960px; margin: 0 auto; padding: 0 24px 80px; }

  /* ── HUD TOPBAR ── */
  .hud-top {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(3,6,9,0.92);
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(8px);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 24px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.08em;
  }
  .hud-left { color: var(--cyan); }
  .hud-mid { color: var(--ghost-dim); display: flex; gap: 24px; }
  .hud-mid span { position: relative; padding-left: 14px; }
  .hud-mid span::before { content: ''; position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 6px; height: 6px; border-radius: 50%; background: var(--cyan); animation: blink 2s step-end infinite; }
  .hud-right { color: var(--amber); }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }

  /* ── HERO ── */
  .hero {
    padding: 64px 0 48px;
    position: relative;
  }
  .hero-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--cyan);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 16px;
  }
  .hero-label::before { content: '> '; color: var(--violet); }

  .hero-name {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(40px, 8vw, 80px);
    font-weight: 900;
    line-height: 1;
    letter-spacing: -0.02em;
    color: transparent;
    background: linear-gradient(135deg, var(--cyan) 0%, var(--violet) 60%, var(--amber) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    margin-bottom: 12px;
    position: relative;
    display: inline-block;
  }

  .hero-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    color: var(--ghost-dim);
    letter-spacing: 0.05em;
    margin-bottom: 32px;
    line-height: 2;
  }
  .hero-sub .tag { color: var(--cyan); margin-right: 4px; }
  .hero-sub .sep { color: var(--border); margin: 0 8px; }

  .cursor {
    display: inline-block;
    width: 10px;
    height: 1.1em;
    background: var(--cyan);
    vertical-align: text-bottom;
    margin-left: 4px;
    animation: blink 1s step-end infinite;
  }

  /* ── BADGE ROW ── */
  .badge-row { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 48px; }
  .badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border: 1px solid var(--border);
    border-radius: 2px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--ghost-dim);
    background: var(--cyan-ghost);
    text-decoration: none;
    letter-spacing: 0.05em;
    transition: border-color 0.2s, color 0.2s;
    position: relative;
    overflow: hidden;
  }
  .badge::after {
    content: '';
    position: absolute;
    inset: 0;
    background: var(--cyan);
    opacity: 0;
    transition: opacity 0.2s;
  }
  .badge:hover { border-color: var(--cyan); color: var(--cyan); }
  .badge .dot { width: 5px; height: 5px; border-radius: 50%; background: var(--cyan); }
  .badge.amber .dot { background: var(--amber); }
  .badge.violet .dot { background: var(--violet); }

  /* ── SECTION ── */
  .section { margin-bottom: 56px; }
  .sec-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 24px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border-dim);
  }
  .sec-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--cyan);
    letter-spacing: 0.15em;
    opacity: 0.6;
  }
  .sec-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 13px;
    font-weight: 700;
    color: var(--ghost);
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }
  .sec-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border) 0%, transparent 100%);
  }

  /* ── CODE BLOCK (About Me) ── */
  .code-panel {
    background: var(--panel);
    border: 1px solid var(--border-dim);
    border-radius: 2px;
    padding: 24px 28px;
    position: relative;
    overflow: hidden;
  }
  .code-panel::before {
    content: '●  ●  ●';
    display: block;
    color: rgba(255,255,255,0.15);
    font-size: 10px;
    letter-spacing: 6px;
    margin-bottom: 20px;
  }
  .code-panel::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--cyan), transparent);
    opacity: 0.5;
  }
  pre {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12.5px;
    line-height: 1.85;
    white-space: pre-wrap;
    color: var(--ghost-dim);
  }
  .k { color: var(--violet); }
  .s { color: var(--amber); }
  .p { color: var(--cyan); }
  .c { color: rgba(255,255,255,0.3); font-style: italic; }

  /* ── TECH GRID ── */
  .tech-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(110px, 1fr)); gap: 10px; }
  .tech-cell {
    background: var(--panel);
    border: 1px solid var(--border-dim);
    border-radius: 2px;
    padding: 16px 10px 14px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--ghost-dim);
    transition: border-color 0.25s, color 0.25s, background 0.25s;
    cursor: default;
    position: relative;
    overflow: hidden;
  }
  .tech-cell::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 1px;
    background: var(--cyan);
    transform: scaleX(0);
    transition: transform 0.25s;
  }
  .tech-cell:hover { border-color: var(--cyan); color: var(--ghost); background: rgba(0,255,209,0.05); }
  .tech-cell:hover::after { transform: scaleX(1); }
  .tech-cell:hover .tlogo { filter: brightness(0) invert(1) sepia(1) saturate(4) hue-rotate(130deg); opacity: 1; }
  .tlogo {
    width: 32px;
    height: 32px;
    object-fit: contain;
    opacity: 0.55;
    transition: filter 0.25s, opacity 0.25s;
    filter: brightness(0) invert(0.6);
  }
  .tech-cell.amber:hover { border-color: var(--amber); background: rgba(255,183,0,0.05); }
  .tech-cell.amber::after { background: var(--amber); }
  .tech-cell.amber:hover .tlogo { filter: brightness(0) invert(1) sepia(1) saturate(8) hue-rotate(5deg); opacity: 1; }
  .tech-cell.violet:hover { border-color: var(--violet); background: rgba(155,93,229,0.05); }
  .tech-cell.violet::after { background: var(--violet); }
  .tech-cell.violet:hover .tlogo { filter: brightness(0) invert(0.6) sepia(1) saturate(5) hue-rotate(240deg); opacity: 1; }

  /* ── STATS GRID ── */
  .stats-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .stat-card {
    background: var(--panel);
    border: 1px solid var(--border-dim);
    border-radius: 2px;
    padding: 20px 24px;
    position: relative;
    overflow: hidden;
  }
  .stat-card::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 2px;
    background: var(--cyan);
    opacity: 0.7;
  }
  .stat-card.violet::before { background: var(--violet); }
  .stat-card img { width: 100%; border-radius: 2px; display: block; filter: hue-rotate(20deg) saturate(1.1); }
  .stat-label { font-size: 10px; color: var(--cyan); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 8px; font-family: 'JetBrains Mono', monospace; }
  .stat-card.violet .stat-label { color: var(--violet); }

  /* ── ACHIEVEMENT TABLE ── */
  .ach-table { width: 100%; border-collapse: collapse; font-family: 'JetBrains Mono', monospace; font-size: 12px; }
  .ach-table tr { border-bottom: 1px solid var(--border-dim); }
  .ach-table tr:last-child { border-bottom: none; }
  .ach-table tr:hover td { background: var(--cyan-ghost); }
  .ach-table td { padding: 14px 12px; color: var(--ghost-dim); vertical-align: middle; }
  .ach-table td:first-child { color: var(--cyan); width: 36px; font-size: 14px; }
  .ach-table td:nth-child(2) { color: var(--ghost); font-weight: 600; padding-right: 24px; white-space: nowrap; }
  .ach-table td:nth-child(2)::before { content: '// '; color: var(--violet); }

  /* ── CONNECT ── */
  .connect-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 10px; }
  .connect-card {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 4px;
    padding: 16px 18px;
    background: var(--panel);
    border: 1px solid var(--border-dim);
    border-radius: 2px;
    text-decoration: none;
    transition: border-color 0.2s;
    position: relative;
    overflow: hidden;
  }
  .connect-card:hover { border-color: var(--cyan); }
  .connect-card:hover .cc-arrow { transform: translateX(4px); }
  .cc-platform { font-size: 10px; color: var(--ghost-dim); letter-spacing: 0.12em; text-transform: uppercase; font-family: 'JetBrains Mono', monospace; }
  .cc-handle { font-size: 13px; color: var(--cyan); font-family: 'JetBrains Mono', monospace; }
  .cc-handle.violet { color: var(--violet); }
  .cc-handle.amber { color: var(--amber); }
  .cc-arrow { font-size: 11px; color: var(--ghost-dim); margin-top: 4px; transition: transform 0.2s; }

  /* ── FOOTER ── */
  .hud-bot {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    z-index: 100;
    background: rgba(3,6,9,0.92);
    border-top: 1px solid var(--border);
    backdrop-filter: blur(8px);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 7px 24px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.07em;
    color: var(--ghost-dim);
  }
  .hud-bot .status { color: var(--cyan); }
  .hud-bot .warn { color: var(--amber); }

  /* ── DIVIDER ── */
  .divider {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 48px 0;
    color: var(--border);
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
  }
  .divider::before, .divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border-dim);
  }

  /* ── ACTIVITY GRAPH ── */
  .activity-wrap {
    background: var(--panel);
    border: 1px solid var(--border-dim);
    border-radius: 2px;
    padding: 20px;
    overflow: hidden;
  }
  .activity-wrap img { width: 100%; border-radius: 2px; display: block; }

  /* ── QUOTE ── */
  .quote-box {
    border-left: 2px solid var(--violet);
    padding: 16px 24px;
    background: var(--panel);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--ghost-dim);
    line-height: 1.8;
    position: relative;
  }
  .quote-box::before { content: '> '; color: var(--violet); }

  /* ── TYPING ANIMATION ── */
  .typed-line {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: var(--cyan);
    overflow: hidden;
    white-space: nowrap;
    border-right: 2px solid var(--cyan);
    width: 0;
    animation: typeReveal 1.5s steps(40) 0.3s forwards, blinkCaret 0.75s step-end infinite;
  }
  @keyframes typeReveal { to { width: 100%; } }
  @keyframes blinkCaret { 0%,100%{border-color:var(--cyan)} 50%{border-color:transparent} }

  /* ── SNAKE IMG ── */
  .snake-wrap {
    background: var(--panel);
    border: 1px solid var(--border-dim);
    border-radius: 2px;
    padding: 24px;
    overflow: hidden;
  }
  .snake-wrap img { width: 100%; border-radius: 2px; display: block; filter: hue-rotate(155deg) saturate(1.5) brightness(0.85); }

  /* UPTIME CLOCK */
  #clock { font-variant-numeric: tabular-nums; }

  @media (max-width: 600px) {
    .stats-row { grid-template-columns: 1fr; }
    .hero-name { font-size: 36px; }
    .hud-mid { gap: 12px; }
    .tech-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>
</head>
<body>

<!-- HUD TOP -->
<div class="hud-top">
  <span class="hud-left">SYS_ONLINE // YASHK-ARCH.DEV</span>
  <span class="hud-mid">
    <span>NODE_ACTIVE</span>
    <span>UPLINK_STABLE</span>
    <span>INDIA_CLUSTER</span>
  </span>
  <span class="hud-right" id="clock">--:--:--</span>
</div>

<div class="wrap">

  <!-- HERO -->
  <section class="hero">
    <div class="hero-label">CLASSIFIED_PROFILE // OPERATOR_DOSSIER</div>
    <h1 class="hero-name">YASH KUMAR<span class="cursor"></span></h1>
    <div class="hero-sub">
      <span class="tag">[</span>FULL-STACK DEV<span class="tag">]</span>
      <span class="sep">|</span>
      <span class="tag">[</span>DATA ENTHUSIAST<span class="tag">]</span>
      <span class="sep">|</span>
      <span class="tag">[</span>DSA GRINDER<span class="tag">]</span>
    </div>
    <div style="font-family:'JetBrains Mono',monospace; font-size:12px; color:var(--ghost-dim); line-height:2;">
      <span style="color:var(--violet)">$</span> status --operator=yash<br>
      <span style="color:var(--cyan)">✓</span> Jurisdiction: India 🇮🇳 &nbsp;|&nbsp; Languages: Java · JS · Python · Bash<br>
      <span style="color:var(--cyan)">✓</span> Focus: DSA + Building Real Projects &nbsp;|&nbsp; Fun: I solve DSA &gt; scroll social media
    </div>
  </section>

  <!-- BADGE ROW -->
  <div class="badge-row">
    <a href="https://linkedin.com/in/yash-kumar-836847279" class="badge"><span class="dot"></span>LinkedIn</a>
    <a href="mailto:yashkumar02006@gmail.com" class="badge amber"><span class="dot amber"></span>Gmail</a>
    <a href="https://www.youtube.com/@beyondyourthoughts" class="badge amber"><span class="dot amber"></span>YouTube</a>
    <a href="https://x.com/Yash Kumar" class="badge violet"><span class="dot violet"></span>X / Twitter</a>
    <a href="https://github.com/YASHK-arch" class="badge"><span class="dot"></span>GitHub</a>
  </div>

  <!-- ABOUT -->
  <section class="section">
    <div class="sec-header">
      <span class="sec-num">01</span>
      <span class="sec-title">OPERATOR_PROFILE</span>
      <div class="sec-line"></div>
    </div>
    <div class="code-panel">
<pre><span class="c">// identity.config.ts — CLASSIFIED</span>
<span class="k">const</span> <span class="p">yash</span> = {
  <span class="k">name</span>:         <span class="s">"Yash Kumar"</span>,
  <span class="k">location</span>:     <span class="s">"India 🇮🇳"</span>,
  <span class="k">role</span>:         [<span class="s">"Full-Stack Developer"</span>, <span class="s">"Data Enthusiast"</span>],
  <span class="k">languages</span>:    [<span class="s">"Java"</span>, <span class="s">"JavaScript"</span>, <span class="s">"Python"</span>, <span class="s">"Pascal"</span>, <span class="s">"Bash"</span>],
  <span class="k">libraries</span>:    [<span class="s">"NumPy"</span>, <span class="s">"Pandas"</span>, <span class="s">"Matplotlib"</span>, <span class="s">"Seaborn"</span>],
  <span class="k">frontend</span>:     [<span class="s">"HTML"</span>, <span class="s">"CSS"</span>, <span class="s">"Tailwind"</span>, <span class="s">"Vite"</span>, <span class="s">"React"</span>],
  <span class="k">tools</span>:        [<span class="s">"Git"</span>, <span class="s">"Linux"</span>, <span class="s">"Jupyter"</span>, <span class="s">"Firebase"</span>, <span class="s">"Docker"</span>],
  <span class="k">currentFocus</span>: <span class="s">"DSA + Building Real Projects"</span>,
  <span class="k">funFact</span>:      <span class="s">"I solve DSA &gt; scrolling social media 😄"</span>,
};</pre>
    </div>
  </section>

  <!-- TECH STACK -->
  <section class="section">
    <div class="sec-header">
      <span class="sec-num">02</span>
      <span class="sec-title">TECH_ARSENAL</span>
      <div class="sec-line"></div>
    </div>
    <div class="tech-grid">
      <div class="tech-cell"><span class="tech-dot td-amber"></span>JavaScript</div>
      <div class="tech-cell"><span class="tech-dot td-cyan"></span>TypeScript</div>
      <div class="tech-cell"><span class="tech-dot td-cyan"></span>React</div>
      <div class="tech-cell"><span class="tech-dot td-cyan"></span>Tailwind</div>
      <div class="tech-cell"><span class="tech-dot td-violet"></span>Node.js</div>
      <div class="tech-cell"><span class="tech-dot td-amber"></span>Python</div>
      <div class="tech-cell"><span class="tech-dot td-violet"></span>Java</div>
      <div class="tech-cell"><span class="tech-dot td-cyan"></span>MongoDB</div>
      <div class="tech-cell"><span class="tech-dot td-violet"></span>Docker</div>
      <div class="tech-cell"><span class="tech-dot td-cyan"></span>Firebase</div>
      <div class="tech-cell"><span class="tech-dot td-amber"></span>Git</div>
      <div class="tech-cell"><span class="tech-dot td-violet"></span>Linux</div>
      <div class="tech-cell"><span class="tech-dot td-amber"></span>SQL</div>
      <div class="tech-cell"><span class="tech-dot td-cyan"></span>HTML5</div>
      <div class="tech-cell"><span class="tech-dot td-violet"></span>Jupyter</div>
      <div class="tech-cell"><span class="tech-dot td-amber"></span>TensorFlow</div>
    </div>
  </section>

  <!-- GITHUB STATS -->
  <section class="section">
    <div class="sec-header">
      <span class="sec-num">03</span>
      <span class="sec-title">SYSTEM_TELEMETRY</span>
      <div class="sec-line"></div>
    </div>
    <div class="stats-row">
      <div class="stat-card">
        <div class="stat-label">// GitHub Stats</div>
        <img src="https://github-readme-stats.vercel.app/api?username=YASHK-arch&show_icons=true&theme=dark&hide_border=true&include_all_commits=true&count_private=true&rank_icon=github&bg_color=070d14&title_color=00ffd1&text_color=8aadcc&icon_color=9b5de5&card_width=420" alt="GitHub Stats" />
      </div>
      <div class="stat-card violet">
        <div class="stat-label" style="color:var(--violet)">// Streak</div>
        <img src="https://streak-stats.demolab.com?user=YASHK-arch&theme=dark&hide_border=true&stroke=9b5de5&ring=00ffd1&fire=ffb700&currStreakLabel=00ffd1&background=070d14&sideLabels=8aadcc&dates=8aadcc&card_width=420" alt="GitHub Streak" />
      </div>
    </div>
  </section>

  <!-- ACTIVITY -->
  <section class="section">
    <div class="sec-header">
      <span class="sec-num">04</span>
      <span class="sec-title">CONTRIBUTION_SIGNAL</span>
      <div class="sec-line"></div>
    </div>
    <div class="activity-wrap">
      <img src="https://github-readme-activity-graph.vercel.app/graph?username=YASHK-arch&bg_color=070d14&color=00ffd1&line=9b5de5&point=ffb700&area=true&area_color=00ffd1&hide_border=true&custom_title=Yash%27s+Contribution+Graph" alt="Activity Graph" />
    </div>
  </section>

  <!-- ACHIEVEMENTS -->
  <section class="section">
    <div class="sec-header">
      <span class="sec-num">05</span>
      <span class="sec-title">COMMENDATIONS</span>
      <div class="sec-line"></div>
    </div>
    <div class="code-panel">
      <table class="ach-table">
        <tr>
          <td>⚡</td>
          <td>CONSISTENT_CONTRIBUTOR</td>
          <td>Regular commits across personal &amp; open-source projects</td>
        </tr>
        <tr>
          <td>🏗</td>
          <td>FULL_STACK_BUILDER</td>
          <td>End-to-end apps: Vite + Tailwind + Firebase + Node.js</td>
        </tr>
        <tr>
          <td>📊</td>
          <td>DATA_EXPLORER</td>
          <td>Projects in NumPy, Pandas, Matplotlib &amp; TensorFlow</td>
        </tr>
        <tr>
          <td>⚔️</td>
          <td>DSA_ENTHUSIAST</td>
          <td>Active problem solver — Java &amp; Python preferred</td>
        </tr>
        <tr>
          <td>🎮</td>
          <td>GAME_DEV_CURIOUS</td>
          <td>Exploring Unreal Engine &amp; Unity for indie projects</td>
        </tr>
        <tr>
          <td>🎬</td>
          <td>CREATIVE_TECHNOLOGIST</td>
          <td>Adobe CC suite for video, motion &amp; visual design</td>
        </tr>
        <tr>
          <td>☁️</td>
          <td>CLOUD_DEPLOYER</td>
          <td>Apps live on Vercel, Netlify, Firebase &amp; Google Cloud</td>
        </tr>
      </table>
    </div>
  </section>

  <!-- SNAKE -->
  <section class="section">
    <div class="sec-header">
      <span class="sec-num">06</span>
      <span class="sec-title">CONTRIBUTION_SNAKE</span>
      <div class="sec-line"></div>
    </div>
    <div class="snake-wrap">
      <img src="https://raw.githubusercontent.com/YASHK-arch/YASHK-arch/output/github-snake-dark.svg" alt="Contribution Snake" />
    </div>
  </section>

  <!-- QUOTE -->
  <section class="section">
    <div class="sec-header">
      <span class="sec-num">07</span>
      <span class="sec-title">OPERATOR_QUOTE</span>
      <div class="sec-line"></div>
    </div>
    <div class="quote-box">
      Any sufficiently advanced technology is indistinguishable from magic.<br>
      <span style="color:var(--ghost-dim); font-size:11px; display:block; margin-top:8px;">— Arthur C. Clarke &nbsp;·&nbsp; <span style="color:var(--cyan)">exec daily</span></span>
    </div>
  </section>

  <!-- CONNECT -->
  <section class="section">
    <div class="sec-header">
      <span class="sec-num">08</span>
      <span class="sec-title">ESTABLISH_UPLINK</span>
      <div class="sec-line"></div>
    </div>
    <div class="connect-grid">
      <a href="https://linkedin.com/in/yash-kumar-836847279" class="connect-card">
        <span class="cc-platform">LinkedIn</span>
        <span class="cc-handle">yash-kumar</span>
        <span class="cc-arrow">→ connect</span>
      </a>
      <a href="https://x.com/Yash Kumar" class="connect-card">
        <span class="cc-platform">X / Twitter</span>
        <span class="cc-handle violet">@yashkumar</span>
        <span class="cc-arrow">→ follow</span>
      </a>
      <a href="https://www.youtube.com/@beyondyourthoughts" class="connect-card">
        <span class="cc-platform">YouTube</span>
        <span class="cc-handle amber">@beyondyourthoughts</span>
        <span class="cc-arrow">→ subscribe</span>
      </a>
      <a href="mailto:yashkumar02006@gmail.com" class="connect-card">
        <span class="cc-platform">Email</span>
        <span class="cc-handle">yashkumar02006</span>
        <span class="cc-arrow">→ send signal</span>
      </a>
      <a href="https://github.com/YASHK-arch" class="connect-card">
        <span class="cc-platform">GitHub</span>
        <span class="cc-handle">YASHK-arch</span>
        <span class="cc-arrow">→ star repos</span>
      </a>
    </div>
  </section>

  <div class="divider">END_OF_FILE // YASHK-arch // Updated May 2026</div>

</div>

<!-- HUD BOTTOM -->
<div class="hud-bot">
  <span class="status">● UPLINK_STABLE</span>
  <span>OPERATOR: YASH KUMAR &nbsp;|&nbsp; NODE: INDIA_CLUSTER_01 &nbsp;|&nbsp; BUILD: v2.6.0</span>
  <span class="warn">⚠ CLASSIFIED — AUTHORIZED VIEWERS ONLY</span>
</div>

<script>
  function updateClock() {
    const now = new Date();
    const h = String(now.getHours()).padStart(2,'0');
    const m = String(now.getMinutes()).padStart(2,'0');
    const s = String(now.getSeconds()).padStart(2,'0');
    document.getElementById('clock').textContent = h + ':' + m + ':' + s;
  }
  updateClock();
  setInterval(updateClock, 1000);
</script>
</body>
</html>
