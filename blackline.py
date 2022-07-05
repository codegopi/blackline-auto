import pyautogui
import win32api, win32con
import time
import keyboard

#   print(pyautogui.position())
#pyautogui.displayMousePosition()

pos1 = [599, 853]
timePos = [567, 881]
subbut = [924, 715]

position = {601: 855, 692: 862}

rgb = [255, 252, 249]


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


    
def run_black():
    #a = 0
    time.sleep(5)
    #while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(139, 414)[0] == 255:
        #pixel()[0, 1, 2] = [r, g, b]
        click(139, 414) 
        #a = 1
        time.sleep(3)
        #while keyboard.is_pressed('q') == False:
        if pyautogui.locateOnScreen('min.png') != None:
            print("Hello")
            b  = pyautogui.locateOnScreen('min.png')
            time.sleep(5)
            click(b[0]+40, b[1]+40)
            pyautogui.press('backspace')
            pyautogui.write("15")
            time.sleep(2)
            #pyautogui.scroll(50)
            pyautogui.press("tab")
            pyautogui.press('pagedown')
            time.sleep(2)
            #win32api.SetCursorPos((891, 715))
            click(891, 715)
            #break
            time.sleep(5)

for i  in range(15):
    run_black()
#time.sleep(3)
#b  = pyautogui.locateOnScreen('min.png')
#print(b[0] + 5)


