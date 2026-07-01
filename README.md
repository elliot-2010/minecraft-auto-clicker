# 🖱️ Minecraft Auto Clicker

A lightweight Minecraft auto-clicker built with Python and `pynput`. It supports both **gaming mice with side buttons** and **standard keyboards**, making it easy to use on almost any setup.

---

## 🚀 Features

* Two control methods:

  * 🖱️ Gaming mouse side buttons
  * ⌨️ Keyboard hotkeys
* Runs at **20 clicks per second**, matching Minecraft's internal tick rate
* Runs in the background — works system-wide, including inside the game
* Built with multithreading for smooth, non-blocking input handling
* Lightweight and easy to customize

---

## 📦 Installation

```bash
# Clone the repository
git clone git@github.com:elliot-2010/minecraft-auto-clicker.git
cd minecraft-auto-clicker

# Install dependencies
pip install pynput --break-system-packages
```

---

# 🖱️ Gaming Mouse Version

Run:

```bash
python3 ACM.py
```

### Default Controls

| Button           | Action                  |
| ---------------- | ----------------------- |
| `Button.button9` | Toggle left auto-click  |
| `Button.button8` | Toggle right auto-click |

Example output:

```
Auto-click-left: ON
Auto-click-left: OFF

Auto-click-right: ON
Auto-click-right: OFF
```

> ⚠️ On Wayland/GNOME, the first simulated click may trigger a **Remote Desktop** permission prompt. Click **Share** to allow it. This only happens once per session.

---

# ⌨️ Keyboard Version

If your mouse does not have programmable side buttons, use:

```bash
python3 auto-clicker-keyboard.py
```

### Default Hotkeys

| Key         | Action                  |
| ----------- | ----------------------- |
| `Caps Lock` | Toggle left auto-click  |
| `F6`        | Toggle right auto-click |

Example output:

```
Auto-click-left: ON
Auto-click-left: OFF

Auto-click-right: ON
Auto-click-right: OFF
```

---

## 🔍 Finding Your Mouse Button

Different gaming mice may use different button numbers.

Run:

```bash
python3 find_button.py
```

Then press your side button.

Example output:

```
Button.button8
Button.button9
```

Update `ACM.py` accordingly:

```python
if button == Button.button9 and pressed:
```

---

## ⚙️ Customization

### Change Click Speed

The click speed is controlled by:

```python
time.sleep(1/20)
```

Examples:

```python
time.sleep(1/10)   # 10 CPS
time.sleep(1/20)   # 20 CPS
time.sleep(1/30)   # 30 CPS
```

> Although higher values are possible, Minecraft generally processes clicks at its tick rate, so increasing CPS may not provide any practical benefit.

---

## 🗂️ Project Structure

```
minecraft-auto-clicker/
│
├── ACM.py                    # Gaming mouse version
├── auto-clicker-keyboard.py  # Keyboard version
├── find_button.py            # Detect mouse side buttons
└── README.md
```

---

## 🧠 Concepts Used

* Threading
* `pynput`
* Mouse and keyboard event listeners
* Mouse click simulation
* Global state shared between threads

---

## ⚠️ Disclaimer

This tool simulates physical mouse clicks for personal use. Using auto-clickers on multiplayer servers may violate server rules and could result in penalties or a ban. Use responsibly and only where permitted.

---

## 👤 Author

**Elliot** — 15-year-old developer from Iran, Linux enthusiast, building real tools while learning Python.

---

## 📜 License

MIT License
