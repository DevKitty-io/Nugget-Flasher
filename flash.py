import os, subprocess
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
portsInUse = []


for port, desc, hwid in sorted(ports):
	
	if (desc == "ESP32-S2" and (port not in portsInUse) ):
		portsInUse.append(port)
		print("------------------------------")
		print("Found ESP32-S2!")
		print("Erasing and flashing board...")
		os.system('gnome-terminal --working-directory ~/Projects/Nugget/firmware/tools/Nugget-Flasher/ -e \"esptool.py --port {} --chip esp32s2 write_flash 0x0 v1.1-beta-USB-Nugget.bin\"'.format(port))
		
