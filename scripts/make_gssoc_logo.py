import urllib.request
from PIL import Image
import io
import base64

url = "https://plone.org/community/gsoc/google_summer_of_code_sun_logo_2022-svg.png/@@images/image/preview"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req)
    img = Image.open(io.BytesIO(res.read())).convert('RGBA')

    # Convert to monochrome white
    data = img.getdata()
    new_data = []
    for item in data:
        # Keep original alpha, but set RGB to 255 (white)
        new_data.append((255, 255, 255, item[3]))
    img.putdata(new_data)

    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {img.width} {img.height}" width="50" height="50">
  <image href="data:image/png;base64,{img_str}" width="{img.width}" height="{img.height}" />
</svg>"""

    with open("gssoc-logo.svg", "w") as f:
        f.write(svg_content)
    print("Successfully updated gssoc-logo.svg")
except Exception as e:
    print(f"Error: {e}")
