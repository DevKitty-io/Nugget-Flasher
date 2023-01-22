USB_NUGGET_FILE_NAME=USB-Nugget.bin

usb-nugget-latest: flasher-deps download-latest-usb-nugget
	python3 flash.py $(USB_NUGGET_FILE_NAME)

tester: flasher-deps
	python3 flash.py tester.bin

download-latest-usb-nugget: wget
	# download latest version, or don't if we already have it
	wget --timestamping 'https://github.com/HakCat-Tech/USB-Nugget/releases/latest/download/$(USB_NUGGET_FILE_NAME)'

flasher-deps:
	@which python3 > /dev/null || echo 'python3 not installed'
	@which esptool.py > /dev/null || echo 'esptool.py not installed. Run `pip3 install esptool`.'

wget:
	@which wget > /dev/null || echo 'wget not installed'

