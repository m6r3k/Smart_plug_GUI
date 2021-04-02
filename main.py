from tkinter import *
import asyncio
from smartplug import SmartPlug
from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

device = config_object["DEVICECONFIG"]


State1 = 0
State2 = 0
State3 = 0
plugs = int(device['quantity'])


def power_on(ip):
    plug = SmartPlug(ip)
    asyncio.run(plug.update())
    asyncio.run(plug.turn_on())


def power_off(ip):
    plug = SmartPlug(ip)
    asyncio.run(plug.update())
    asyncio.run(plug.turn_off())


def button1(event):
    global State1

    if State1 == 1:
        winbtn1.config(image=btnoff)
        power_off(device["IP_SmartPlug1"])
        State1 = 0
    else:
        winbtn1.config(image=btnon)
        power_on(device["IP_SmartPlug1"])
        State1 = 1


def button2(event):
    global State2

    if State2 == 1:
        winbtn2.config(image=btnoff)
        power_off(device["IP_SmartPlug2"])
        State2 = 0
    else:
        winbtn2.config(image=btnon)
        power_on(device["IP_SmartPlug2"])
        State2 = 1


def button3(event):
    global State3

    if State3 == 1:
        winbtn3.config(image=btnoff)
        power_off(device["IP_SmartPlug3"])
        State3 = 0
    else:
        winbtn3.config(image=btnon)
        power_on(device["IP_SmartPlug3"])
        State3 = 1


# GUI

app = Tk()
app.title("SmartPlug GUI")
app.geometry("250x300")
app.resizable(0, 0)
btnoff = PhotoImage(file="icons/off.png")
btnon = PhotoImage(file="icons/on.png")

# 1st button

relay1_label = Label(app, font="Consolas 12", text=(device["name_SmartPlug1"]))
winbtn1 = Label(app, image=btnoff)
winbtn1.bind("<Button-1>", button1)
winbtn1.pack()
relay1_label.pack()
winbtn1.place(x=150, y=100)
relay1_label.place(x=50, y=105)

# Startup state
if State1 == 0:
    winbtn1.config(image=btnoff)
else:
    winbtn1.config(image=btnon)

# 2nd button
if plugs >= 2:
    relay2_label = Label(app, font="Consolas 12", text=(device["name_SmartPlug2"]))
    winbtn2 = Label(app, image=btnoff)
    winbtn2.bind("<Button-1>", button2)
    winbtn2.pack()
    relay2_label.pack()
    winbtn2.place(x=150, y=150)
    relay2_label.place(x=50, y=155)

    # Startup state
    if State2 == 0:
        winbtn2.config(image=btnoff)
    else:
        winbtn2.config(image=btnon)

# 3th button
if plugs >= 3:
    relay3_label = Label(app, font="Consolas 12", text=(device["name_SmartPlug3"]))
    winbtn3 = Label(app, image=btnoff)
    winbtn3.bind("<Button-1>", button2)
    winbtn3.pack()
    relay3_label.pack()
    winbtn3.place(x=150, y=200)
    relay3_label.place(x=50, y=205)

    # Startup state
    if State3 == 0:
        winbtn3.config(image=btnoff)
    else:
        winbtn3.config(image=btnon)

app.mainloop()
