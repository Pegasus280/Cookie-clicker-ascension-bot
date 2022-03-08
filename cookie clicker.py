import pyautogui
import time

time.sleep(3)

while True:
    
    # purchase all upgrades
    time.sleep(1.3)
    pyautogui.moveTo(1750, 150, duration = 0)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()


    # scroll down to buy a fractal engine
    pyautogui.moveTo(1750, 840, duration = 0)
    pyautogui.scroll(-430)
    time.sleep(0.1)
    pyautogui.click()
    pyautogui.moveTo(1750, 900, duration = 0)
    pyautogui.click()


    # buys 1 idleverse, then 100 of each last four
    pyautogui.moveTo(1750, 1030, duration = 0)
    pyautogui.click()
    pyautogui.keyDown('shift')
    pyautogui.doubleClick()
    pyautogui.moveTo(1750, 970, duration = 0)
    pyautogui.doubleClick()
    pyautogui.click()
    pyautogui.moveTo(1750, 900, duration = 0)
    pyautogui.doubleClick()
    pyautogui.click()
    pyautogui.moveTo(1750, 840, duration = 0)
    pyautogui.doubleClick()
    pyautogui.click()
    pyautogui.keyUp('shift')

    # buys the upgrades again
    time.sleep(0.7)
    pyautogui.scroll(430)
    pyautogui.moveTo(1750, 150, duration = 0)
    pyautogui.click()
    time.sleep(0.9)
    pyautogui.click()

    # buys 100 of each last four again
    time.sleep(0.6)
    pyautogui.scroll(-430)
    pyautogui.keyDown('shift')
    pyautogui.moveTo(1750, 1030, duration = 0)
    pyautogui.doubleClick()
    pyautogui.moveTo(1750, 955, duration = 0)
    pyautogui.doubleClick()
    pyautogui.click()
    pyautogui.moveTo(1750, 900, duration = 0)
    pyautogui.doubleClick()
    pyautogui.click()
    pyautogui.moveTo(1750, 840, duration = 0)
    pyautogui.doubleClick()
    pyautogui.click()
    pyautogui.keyUp('shift')
    time.sleep(0.3)

    # buys the upgrades again
    pyautogui.scroll(430)
    pyautogui.moveTo(1750, 150, duration = 0)
    pyautogui.click()
    time.sleep(0.6)
    pyautogui.click()
    time.sleep(0.7)

    # reincarnation
    time.sleep(0.2)
    pyautogui.moveTo(1550, 80, duration = 0)
    pyautogui.click()
    pyautogui.moveTo(860, 610, duration = 0)
    pyautogui.click()
    time.sleep(5.3)
    pyautogui.moveTo(945, 110, duration = 0)
    pyautogui.click()
    pyautogui.moveTo(945, 560, duration = 0)
    pyautogui.click()
