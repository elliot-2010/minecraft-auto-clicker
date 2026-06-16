# 🖱️ Minecraft Auto Clicker

A lightweight auto-clicker for Minecraft built with Python and `pynput`, toggled with a single mouse button — capped at 20 clicks per second, matching Minecraft's tick rate.

---

## 🚀 Features

- Toggle auto-clicking on/off with one mouse button press
- Runs at 20 clicks per second — matches Minecraft's internal tick rate (clicking faster has no extra effect)
- Runs in the background — works system-wide, including inside the game
- Built with multithreading — clicking and input listening happen simultaneously without blocking each other

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

## 🛠️ Usage

```bash
python3 ACM.py
```

Press your mouse's side button (default mapped to `Button.button9`) to toggle the auto-clicker on and off.

```
Auto-click: ON
Auto-click: OFF
```

> ⚠️ On Wayland/GNOME, the first simulated click may trigger a "Remote Desktop" permission prompt. Click **Share** to allow it — this only happens once per session.

---

## ⚙️ Customization

To change which button toggles the clicker, find your button's name by running this snippet and pressing it:

```python
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    print(f"Button: {button}, Pressed: {pressed}")

with Listener(on_click=on_click) as listener:
    listener.join()
```

Then update `ACM.py`:
```python
if button == Button.button9 and pressed:
```

To change the click speed, adjust the sleep value (clicks per second = `1 / value`):
```python
time.sleep(1/20)   # 20 clicks per second
```

---

## 🗂️ Project Structure

```
minecraft-auto-clicker/
│
├── ACM.py        # Main script — click loop + mouse listener
└── README.md
```

---

## 🧠 Concepts Used

- Threading — running the click loop and input listener concurrently
- pynput — simulating mouse clicks and listening to system-wide input events
- Global state — toggling a shared `clicking` flag between threads

---

## ⚠️ Disclaimer

This tool simulates physical mouse clicks for personal, single-player use. Using auto-clickers on multiplayer servers may violate their rules and could result in a ban. Use responsibly.

---

## 👤 Author

**Elliot** — 15 y/o developer from Isfahan, Linux enthusiast, building real tools while learning Python.

---

## 📜 License

MIT
