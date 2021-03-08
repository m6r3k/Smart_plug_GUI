from tkinter import *
import asyncio
from kasa import SmartPlug
from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

device = config_object["DEVICECONFIG"]
debug = config_object["DEBUG"]


def turn_on_button():
    if (debug["DEBUG"]) == "TRUE":
        print("DEVICE ON")
    else:
        plug = SmartPlug(device["host"])
        asyncio.run(plug.update())
        asyncio.run(plug.turn_on())


def turn_off_button():
    if (debug["DEBUG"]) == "TRUE":
        print("DEVICE OFF")
    else:
        plug = SmartPlug(device["host"])
        asyncio.run(plug.update())
        asyncio.run(plug.turn_off())


root = Tk()
root.geometry('300x200')
root.title("Smart Plug")
window_photo = PhotoImage(file='icons/icon.png')
root.iconphoto(False, window_photo)

my_label = Label(root, text="Ovládanie TP-link smart zásuvky HS110")
my_label.pack(pady=10)

my_button = Button(root, text="ON", command=turn_on_button, width=10)
my_button.pack(pady=10)

my_button2 = Button(root, text="OFF", command=turn_off_button, width=10)
my_button2.pack(pady=10)

root.mainloop()
