# Nugget Mass Flasher Tool
Cross-platform mass flashing tool for the USB Nugget & WiFi Nugget.  

## How to Use
1. Install [Python3](https://www.python.org/downloads/)
2. Install `esptool.py` from a terminal:
  ```
  pip install esptool
  ```
3. Place all Nuggets in DFU mode
4. Run the flasher to flash the test code:
  ```
  python3 flash.py
  ```
5. Replace flash.py with the firmware you want to update with, and rename it to flasher.py
6. Run the flasher again to flash your firmware update code:
  ```
  python3 flash.py
  ```
