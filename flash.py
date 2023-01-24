from subprocess import Popen, PIPE
import subprocess
import glob
import esptool
import serial.tools.list_ports
import sys

if (len(sys.argv) != 2):
        print("Usage: {} <binary>".format(sys.argv[0]))
        exit(1)
binary = sys.argv[1]

ports = serial.tools.list_ports.comports()
print("Found {} devices to flash".format(len(ports)))

processes = []
for port, desc, hwid in sorted(ports):
        
        if ("303A:0002" in hwid):
                print("ESP32-S2 found on port: {}".format(port))
                proc = subprocess.Popen(["esptool.py --port {} --after no_reset write_flash 0x0 {}".format(port, binary)],shell=True)
                processes.append(proc)
for p in processes:
        p.wait()
print("###################################")
print("FINISHED FLASHING")
print("###################################")
