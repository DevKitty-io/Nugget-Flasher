# Nugget Mass Flasher Tool
Cross-platform mass flashing tool for the USB Nugget & WiFi Nugget.  

## How to Use

To flash latest USB Nugget software, place all Nuggets in DFU mode and then run
`make usb-nugget-latest`. The latest software version will be installed
automatically.

To flash any other binary,
`python3 flash.py <binary>`


If you run into any problems, check that `make flasher-deps` doesn't report any
missing dependencies. If you think it's a problem with your binary, you can
flash our testing binary with either `make tester` or `python3 flash.py
tester.bin`
