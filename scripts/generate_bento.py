#!/usr/bin/env python3
import urllib.request
import base64
import os
import re

BADGES = [
    # Frontend (col 0, 1)
    {"cat": "🎨 Frontend", "name": "HTML5", "url": "https://img.shields.io/badge/html5-%231a1a1a.svg?style=for-the-badge&logo=html5&logoColor=white"},
    {"cat": "🎨 Frontend", "name": "CSS3", "url": "https://img.shields.io/badge/css3-%231a1a1a.svg?style=for-the-badge&logo=css3&logoColor=white"},
    {"cat": "🎨 Frontend", "name": "React", "url": "https://img.shields.io/badge/react-%231a1a1a.svg?style=for-the-badge&logo=react&logoColor=white"},
    {"cat": "🎨 Frontend", "name": "Tailwind CSS", "url": "https://img.shields.io/badge/tailwindcss-%231a1a1a.svg?style=for-the-badge&logo=tailwind-css&logoColor=white"},
    {"cat": "🎨 Frontend", "name": "Bootstrap", "url": "https://img.shields.io/badge/bootstrap-%231a1a1a.svg?style=for-the-badge&logo=bootstrap&logoColor=white"},
    {"cat": "🎨 Frontend", "name": "Vite", "url": "https://img.shields.io/badge/vite-%231a1a1a.svg?style=for-the-badge&logo=vite&logoColor=white"},
    {"cat": "🎨 Frontend", "name": "Jinja", "url": "https://img.shields.io/badge/jinja-%231a1a1a.svg?style=for-the-badge&logo=jinja&logoColor=white"},

    # Databases & Cloud (col 2)
    {"cat": "🗄️ Databases & Cloud", "name": "MongoDB", "url": "https://img.shields.io/badge/MongoDB-%231a1a1a.svg?style=for-the-badge&logo=mongodb&logoColor=white"},
    {"cat": "🗄️ Databases & Cloud", "name": "PostgreSQL", "url": "https://img.shields.io/badge/postgresql-%231a1a1a.svg?style=for-the-badge&logo=postgresql&logoColor=white"},
    {"cat": "🗄️ Databases & Cloud", "name": "MySQL", "url": "https://img.shields.io/badge/mysql-%231a1a1a.svg?style=for-the-badge&logo=mysql&logoColor=white"},
    {"cat": "🗄️ Databases & Cloud", "name": "SQLite", "url": "https://img.shields.io/badge/sqlite-%231a1a1a.svg?style=for-the-badge&logo=sqlite&logoColor=white"},
    {"cat": "🗄️ Databases & Cloud", "name": "Supabase", "url": "https://img.shields.io/badge/Supabase-%231a1a1a.svg?style=for-the-badge&logo=supabase&logoColor=white"},
    {"cat": "🗄️ Databases & Cloud", "name": "Firebase", "url": "https://img.shields.io/badge/Firebase-%231a1a1a.svg?style=for-the-badge&logo=firebase&logoColor=white"},

    # Languages (col 0)
    {"cat": "💻 Languages", "name": "Python", "url": "https://img.shields.io/badge/python-%231a1a1a.svg?style=for-the-badge&logo=python&logoColor=white"},
    {"cat": "💻 Languages", "name": "JavaScript", "url": "https://img.shields.io/badge/javascript-%231a1a1a.svg?style=for-the-badge&logo=javascript&logoColor=white"},
    {"cat": "💻 Languages", "name": "TypeScript", "url": "https://img.shields.io/badge/typescript-%231a1a1a.svg?style=for-the-badge&logo=typescript&logoColor=white"},
    {"cat": "💻 Languages", "name": "Java", "url": "https://img.shields.io/badge/java-%231a1a1a.svg?style=for-the-badge&logo=openjdk&logoColor=white"},

    # Backend (col 1)
    {"cat": "⚙️ Backend", "name": "Node.js", "url": "https://img.shields.io/badge/node.js-%231a1a1a.svg?style=for-the-badge&logo=node.js&logoColor=white"},
    {"cat": "⚙️ Backend", "name": "Flask", "url": "https://img.shields.io/badge/flask-%231a1a1a.svg?style=for-the-badge&logo=flask&logoColor=white"},
    {"cat": "⚙️ Backend", "name": "SQLAlchemy", "url": "https://img.shields.io/badge/SQLAlchemy-%231a1a1a.svg?style=for-the-badge&logo=sqlalchemy&logoColor=white"},
    {"cat": "⚙️ Backend", "name": "Psycopg2", "url": "https://img.shields.io/badge/psycopg2-%231a1a1a.svg?style=for-the-badge&logo=postgresql&logoColor=white"},

    # Data Science & ML (col 0, 1)
    {"cat": "🧠 Data Science & ML", "name": "NumPy", "url": "https://img.shields.io/badge/numpy-%231a1a1a.svg?style=for-the-badge&logo=numpy&logoColor=white"},
    {"cat": "🧠 Data Science & ML", "name": "Pandas", "url": "https://img.shields.io/badge/pandas-%231a1a1a.svg?style=for-the-badge&logo=pandas&logoColor=white"},
    {"cat": "🧠 Data Science & ML", "name": "Matplotlib", "url": "https://img.shields.io/badge/Matplotlib-%231a1a1a.svg?style=for-the-badge&logo=plotly&logoColor=white"},
    {"cat": "🧠 Data Science & ML", "name": "Seaborn", "url": "https://img.shields.io/badge/Seaborn-%231a1a1a.svg?style=for-the-badge&logo=python&logoColor=white"},
    {"cat": "🧠 Data Science & ML", "name": "SciPy", "url": "https://img.shields.io/badge/SciPy-%231a1a1a.svg?style=for-the-badge&logo=scipy&logoColor=white"},
    {"cat": "🧠 Data Science & ML", "name": "Scikit-learn", "url": "https://img.shields.io/badge/scikit--learn-%231a1a1a.svg?style=for-the-badge&logo=scikitlearn&logoColor=white"},

    # DevOps & Tools (col 2)
    {"cat": "🛠️ DevOps & Tools", "name": "Docker", "url": "https://img.shields.io/badge/docker-%231a1a1a.svg?style=for-the-badge&logo=docker&logoColor=white"},
    {"cat": "🛠️ DevOps & Tools", "name": "Git", "url": "https://img.shields.io/badge/git-%231a1a1a.svg?style=for-the-badge&logo=git&logoColor=white"},
    {"cat": "🛠️ DevOps & Tools", "name": "Linux", "url": "https://img.shields.io/badge/linux-%231a1a1a.svg?style=for-the-badge&logo=linux&logoColor=white"},
]

LAYOUT = {
    "🎨 Frontend": {"col": 0, "row": 0, "colspan": 2, "rowspan": 1},
    "🗄️ Databases & Cloud": {"col": 2, "row": 0, "colspan": 1, "rowspan": 2},
    "💻 Languages": {"col": 0, "row": 1, "colspan": 1, "rowspan": 1},
    "⚙️ Backend": {"col": 1, "row": 1, "colspan": 1, "rowspan": 1},
    "🧠 Data Science & ML": {"col": 0, "row": 2, "colspan": 2, "rowspan": 1},
    "🛠️ DevOps & Tools": {"col": 2, "row": 2, "colspan": 1, "rowspan": 1},
}

def fetch_badge(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as r:
        svg_data = r.read().decode('utf-8')
        
    def replacer(match):
        x, y, w, h, b64 = match.groups()
        decoded = base64.b64decode(b64).decode('utf-8')
        decoded = re.sub(r'<\?xml.*?\?>', '', decoded)
        # shields.io base64 SVGs often don't have x,y,width,height on the root tag, so we inject them
        decoded = re.sub(r'<svg ', f'<svg x="{x}" y="{y}" width="{w}" height="{h}" ', decoded, count=1)
        return decoded

    # Replace <image ... href="data:image/svg+xml;base64,..."/> with the actual decoded <svg>
    svg_data = re.sub(r'<image\s+x="([^"]+)"\s+y="([^"]+)"\s+width="([^"]+)"\s+height="([^"]+)"\s+href="data:image/svg\+xml;base64,([^"]+)"\s*/>', replacer, svg_data)
        
    width_match = re.search(r'width="(\d+(?:\.\d+)?)"', svg_data)
    height_match = re.search(r'height="(\d+(?:\.\d+)?)"', svg_data)
    width = float(width_match.group(1)) if width_match else 100.0
    height = float(height_match.group(1)) if height_match else 28.0
    
    b64 = base64.b64encode(svg_data.encode('utf-8')).decode('utf-8')
    data_uri = f"data:image/svg+xml;base64,{b64}"
    # We will return the raw SVG data to inline it, to bypass GitHub markdown proxy blocking base64 image hrefs.
    return svg_data, width, height

def generate_svg():
    TOTAL_WIDTH = 800
    GAP = 12
    PADDING = 20
    COLS = 3
    CELL_WIDTH = (TOTAL_WIDTH - (COLS - 1) * GAP) / COLS
    
    # Calculate row heights dynamically based on content
    row_heights = {0: 0, 1: 0, 2: 0}
    
    # Group badges by category and fetch data
    grouped_badges = {cat: [] for cat in LAYOUT}
    for b in BADGES:
        cat = b["cat"]
        svg_data, w, h = fetch_badge(b["url"])
        grouped_badges[cat].append({"name": b["name"], "svg_data": svg_data, "w": w, "h": h})
        
    # First pass: layout within each cell to determine required heights
    cell_layouts = {}
    
    for cat, conf in LAYOUT.items():
        colspan = conf["colspan"]
        available_w = colspan * CELL_WIDTH + (colspan - 1) * GAP - 2 * PADDING
        
        current_x = PADDING
        current_y = PADDING + 35 # Space for title
        max_row_h = 0
        
        placements = []
        for badge in grouped_badges[cat]:
            if current_x + badge["w"] > PADDING + available_w and current_x > PADDING:
                current_x = PADDING
                current_y += max_row_h + GAP
                max_row_h = 0
                
            placements.append({"badge": badge, "x": current_x, "y": current_y})
            current_x += badge["w"] + GAP
            max_row_h = max(max_row_h, badge["h"])
            
        total_h = current_y + max_row_h + PADDING
        cell_layouts[cat] = {"placements": placements, "min_h": total_h}
        
        rowspan = conf["rowspan"]
        if rowspan == 1:
            row_heights[conf["row"]] = max(row_heights[conf["row"]], total_h)

    # Resolve rowspan heights (Database spans row 0 and 1)
    # Ensure row 0 + row 1 + GAP >= Database min_h
    db_min_h = cell_layouts["🗄️ Databases & Cloud"]["min_h"]
    if row_heights[0] + row_heights[1] + GAP < db_min_h:
        diff = db_min_h - (row_heights[0] + row_heights[1] + GAP)
        row_heights[1] += diff # Add diff to bottom row
        
    # Calculate row Y offsets
    row_y = {0: 0}
    row_y[1] = row_y[0] + row_heights[0] + GAP
    row_y[2] = row_y[1] + row_heights[1] + GAP
    
    TOTAL_HEIGHT = row_y[2] + row_heights[2]

    # Generate SVG
    svg_elements = []
    svg_elements.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {TOTAL_WIDTH} {TOTAL_HEIGHT}" width="100%" height="100%">')
    svg_elements.append("""<style>
        .box { fill: transparent; stroke: #30363d; stroke-width: 1px; rx: 8px; transition: fill 0.3s ease, stroke 0.3s ease; }
        .box-group:hover .box { fill: #1a1e23; stroke: #8b949e; }
        .title { fill: #c9d1d9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 15px; font-weight: 600; }
    </style>""")

    for cat, conf in LAYOUT.items():
        col = conf["col"]
        row = conf["row"]
        colspan = conf["colspan"]
        rowspan = conf["rowspan"]
        
        box_x = col * (CELL_WIDTH + GAP)
        box_y = row_y[row]
        box_w = colspan * CELL_WIDTH + (colspan - 1) * GAP
        box_h = sum(row_heights[r] for r in range(row, row + rowspan)) + (rowspan - 1) * GAP
        
        svg_elements.append(f'<g class="box-group" transform="translate({box_x}, {box_y})">')
        svg_elements.append(f'<rect class="box" x="0" y="0" width="{box_w}" height="{box_h}" />')
        
        # Center title
        svg_elements.append(f'<text class="title" x="{box_w/2}" y="{PADDING + 12}" text-anchor="middle">{cat}</text>')
        
        # Place badges
        lines = {}
        for p in cell_layouts[cat]["placements"]:
            lines.setdefault(p["y"], []).append(p)
            
        for y, badges_in_line in lines.items():
            line_w = sum(p["badge"]["w"] for p in badges_in_line) + GAP * (len(badges_in_line) - 1)
            start_x = (box_w - line_w) / 2 # Center horizontally
            
            cur_x = start_x
            for p in badges_in_line:
                b = p["badge"]
                inner_svg = b["svg_data"]
                inner_svg = re.sub(r'<\?xml.*?\?>', '', inner_svg)
                inner_svg = re.sub(r'<svg ', f'<svg x="{cur_x}" y="{p["y"]}" ', inner_svg, count=1)
                svg_elements.append(inner_svg)
                cur_x += b["w"] + GAP
                
        svg_elements.append('</g>')

    svg_elements.append('</svg>')
    
    with open("bento.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(svg_elements))
        
if __name__ == "__main__":
    generate_svg()
