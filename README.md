<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>YASHK-arch | GitHub Profile</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Syne:wght@400;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0a0f;
    --surface: #0f0f1a;
    --card: #141420;
    --border: #1e1e30;
    --accent: #7c3aed;
    --accent2: #06b6d4;
    --accent3: #f59e0b;
    --text: #e2e8f0;
    --muted: #64748b;
    --glow: rgba(124, 58, 237, 0.35);
    --glow2: rgba(6, 182, 212, 0.2);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Animated grid background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(124,58,237,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(124,58,237,0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    z-index: 0;
    animation: gridPulse 8s ease-in-out infinite alternate;
  }

  @keyframes gridPulse {
    from { opacity: 0.4; }
    to { opacity: 1; }
  }

  .container {
    max-width: 860px;
    margin: 0 auto;
    padding: 40px 20px;
    position: relative;
    z-index: 1;
  }

  /* ── HERO ── */
  .hero {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 60px 0 40px;
    gap: 20px;
  }

  .avatar-ring {
    position: relative;
    width: 120px;
    height: 120px;
    flex-shrink: 0;
  }

  .avatar-ring::before {
    content: '';
    position: absolute;
    inset: -4px;
    border-radius: 50%;
    background: conic-gradient(var(--accent), var(--accent2), var(--accent3), var(--accent));
    animation: spin 4s linear infinite;
    z-index: 0;
  }

  @keyframes spin {
    to { transform: rotate(360deg); }
  }

  .avatar-inner {
    position: relative;
    z-index: 1;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border: 3px solid var(--bg);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    background: var(--card);
    color: var(--accent);
    overflow: hidden;
  }

  .avatar-initials {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 2.2rem;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -1px;
  }

  .hero-text {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
  }

  .hero-name {
    font-family: 'Syne', sans-serif;
    font-size: 2.6rem;
    font-weight: 800;
    letter-spacing: -1.5px;
    background: linear-gradient(135deg, #ffffff 30%, var(--accent) 70%, var(--accent2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: fadeDown 0.8s ease both;
  }

  .hero-handle {
    font-size: 0.95rem;
    color: var(--accent2);
    letter-spacing: 2px;
    animation: fadeDown 0.9s 0.1s ease both;
    opacity: 0;
  }

  @keyframes fadeDown {
    from { opacity: 0; transform: translateY(-14px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* Animated typing title */
  .hero-title {
    font-size: 1rem;
    color: var(--muted);
    letter-spacing: 1px;
    animation: fadeDown 1s 0.2s ease both;
    opacity: 0;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .typing-text {
    color: var(--accent3);
    white-space: nowrap;
    overflow: hidden;
    border-right: 2px solid var(--accent3);
    animation: typing 3s steps(30, end) 1.2s both, blink 0.75s step-end infinite 1.2s;
    max-width: 0;
  }

  @keyframes typing {
    from { max-width: 0; }
    to { max-width: 380px; }
  }

  @keyframes blink {
    from, to { border-color: transparent; }
    50% { border-color: var(--accent3); }
  }

  /* ── STATUS BADGES ── */
  .badges {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    justify-content: center;
    animation: fadeUp 0.9s 0.4s ease both;
    opacity: 0;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(14px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .badge {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 5px 14px;
    border-radius: 100px;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.5px;
    border: 1px solid transparent;
    position: relative;
    overflow: hidden;
  }

  .badge.green  { background: rgba(16,185,129,0.1); border-color: rgba(16,185,129,0.3); color: #34d399; }
  .badge.purple { background: rgba(124,58,237,0.15); border-color: rgba(124,58,237,0.4); color: #a78bfa; }
  .badge.cyan   { background: rgba(6,182,212,0.1); border-color: rgba(6,182,212,0.3); color: #67e8f9; }
  .badge.amber  { background: rgba(245,158,11,0.1); border-color: rgba(245,158,11,0.3); color: #fcd34d; }

  .badge .dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: currentColor;
    animation: pulse 2s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.7); }
  }

  /* ── SECTION LABELS ── */
  .section {
    margin: 36px 0 16px;
    animation: fadeUp 0.8s ease both;
  }

  .section-label {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 3px;
    color: var(--muted);
    margin-bottom: 16px;
  }

  .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border), transparent);
  }

  .section-label span {
    color: var(--accent2);
  }

  /* ── STATS GRID ── */
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
  }

  .stat-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 16px;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s, border-color 0.2s;
    animation: fadeUp 0.8s ease both;
  }

  .stat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    transform: scaleX(0);
    transition: transform 0.3s ease;
    transform-origin: left;
  }

  .stat-card:hover { transform: translateY(-3px); border-color: var(--accent); }
  .stat-card:hover::before { transform: scaleX(1); }

  .stat-value {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #fff, var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .stat-label {
    font-size: 0.65rem;
    color: var(--muted);
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-top: 4px;
  }

  /* ── TECH STACK ── */
  .tech-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
  }

  .tech-category {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px;
    transition: border-color 0.2s, transform 0.2s;
    animation: fadeUp 0.8s ease both;
  }

  .tech-category:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
  }

  .tech-cat-title {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--accent2);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .tech-cat-icon { font-size: 0.9rem; }

  .tech-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .tech-pill {
    display: flex;
    align-items: center;
    gap: 5px;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 0.7rem;
    font-weight: 500;
    background: rgba(255,255,255,0.04);
    border: 1px solid var(--border);
    color: var(--text);
    transition: background 0.2s, border-color 0.2s, color 0.2s;
    cursor: default;
  }

  .tech-pill:hover {
    background: rgba(124,58,237,0.15);
    border-color: var(--accent);
    color: #c4b5fd;
  }

  .tech-pill .icon { font-size: 0.85rem; }

  /* ── ACTIVITY / CONTRIBUTION GRAPH ── */
  .contrib-graph {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    animation: fadeUp 0.8s ease both;
  }

  .contrib-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  .contrib-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    color: var(--text);
  }

  .contrib-count {
    font-size: 0.72rem;
    color: var(--muted);
  }

  .contrib-count span { color: var(--accent3); }

  .contrib-weeks {
    display: flex;
    gap: 3px;
    overflow-x: auto;
    padding-bottom: 4px;
  }

  .contrib-col {
    display: flex;
    flex-direction: column;
    gap: 3px;
  }

  .contrib-cell {
    width: 11px;
    height: 11px;
    border-radius: 2px;
    background: var(--border);
    transition: transform 0.1s;
    cursor: default;
  }

  .contrib-cell:hover { transform: scale(1.4); }

  .contrib-cell.l1 { background: rgba(124,58,237,0.2); }
  .contrib-cell.l2 { background: rgba(124,58,237,0.4); }
  .contrib-cell.l3 { background: rgba(124,58,237,0.65); }
  .contrib-cell.l4 { background: var(--accent); }

  /* ── STREAK / SKILL BARS ── */
  .skill-bars {
    display: flex;
    flex-direction: column;
    gap: 14px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    animation: fadeUp 0.8s ease both;
  }

  .skill-row {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .skill-meta {
    display: flex;
    justify-content: space-between;
    font-size: 0.72rem;
    color: var(--muted);
  }

  .skill-meta .name { color: var(--text); font-weight: 500; }
  .skill-meta .pct { color: var(--accent2); }

  .skill-track {
    height: 5px;
    background: var(--border);
    border-radius: 100px;
    overflow: hidden;
  }

  .skill-fill {
    height: 100%;
    border-radius: 100px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    transform: scaleX(0);
    transform-origin: left;
    animation: barGrow 1.2s cubic-bezier(0.22, 1, 0.36, 1) 0.6s forwards;
  }

  @keyframes barGrow {
    to { transform: scaleX(1); }
  }

  /* ── FEATURED PROJECTS ── */
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }

  .project-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.25s, transform 0.25s;
    animation: fadeUp 0.8s ease both;
    cursor: default;
  }

  .project-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at top left, rgba(124,58,237,0.08), transparent 60%);
    opacity: 0;
    transition: opacity 0.3s;
  }

  .project-card:hover {
    border-color: var(--accent);
    transform: translateY(-3px);
  }

  .project-card:hover::after { opacity: 1; }

  .project-lang {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--accent2);
    margin-bottom: 8px;
  }

  .project-name {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .project-desc {
    font-size: 0.72rem;
    color: var(--muted);
    line-height: 1.6;
    margin-bottom: 14px;
  }

  .project-meta {
    display: flex;
    gap: 14px;
    font-size: 0.68rem;
    color: var(--muted);
  }

  .project-meta span {
    display: flex;
    align-items: center;
    gap: 4px;
  }

  /* ── CONNECT LINKS ── */
  .connect-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    justify-content: center;
    padding: 10px 0 40px;
    animation: fadeUp 0.8s 0.3s ease both;
    opacity: 0;
  }

  .connect-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    border: 1px solid var(--border);
    background: var(--card);
    color: var(--text);
    text-decoration: none;
    transition: all 0.2s;
    cursor: pointer;
  }

  .connect-btn:hover {
    border-color: var(--accent);
    background: rgba(124,58,237,0.1);
    color: #c4b5fd;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(124,58,237,0.15);
  }

  /* ── FOOTER ── */
  .footer {
    text-align: center;
    font-size: 0.65rem;
    color: var(--muted);
    padding-bottom: 20px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }

  .footer span { color: var(--accent); }

  /* stagger helper */
  .s1 { animation-delay: 0.1s; }
  .s2 { animation-delay: 0.2s; }
  .s3 { animation-delay: 0.3s; }
  .s4 { animation-delay: 0.4s; }
  .s5 { animation-delay: 0.5s; }
  .s6 { animation-delay: 0.6s; }

  /* scrollbar */
  ::-webkit-scrollbar { width: 4px; height: 4px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 2px; }
</style>
</head>
<body>
<div class="container">

  <!-- HERO -->
  <div class="hero">
    <div class="avatar-ring">
      <div class="avatar-inner">
        <span class="avatar-initials">YK</span>
      </div>
    </div>
    <div class="hero-text">
      <div class="hero-name">Yash Kumar</div>
      <div class="hero-handle">@YASHK-arch</div>
      <div class="hero-title">
        <span>&gt;_</span>
        <span class="typing-text">Full-Stack Developer · Systems Architect · Open Source Enthusiast</span>
      </div>
    </div>
    <div class="badges">
      <div class="badge green"><div class="dot"></div> Open to work</div>
      <div class="badge purple"><div class="dot"></div> Building in public</div>
      <div class="badge cyan"><div class="dot"></div> OSS contributor</div>
      <div class="badge amber"><div class="dot"></div> Learning Rust</div>
    </div>
  </div>

  <!-- STATS -->
  <div class="section">
    <div class="section-label"><span>//</span> GitHub Stats</div>
    <div class="stats-grid">
      <div class="stat-card s1">
        <div class="stat-value" id="s1">0</div>
        <div class="stat-label">Commits / yr</div>
      </div>
      <div class="stat-card s2">
        <div class="stat-value" id="s2">0</div>
        <div class="stat-label">Repositories</div>
      </div>
      <div class="stat-card s3">
        <div class="stat-value" id="s3">0</div>
        <div class="stat-label">PRs Merged</div>
      </div>
      <div class="stat-card s4">
        <div class="stat-value" id="s4">0</div>
        <div class="stat-label">Stars Earned</div>
      </div>
    </div>
  </div>

  <!-- TECH STACK -->
  <div class="section">
    <div class="section-label"><span>//</span> Tech Stack</div>
    <div class="tech-grid">
      <!-- Languages -->
      <div class="tech-category s1">
        <div class="tech-cat-title"><span class="tech-cat-icon">🧠</span> Languages</div>
        <div class="tech-pills">
          <div class="tech-pill"><span class="icon">🐍</span> Python</div>
          <div class="tech-pill"><span class="icon">⚡</span> TypeScript</div>
          <div class="tech-pill"><span class="icon">🟨</span> JavaScript</div>
          <div class="tech-pill"><span class="icon">☕</span> Java</div>
          <div class="tech-pill"><span class="icon">🦀</span> Rust</div>
          <div class="tech-pill"><span class="icon">🐚</span> Bash</div>
          <div class="tech-pill"><span class="icon">🗄️</span> SQL</div>
        </div>
      </div>
      <!-- Frontend -->
      <div class="tech-category s2">
        <div class="tech-cat-title"><span class="tech-cat-icon">🎨</span> Frontend</div>
        <div class="tech-pills">
          <div class="tech-pill"><span class="icon">⚛️</span> React</div>
          <div class="tech-pill"><span class="icon">▲</span> Next.js</div>
          <div class="tech-pill"><span class="icon">💚</span> Vue</div>
          <div class="tech-pill"><span class="icon">🌊</span> Tailwind</div>
          <div class="tech-pill"><span class="icon">📦</span> Vite</div>
          <div class="tech-pill"><span class="icon">🎭</span> Framer</div>
          <div class="tech-pill"><span class="icon">🧩</span> Redux</div>
        </div>
      </div>
      <!-- Backend -->
      <div class="tech-category s3">
        <div class="tech-cat-title"><span class="tech-cat-icon">⚙️</span> Backend</div>
        <div class="tech-pills">
          <div class="tech-pill"><span class="icon">🟢</span> Node.js</div>
          <div class="tech-pill"><span class="icon">🚀</span> FastAPI</div>
          <div class="tech-pill"><span class="icon">🌿</span> Django</div>
          <div class="tech-pill"><span class="icon">🔷</span> Express</div>
          <div class="tech-pill"><span class="icon">🐇</span> RabbitMQ</div>
          <div class="tech-pill"><span class="icon">🔴</span> Redis</div>
          <div class="tech-pill"><span class="icon">🔗</span> GraphQL</div>
        </div>
      </div>
      <!-- DevOps / Cloud -->
      <div class="tech-category s4">
        <div class="tech-cat-title"><span class="tech-cat-icon">☁️</span> DevOps & Cloud</div>
        <div class="tech-pills">
          <div class="tech-pill"><span class="icon">🐋</span> Docker</div>
          <div class="tech-pill"><span class="icon">☸️</span> Kubernetes</div>
          <div class="tech-pill"><span class="icon">🏗️</span> Terraform</div>
          <div class="tech-pill"><span class="icon">🔁</span> GitHub CI</div>
          <div class="tech-pill"><span class="icon">🟠</span> AWS</div>
          <div class="tech-pill"><span class="icon">🔵</span> GCP</div>
          <div class="tech-pill"><span class="icon">📊</span> Grafana</div>
        </div>
      </div>
      <!-- Databases -->
      <div class="tech-category s5">
        <div class="tech-cat-title"><span class="tech-cat-icon">🗃️</span> Databases</div>
        <div class="tech-pills">
          <div class="tech-pill"><span class="icon">🐘</span> PostgreSQL</div>
          <div class="tech-pill"><span class="icon">🍃</span> MongoDB</div>
          <div class="tech-pill"><span class="icon">🔥</span> Firebase</div>
          <div class="tech-pill"><span class="icon">⚡</span> Supabase</div>
          <div class="tech-pill"><span class="icon">🕸️</span> Neo4j</div>
          <div class="tech-pill"><span class="icon">📚</span> Prisma</div>
        </div>
      </div>
      <!-- Tools -->
      <div class="tech-category s6">
        <div class="tech-cat-title"><span class="tech-cat-icon">🛠️</span> Tools & Others</div>
        <div class="tech-pills">
          <div class="tech-pill"><span class="icon">🐧</span> Linux</div>
          <div class="tech-pill"><span class="icon">✏️</span> Neovim</div>
          <div class="tech-pill"><span class="icon">🔍</span> Postman</div>
          <div class="tech-pill"><span class="icon">🧪</span> Jest</div>
          <div class="tech-pill"><span class="icon">📐</span> Figma</div>
          <div class="tech-pill"><span class="icon">📡</span> Kafka</div>
        </div>
      </div>
    </div>
  </div>

  <!-- SKILL BARS + CONTRIBUTION GRAPH side by side -->
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin:0 0 36px;">
    <div class="skill-bars s1">
      <div class="section-label" style="margin:0 0 8px;"><span>//</span> Proficiency</div>
      <!-- Python -->
      <div class="skill-row">
        <div class="skill-meta"><span class="name">Python</span><span class="pct">92%</span></div>
        <div class="skill-track"><div class="skill-fill" style="width:92%;"></div></div>
      </div>
      <!-- TypeScript -->
      <div class="skill-row">
        <div class="skill-meta"><span class="name">TypeScript / JS</span><span class="pct">88%</span></div>
        <div class="skill-track"><div class="skill-fill" style="width:88%; animation-delay:0.7s;"></div></div>
      </div>
      <!-- React / Next -->
      <div class="skill-row">
        <div class="skill-meta"><span class="name">React / Next.js</span><span class="pct">85%</span></div>
        <div class="skill-track"><div class="skill-fill" style="width:85%; animation-delay:0.8s;"></div></div>
      </div>
      <!-- DevOps -->
      <div class="skill-row">
        <div class="skill-meta"><span class="name">DevOps / Cloud</span><span class="pct">78%</span></div>
        <div class="skill-track"><div class="skill-fill" style="width:78%; animation-delay:0.9s;"></div></div>
      </div>
      <!-- Rust -->
      <div class="skill-row">
        <div class="skill-meta"><span class="name">Rust</span><span class="pct">52%</span></div>
        <div class="skill-track"><div class="skill-fill" style="width:52%; animation-delay:1s; background:linear-gradient(90deg,#f59e0b,#ef4444);"></div></div>
      </div>
    </div>

    <!-- Contribution graph -->
    <div class="contrib-graph s2">
      <div class="section-label" style="margin:0 0 10px;"><span>//</span> Activity</div>
      <div class="contrib-header">
        <div class="contrib-title">Contribution Graph</div>
        <div class="contrib-count"><span id="contrib-num">0</span> contributions this year</div>
      </div>
      <div class="contrib-weeks" id="contribGraph"></div>
    </div>
  </div>

  <!-- FEATURED PROJECTS -->
  <div class="section">
    <div class="section-label"><span>//</span> Featured Projects</div>
    <div class="projects-grid">
      <div class="project-card s1">
        <div class="project-lang">🐍 Python · FastAPI</div>
        <div class="project-name">🔐 auth-nexus</div>
        <div class="project-desc">High-performance JWT + OAuth2 authentication microservice with role-based access control and rate limiting.</div>
        <div class="project-meta">
          <span>⭐ 142</span>
          <span>🍴 38</span>
          <span>🟣 MIT</span>
        </div>
      </div>
      <div class="project-card s2">
        <div class="project-lang">⚡ TypeScript · Next.js</div>
        <div class="project-name">📊 dashify</div>
        <div class="project-desc">Modular analytics dashboard builder with drag-and-drop widgets and real-time WebSocket updates.</div>
        <div class="project-meta">
          <span>⭐ 89</span>
          <span>🍴 21</span>
          <span>🟣 Apache 2.0</span>
        </div>
      </div>
      <div class="project-card s3">
        <div class="project-lang">🐋 Docker · K8s · Go</div>
        <div class="project-name">☸️ kube-pilot</div>
        <div class="project-desc">CLI toolkit for Kubernetes cluster management with intelligent resource scheduling and one-click rollbacks.</div>
        <div class="project-meta">
          <span>⭐ 67</span>
          <span>🍴 14</span>
          <span>🟣 MIT</span>
        </div>
      </div>
      <div class="project-card s4">
        <div class="project-lang">🦀 Rust · WASM</div>
        <div class="project-name">⚡ wasm-bench</div>
        <div class="project-desc">WebAssembly performance benchmarking suite — compare Rust, Go, C++ and JS execution in-browser with live charts.</div>
        <div class="project-meta">
          <span>⭐ 53</span>
          <span>🍴 9</span>
          <span>🟣 GPL v3</span>
        </div>
      </div>
    </div>
  </div>

  <!-- CONNECT -->
  <div class="section">
    <div class="section-label"><span>//</span> Connect</div>
    <div class="connect-row">
      <div class="connect-btn">🐙 GitHub</div>
      <div class="connect-btn">💼 LinkedIn</div>
      <div class="connect-btn">🐦 X / Twitter</div>
      <div class="connect-btn">📝 Dev.to</div>
      <div class="connect-btn">📬 Email</div>
      <div class="connect-btn">🌐 Portfolio</div>
    </div>
  </div>

  <div class="footer">Built with <span>❤</span> by Yash Kumar · YASHK-arch</div>
</div>

<script>
// Counter animation
function animateCounter(id, target, suffix='', duration=1600) {
  const el = document.getElementById(id);
  if (!el) return;
  let start = 0;
  const step = target / (duration / 16);
  const timer = setInterval(() => {
    start += step;
    if (start >= target) { el.textContent = target + suffix; clearInterval(timer); }
    else { el.textContent = Math.floor(start) + suffix; }
  }, 16);
}

window.addEventListener('load', () => {
  setTimeout(() => {
    animateCounter('s1', 1247);
    animateCounter('s2', 42);
    animateCounter('s3', 193);
    animateCounter('s4', 351);
    animateCounter('contrib-num', 1247);
  }, 600);

  // Build contribution graph
  const graph = document.getElementById('contribGraph');
  const levels = [0,0,0,1,0,0,0,0,1,2,1,0,0,0,1,1,2,3,2,1,0,0,2,3,4,3,2,1,0,1,2,3,4,4,3,2,1,2,3,4,4,3,2,1,0,1,2,3,4,4,3,4,3,2,1,0,1,2,3];
  
  for (let w = 0; w < 53; w++) {
    const col = document.createElement('div');
    col.className = 'contrib-col';
    for (let d = 0; d < 7; d++) {
      const cell = document.createElement('div');
      const idx = (w * 7 + d) % levels.length;
      const l = levels[idx];
      cell.className = 'contrib-cell' + (l > 0 ? ` l${l}` : '');
      // small randomness for realism
      if (Math.random() > 0.7 && l < 4) {
        const bump = [0,'l1','l2','l3','l4'][Math.min(4,l+1)];
        if (bump) cell.classList.add(bump);
      }
      col.appendChild(cell);
    }
    graph.appendChild(col);
  }
});
</script>
</body>
</html>
