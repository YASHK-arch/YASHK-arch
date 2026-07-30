import urllib.request
from PIL import Image
import io
import base64

url = "https://plone.org/community/gsoc/google_summer_of_code_sun_logo_2022-svg.png/@@images/image/preview"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req)
    img = Image.open(io.BytesIO(res.read())).convert('RGBA')

    # Convert to a stencil: white pixels become transparent, colored pixels become white
    data = img.getdata()
    new_data = []
    for item in data:
        # If already transparent, keep it transparent
        if item[3] < 10:
            new_data.append((255, 255, 255, 0))
        # If the pixel is white (the lines between the logo segments), make it transparent
        elif item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        # Otherwise it's a colored segment, make it solid white
        else:
            new_data.append((255, 255, 255, item[3]))
    img.putdata(new_data)

    # Add transparent padding to prevent clipping
    padding = 20
    padded_img = Image.new('RGBA', (img.width + 2 * padding, img.height + 2 * padding), (255, 255, 255, 0))
    padded_img.paste(img, (padding, padding))

    # Save the processed and padded image directly as a PNG
    padded_img.save("gssoc.png", format="PNG")
    print("Successfully updated gssoc.png with padding")
except Exception as e:
    print(f"Error: {e}")
