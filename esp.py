from subprocess import Popen, PIPE
import subprocess
import glob
import esptool
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
        
        if ("303A:0002" in hwid):
                print("ESP32-S2 found on port: {}".format(port))
                proc = subprocess.Popen(["esptool.py --port {} --after no_reset write_flash 0x0 tester.bin".format(port)],shell=True)
                
                # esptool.main(flash_cmd)
print("###################################")
print("FINISHED FLASHING")
print("###################################")
