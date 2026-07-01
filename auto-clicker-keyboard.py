from pynput.mouse import Controller, Button
from pynput.keyboard import Key, Listener
import threading
import time



mouse = Controller()
clicking_left = False
clicking_right = False
def click_loop():
    while True:
        if clicking_left:
            mouse.click(Button.left)
            time.sleep(1/20)   # 20 کلیک در ثانیه
        elif clicking_right:
            mouse.click(Button.right)
            time.sleep(1/20)
        else:
            time.sleep(0.01)
def on_press(key):
    global clicking_right, clicking_left
    if key == Key.caps_lock:
        clicking_left = not clicking_left   # toggle: روشن/خاموش
        print("Auto-click-left:", "ON" if clicking_left else "OFF")
    elif key == Key.f6:
        clicking_right = not clicking_right
        print("Auto-click:-right", "ON" if clicking_right else "OFF")



# Thread برای کلیک کردن
t = threading.Thread(target=click_loop, daemon=True)
t.start()


with Listener(on_press=on_press) as listener:
    listener.join()