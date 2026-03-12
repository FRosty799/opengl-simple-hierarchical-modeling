# OpenGL Simple Hierarchical Modeling

A minimal Python OpenGL demo that demonstrates hierarchical modeling using the fixed-function matrix stack (glPushMatrix/glPopMatrix) to draw a simple furniture scene (table, chair, and fruit basket).

## ✅ What it shows

- A **ground plane** (floor).
- A **table** (top + two legs).
- A **fruit basket** placed on the table.
- A **chair** positioned nearby.
- Uses matrix stack transformations to build the scene hierarchically (child objects follow parent transforms).

## 🧰 Requirements

- **Python 3.14+**
- Packages:
  - `pygame-ce`
  - `PyOpenGL`
  - `numpy` (not directly used in this file, but commonly required for OpenGL work)
  - `Pillow` (not used currently, but referenced in the original requirements comment)
  - `tmx` (not used currently, but referenced in the original requirements comment)

## 🚀 Install dependencies

```bash
pip install pygame-ce PyOpenGL numpy Pillow tmx
```

## ▶️ Run

From the folder containing `grafkom simple hirarki model.py`:

```bash
python "grafkom simple hirarki model.py"
```

## ⌨️ Controls

- **ESC** or window close button: exit the program

## 🧩 Notes

- This demo uses legacy OpenGL (immediate mode + matrix stack). It is intended for learning hierarchical transformations, not modern shader-based rendering.
- The scene is strictly 2D (orthographic-like) and uses `glVertex2f` for simplicity.
