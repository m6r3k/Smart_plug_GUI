from tkinter import *
import asyncio
from smartplug import SmartPlug
from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

device = config_object["DEVICECONFIG"]
debug = config_object["DEBUG"]

State1 = 0
State2 = 0


def button1(event):
    global State1

    if State1 == 1:
        winbtn1.config(image=btnoff)
        plug = SmartPlug(device["host"])
        asyncio.run(plug.update())
        asyncio.run(plug.turn_off())
        State1 = 0
    else:
        winbtn1.config(image=btnon)
        plug = SmartPlug(device["host"])
        asyncio.run(plug.update())
        asyncio.run(plug.turn_on())
        State1 = 1


def button2(event):
    global State2
    if State2 == 1:
        winbtn2.config(image=btnoff)
        print("tralala off")
        State2 = 0
    else:
        winbtn2.config(image=btnon)
        print("tralala on")
        State2 = 1


# GUI

app = Tk()
app.title("SmartPlug GUI")
app.geometry("250x300")
app.resizable(0, 0)

relay1_label = Label(app, font="Consolas 12", text="SmartPlug")
relay2_label = Label(app, font="Consolas 12", text="Tralala")

btnoff = PhotoImage(file="icons/off.png")
btnon = PhotoImage(file="icons/on.png")

winbtn1 = Label(app, image=btnoff)
winbtn1.bind("<Button-1>", button1)
winbtn1.pack()

winbtn2 = Label(app, image=btnoff)
winbtn2.bind("<Button-1>", button2)
winbtn2.pack()

relay1_label.pack()
relay2_label.pack()

winbtn1.place(x=150, y=100)
winbtn2.place(x=150, y=150)

relay1_label.place(x=50, y=105)
relay2_label.place(x=50, y=155)

# Correct startup
if State1 == 0:
    winbtn1.config(image=btnoff)
else:
    winbtn1.config(image=btnon)

if State2 == 0:
    winbtn2.config(image=btnoff)
else:
    winbtn2.config(image=btnon)

app.mainloop()
