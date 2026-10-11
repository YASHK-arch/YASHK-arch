import urllib.request
from PIL import Image
import io
import os

# Source: FOSSASIA's own artwork repo (LGPL-2.1), the square "F" mark.
url = ("https://raw.githubusercontent.com/fossasia/fossasia-artwork/"
       "master/Logo/Square/f-logo.png")
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req)
    img = Image.open(io.BytesIO(res.read())).convert('RGBA')

    # Stencil, same treatment as gssoc.png: white becomes transparent and the
    # coloured mark becomes solid white, so it reads on either theme.
    new_data = []
    for item in img.getdata():
        if item[3] < 10:
            new_data.append((255, 255, 255, 0))
        elif item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append((255, 255, 255, item[3]))
    img.putdata(new_data)

    # Transparent padding to prevent clipping
    padding = 20
    padded = Image.new('RGBA', (img.width + 2 * padding, img.height + 2 * padding),
                       (255, 255, 255, 0))
    padded.paste(img, (padding, padding))

    out_dir = os.environ.get("OUT_DIR", "assets")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "fossasia.png")
    padded.save(out_path, format="PNG")
    print(f"Successfully updated {out_path} with padding")
except Exception as e:
    print(f"Error: {e}")
