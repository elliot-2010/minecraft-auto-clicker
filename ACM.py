from pynput.mouse import Controller, Listener, Button
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
        if clicking_right:
            mouse.click(Button.right)
            time.sleep(1/20)

def on_click(x, y, button, pressed):
    global clicking_left
    global clicking_right
    if button == Button.button9 and pressed:
        clicking_left = not clicking_left   # toggle: روشن/خاموش
        print("Auto-click-left:", "ON" if clicking_left else "OFF")
    if button == Button.button8 and  pressed:
        clicking_right = not clicking_right
        print("Auto-click:-right", "ON" if clicking_right else "OFF")

    

# Thread برای کلیک کردن
t = threading.Thread(target=click_loop, daemon=True)
t.start()

# Listener برای دکمه موس
with Listener(on_click=on_click) as listener:
    listener.join()