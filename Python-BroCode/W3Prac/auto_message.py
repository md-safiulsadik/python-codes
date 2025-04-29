import pyautogui
import time

time.sleep(3)
for _ in range(10):
    pyautogui.typewrite("Hello")
    pyautogui.press("enter")


# while True:
#     x, y = pyautogui.position()
#     print(f"{x}, {y}")
#     time.sleep(0.2)



# time.sleep(10)

# for _ in range(20):
#     pyautogui.press('delete')
#     pyautogui.press('down')
#     pyautogui.click(952, 634)
#     pyautogui.press('down')
#     time.sleep(0.5)
