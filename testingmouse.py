import pyautogui

# moves the mouse around the screen
for i in range(10):
     pyautogui.moveTo(10,19,0.25)
     pyautogui.moveTo(1270,8,0.25)
     pyautogui.moveTo(1273,762,0.25)
     pyautogui.moveTo(34,778,0.25)

# Moves mouse to a specific spot and clicks 
pyautogui.click(600,400)

# Runs built-in MouseInfo program that helps you plan mouse movements
pyautogui.mouseInfo()

