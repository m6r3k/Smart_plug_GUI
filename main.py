from tkinter import *
import asyncio
from kasa import Discover
from kasa import SmartPlug

def turn_on_button():
    plug = SmartPlug("192.168.0.189")
    asyncio.run(plug.update())
    asyncio.run(plug.turn_on())


def turn_off_button():
    plug = SmartPlug("192.168.0.189")
    asyncio.run(plug.update())
    asyncio.run(plug.turn_off())


root = Tk()
root.geometry('300x200')
root.title("Smart Plug")
window_photo = PhotoImage(file = 'icon.png')
root.iconphoto(False, window_photo)


my_label = Label(root, text="Ovládanie TP-link smart zásuvky HS110")
my_label.pack(pady=10)


my_button = Button(root, text="ON", command=turn_on_button, width=10)
my_button.pack(pady=10)

my_button2 = Button(root, text="OFF", command=turn_off_button, width=10)
my_button2.pack(pady=10)

root.mainloop()
