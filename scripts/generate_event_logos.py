gssoc_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="50" height="50">
  <circle cx="50" cy="50" r="45" fill="none" stroke="#ffffff" stroke-width="5" />
  <text x="50" y="55" font-family="Courier New, monospace" font-size="22" font-weight="bold" fill="#ffffff" text-anchor="middle" alignment-baseline="middle">GSSOC</text>
</svg>"""

swoc_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="50" height="50">
  <circle cx="50" cy="50" r="45" fill="none" stroke="#ffffff" stroke-width="5" />
  <text x="50" y="55" font-family="Courier New, monospace" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle" alignment-baseline="middle">SWOC</text>
</svg>"""

with open("gssoc-logo.svg", "w") as f: f.write(gssoc_svg)
with open("swoc-logo.svg", "w") as f: f.write(swoc_svg)
