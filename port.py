from subprocess import Popen, PIPE
import subprocess
import glob
import esptool
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

flash_cmd = ['--baud', '460800', 'write_flash', '0', 'tester.bin']

# cmds_list = [["touch ~/Desktop/",port] for port,desc,hwid in sorted(ports)]

for port, desc, hwid in sorted(ports):
        print(port)
        # if ("303A:0002" in hwid):
        #         print("ESP32-S2 found on port: {}".format(port))
        # subprocess.run(["touch ~/Desktop/{}.txt".format(desc)],shell=True)
                # esptool.main(flash_cmd)