import asyncio
from kasa import Discover
from kasa import SmartPlug

# Print All data about smart device
found_devices = asyncio.run(Discover.discover(target="192.168.0.189"))
for addr, dev in found_devices.items():
    asyncio.run(dev.update())
    print(f"{addr} >> {dev}")


# print SmartPlug Alias
plug = SmartPlug("192.168.0.189")
asyncio.run(plug.update())
print(plug.alias)

# Smart Plug Turn on/off
asyncio.run(plug.turn_off())

# Smart Plug LED on/off - True/False
asyncio.run(plug.set_led(True))
