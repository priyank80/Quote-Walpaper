import json
import os
import textwrap
from langdetect import detect
import random
from PIL import Image, ImageDraw, ImageFont

# Configuration
json_path = "data/quotes.json"
font_path_regular = "fonts/Roboto-Regular.ttf"
font_path_italic = "fonts/DancingScript-Bold.ttf"
output_dir = "wallpapers"
image_width, image_height = 1920, 1080
text_color = (0, 0, 0)
accent_color = (128, 0, 128)
quote_font_size = 64
author_font_size = 44
max_chars = 45
line_thickness = 2
dot_radius = 6
accent_length = 80
line_margin = 80
spacing = 50

# Pastel colors (hex)
pastel_colors = [
   "#74bbfb", "#64bfa4", "#87cefa", "#92cbf1", "#93ccea", "#95e3c0", "#98d98e", "#98f6b0", "#9ab8c2", "#a1d7c9", "#a2cffe", "#a4f4f9", "#a5ced5", "#a5ceec", "#a5fbd5", "#a6e7ff", "#a6fbb2", "#a9c0cb", "#a9d39e", "#aaffaa", "#ace5ee", "#add8e6", "#aec9eb", "#aefd6c", "#b0cec2", "#b1cdac", "#b1fc99", "#b2dcef", "#b2e79f", "#b5cbbb", "#b5ced4", "#b7d24b", "#b7dadd", "#b9b1b6", "#bbbcde", "#bde8d8", "#beb4ab", "#bebdac", "#bee7a5", "#befd73", "#bf77f6", "#bfafb2", "#bfb5a2", "#bfefff", "#c0cba1", "#c2b2f0", "#c3ddd6", "#c3e7e8", "#c4adc9", "#c4fe82", "#c6bedd", "#c6e3f7", "#c6e5ca", "#c6ec7a", "#c7dfb8", "#c8e0e0", "#c8f3cd", "#c8fd3d", "#cae1d9", "#cae277", "#cbe3ee", "#ccccff", "#cce1c7", "#ccfd7f", "#cec8ef", "#cef0cc", "#cfa46b", "#cfbbd8", "#cfe09d", "#cff6f4", "#cffdbc", "#d0d1c1", "#d0f0c0", "#d0fefe", "#d1ffbd", "#d2bfc4", "#d2cbaf", "#d3b683", "#d3d6c4", "#d3d9d1", "#d3e5db", "#d4bbb1", "#d4c9a6", "#d4ede3", "#d5ffff", "#d6c7d6", "#d6fffe", "#d7b1b2", "#d7cec5", "#d7cfbb", "#d7d3a6", "#d7e7d0", "#d7eee4", "#d8b7cf", "#d8d3e6", "#d8d8d0", "#d8e8e6", "#d9d9f3", "#d9dfe0", "#d9e3e5", "#dabbbb", "#dacfba", "#dae4ee", "#dba39a", "#dbeee0", "#dbf4d8", "#dccdbc", "#dcdbca", "#dce7e5", "#ddd3ae", "#ddd6e1", "#dddcdb", "#dde3d5", "#ddedbd", "#ddffdd", "#dedbcc", "#deeadc", "#deeced", "#def7fe", "#dfb19b", "#dfb1b6", "#dfbb7e", "#dfc09f", "#e0d7c6", "#e0dddd", "#e0ded8", "#e0e1d1", "#e0e6d7", "#e1c8d1", "#e1d590", "#e1de8f", "#e1eaec", "#e2c779", "#e3b6aa", "#e3d3bf", "#e3e7c4", "#e3e7e1", "#e4d7c5", "#e4ded5", "#e5bca5", "#e5ccbd", "#e5e2e7", "#e5e4e2", "#e5e7e9", "#e5e8f2", "#e5e9e1", "#e5edf1", "#e6d5ba", "#e6d5ce", "#e6dee6", "#e6e0d4", "#e6e8fa", "#e6f9f1", "#e7d5c9", "#e7e5e8", "#e7eae5", "#e7feff", "#e8e3d9", "#e8e3db", "#e8e8e8", "#e8eae6", "#e8ebe7", "#e8f4f7", "#e9c2a1", "#e9d3ba", "#e9e4ef", "#e9edbd", "#eacacb", "#ead795", "#ead8bb", "#eadac2", "#eae0c8", "#eae3cd", "#eae3d2", "#eae9e0", "#eaeaea", "#eaeeec", "#ebcfaa", "#ebe1ce", "#ebe3d8", "#ebf5f0", "#ecdfd6", "#ece4dc", "#ece5da", "#ece5e1", "#ece67e", "#eceabe", "#ecf1ec", "#ecfcbd", "#ede1d1", "#ede4cf", "#ede9ad", "#edebe7", "#ededb7", "#edf1fe", "#eeaaff", "#eec5ce", "#eedfde", "#eee2c9", "#eee3dd", "#eee78e", "#eee7c8", "#eee7dd", "#eeeddf", "#eeeeaa", "#eef1ea", "#efa6aa", "#efc0fe", "#efc5b5", "#efdba7", "#efdbcd", "#efe0d4", "#efe1cd", "#efe7df", "#efecde", "#efecef", "#eff3f0", "#f0d5a8", "#f0e3c7", "#f0ead2", "#f0ead6", "#f0edd6", "#f0eddb", "#f0eee4", "#f0f8ff", "#f1d4c4", "#f1e4dc", "#f1e6de", "#f1e788", "#f1e7d2", "#f1ebda", "#f1ece2", "#f1f33f", "#f2a0a1", "#f2dea4", "#f2e2a4", "#f2ebdd", "#f2efe1", "#f2f0e6", "#f2f7fd", "#f3bbca", "#f3c775", "#f3dfd4", "#f3e2c6", "#f3e5ab", "#f3e5dc", "#f3ead2", "#f3eba5", "#f3f0e8", "#f4daf1", "#f4dbdc", "#f4dfcd", "#f4e8d1", "#f4eaf0", "#f4ebec", "#f4ecc2", "#f4ecdb", "#f4f0e6", "#f4f3e0", "#f4f5f0", "#f5cee6", "#f5d180", "#f5dcb4", "#f5e6d3", "#f5ebe1", "#f5ecd2", "#f5ece7", "#f6cefc", "#f6dbd8", "#f6e5db", "#f6e5f6", "#f6e6c5", "#f6eed5", "#f6f4f1", "#f7cee0", "#f7d560", "#f7e26b", "#f7e7ce", "#f7eacf", "#f7eecf", "#f7f1e2", "#f7f9e9", "#f8d0e7", "#f8de8d", "#f8deb8", "#f8ea97", "#f8f5e9", "#f8f6d8", "#f8f8ff", "#f9dbe2", "#f9e8e2", "#f9f3db", "#fabfe4", "#fad6e5", "#fada5f", "#fadbd7", "#fadfad", "#fae199", "#fae5bf", "#fae8ab", "#faf0be", "#faf0db", "#faf0e6", "#faf4d4", "#fbd8c9", "#fbdd7e", "#fbe0dc", "#fbe8ce", "#fbedb8", "#fbeee8", "#fcedc5", "#fcf0e5", "#fdd6e5", "#fdd7e4", "#fddc5c", "#fdee73", "#fdefe9", "#fdf5e6", "#fdfd96", "#fdfdfe", "#fdfff5", "#fed8b1", "#fee8d6", "#feedca", "#fef69e", "#fef6be", "#feff7f", "#fefffc", "#ffa180", "#ffb07c", "#ffb865", "#ffc0cb", "#ffc5cb", "#ffcc99", "#ffce81", "#ffcfdc", "#ffd1df", "#ffd5d1", "#ffd8b1", "#ffdadc", "#ffddee", "#ffdfbf", "#ffe2c7", "#ffe4c4", "#ffe5ad", "#ffe8e5", "#ffec89", "#ffedf8", "#ffeeaa", "#fff2de", "#fff2ef", "#fff4f2", "#fff5be", "#fff5ee", "#fff6d9", "#fff8c7", "#fff8d9", "#fffafa", "#fffdd8", "#fffe7a", "#fffedf", "#fffee4", "#ffff84", "#ffffbf", "#ffffc2", "#ffffdd", "#ffffe4", "#ffffff"
]

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Load quote JSON
with open(json_path, "r") as f:
    quotes = json.load(f)

# Gradient generator
def create_gradient_background(width, height, color_end_hex):
    color_end = tuple(int(color_end_hex.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    r1, g1, b1 = (255, 255, 255)  # White start
    r2, g2, b2 = color_end

    img = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    for y in range(height):
        ratio = y / height
        r = int(r1 * (1 - ratio) + r2 * ratio)
        g = int(g1 * (1 - ratio) + g2 * ratio)
        b = int(b1 * (1 - ratio) + b2 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    return img

# Process all unprocessed quotes
processed_any = False

for idx, q in enumerate(quotes):
    if q.get("processed", False):
        continue

    quote_text = f'“{q["quote"]}”'
    author_text = f"— {q['author']} —"
    wrapped_text = textwrap.fill(quote_text, width=max_chars)

    # Create gradient background
    pastel_color = random.choice(pastel_colors)
    image = create_gradient_background(image_width, image_height, pastel_color)
    draw = ImageDraw.Draw(image)

    # Load fonts
    try:
        lang = detect(q["quote"])
    except:
        lang = "en"  # Fallback

# Choose fonts based on language
    if lang == "hi":
        font_quote = ImageFont.truetype("fonts/ITFDevanagari.ttc", quote_font_size)
    else:
        font_quote = ImageFont.truetype(font_path_regular, quote_font_size)
    
    font_author = ImageFont.truetype(font_path_italic, author_font_size)

    # Measure quote
    quote_bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font_quote, align="center")
    quote_w = quote_bbox[2] - quote_bbox[0]
    quote_h = quote_bbox[3] - quote_bbox[1]

    # Measure author
    author_bbox = draw.textbbox((0, 0), author_text, font=font_author)
    author_w = author_bbox[2] - author_bbox[0]
    author_h = author_bbox[3] - author_bbox[1]

    total_text_height = quote_h + spacing + author_h
    center_x = image_width // 2
    center_y = image_height // 2

    # Draw top line
    line_y1 = center_y - total_text_height // 2 - line_margin
    draw.line([(150, line_y1), (image_width - 150, line_y1)], fill=text_color, width=line_thickness)
    draw.ellipse([(140 - dot_radius, line_y1 - dot_radius), (140 + dot_radius, line_y1 + dot_radius)], fill=text_color)
    draw.rectangle([(150, line_y1 - 2), (150 + accent_length, line_y1 + 2)], fill=accent_color)

    # Draw bottom line
    line_y2 = center_y + total_text_height // 2 + line_margin
    draw.line([(150, line_y2), (image_width - 150, line_y2)], fill=text_color, width=line_thickness)
    draw.ellipse([(image_width - 140 - dot_radius, line_y2 - dot_radius),
                  (image_width - 140 + dot_radius, line_y2 + dot_radius)], fill=text_color)
    draw.rectangle([(image_width - 150 - accent_length, line_y2 - 2),
                    (image_width - 150, line_y2 + 2)], fill=accent_color)

    # Draw quote text
    quote_x = center_x - quote_w // 2
    quote_y = center_y - total_text_height // 2
    draw.multiline_text((quote_x, quote_y), wrapped_text, fill=text_color, font=font_quote, align="center")

    # Draw author text
    author_x = center_x - author_w // 2
    author_y = quote_y + quote_h + spacing
    draw.text((author_x, author_y), author_text, fill=text_color, font=font_author)

    # Save image
    output_file = os.path.join(output_dir, f"wallpaper_{idx+1}.png")
    image.save(output_file)
    print(f"✅ Saved: {output_file}")

    # Mark quote as processed
    quotes[idx]["processed"] = True
    processed_any = True

# Save updated JSON
if processed_any:
    with open(json_path, "w") as f:
        json.dump(quotes, f, indent=2)
    print("✅ All unprocessed quotes have been generated and marked.")
else:
    print("🎉 No unprocessed quotes left.")
