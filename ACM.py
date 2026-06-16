from pynput.mouse import Controller, Listener, Button
import threading
import time

mouse = Controller()
clicking = False

def click_loop():
    while True:
        if clicking:
            mouse.click(Button.left)
            time.sleep(1/20)   # 20 کلیک در ثانیه

def on_click(x, y, button, pressed):
    global clicking
    if button == Button.button9 and pressed:
        clicking = not clicking   # toggle: روشن/خاموش
        print("Auto-click:", "ON" if clicking else "OFF")

# Thread برای کلیک کردن
t = threading.Thread(target=click_loop, daemon=True)
t.start()

# Listener برای دکمه موس
with Listener(on_click=on_click) as listener:
    listener.join()