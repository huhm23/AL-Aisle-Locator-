from at09 import bluetooth
from bluepy.btle import Scanner

def scan_for_devices():
        while True:
                try:
                        ble_list = Scanner().scan(10.0)
                        for dev in ble_list:
                                print("mac: {}; rssi: {}".format(dev.addr,dev.rssi))
                except:
                        raise Exception("Error occured")
scan_for_devices()
                

