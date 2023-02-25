from at09 import bluetooth

def scan_for_devices():
        try:
            ble_list = Scanner().scan(10.0)
            for dev in ble_list:
                print("rssi: {} ; mac: {}".format(dev.rssi,dev.addr))
        except:
            raise Exception("Error occured")
