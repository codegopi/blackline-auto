import pyautogui as pg
import time

time.sleep(1)
# if pg.locateOnScreen("name.png"):
#     z = pg.locateOnScreen("name.png")
    
#     print(z.x)

print(pg.position())

for i in range(10):
    time.sleep(2)
    pg.click(332,405)
    pg.write("1")
    pg.hotkey("enter")
    pg.hotkey("f8")
    pg.hotkey("enter")
    pg.hotkey("enter")
    time.sleep(6)


# import pyautogui as pg
# import tkinter as tk
# import pandas as pd
# import xlwings as xw


# data = pd.read_excel("je.xlsx")
# #print(data.iloc[0,1])
# i = 25

# ws = xw.Book(".//file//" + data.iloc[i,4] + ".xlsx").sheets["ManJv_EUR (2)"]
# #print(type(ws.range("E" + str(16)).value))
# print(ws.range("A20").value )             