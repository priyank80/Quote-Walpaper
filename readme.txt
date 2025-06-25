# Quote Wallpaper Generator

Automatically generate beautiful quote wallpapers with dynamic gradient backgrounds and elegant typography.

---

## 📆 Features

* ✨ **Random pastel gradient backgrounds** (blending white with soft colors)
* 🖊️ **Dynamic quote & author placement** using smart text wrapping
* 🎨 **Upper & lower accent lines** for added visual style
* ❓ Automatically avoids regenerating already processed quotes
* 📁 Outputs wallpapers in a clean, organized folder (`wallpapers/`)

---

## 🔧 Setup Instructions

### 1. Install Dependencies

```bash
pip install pillow
```

### 2. Folder Structure

```
project-root/
|
├── data/
│   └── quotes.json           # Your quotes here
|
├── fonts/
│   ├── Roboto-Regular.ttf
│   └── Roboto-Italic.ttf
|
├── wallpapers/              # Auto-generated output
|
└── GenerateWallpaper.py     # Main script
```

### 3. `quotes.json` Format

```json
[
  {
    "quote": "Life is 10% what happens to us and 90% how we react to it.",
    "author": "Charles R. Swindoll"
  },
  {
    "quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "author": "Winston Churchill"
  }
]
```

> ⚠️ The script automatically adds `"processed": true` after creating each wallpaper.

---

## 🔄 Running the Script

```bash
python GenerateWallpaper.py
```

Wallpapers will be saved as `wallpapers/wallpaper_1.png`, `wallpaper_2.png`, etc.

---

## 📚 License

This project is open-source under the MIT License.

---

## 📈 Example Output

![Sample Wallpaper](wallpapers/wallpaper_1.png)

---

## 🎓 Acknowledgements

* Fonts: [Roboto](https://fonts.google.com/specimen/Roboto)
* Color palettes: Inspired by [pastel color lists](https://www.color-hex.com/)
* Image manipulation: [Pillow (PIL)](https://python-pillow.org/)
