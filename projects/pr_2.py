import keyboard as key
import pyautogui as auto

start_button = '9'
pause_button = '0'
end_button = '8'
automatic_button = '7'

while True:
    if key.is_pressed(automatic_button):
        auto.tripleClick()

    if key.is_pressed(start_button):
        while True:
            auto.tripleClick()
            if key.is_pressed(pause_button):
                break

    elif key.is_pressed(end_button):
        break
