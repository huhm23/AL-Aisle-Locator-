from bluepy.btle import Scanner, DefaultDelegate

class bluetooth(DefaultDelegate): 
    def _init_(self):
        DefaultDelegate.__init__(self)
    def scan_for_devices():
        while True:
            try:
                #10.0 sec scanning
                ble_list = Scanner().scan(10.0)
                for dev in ble_list:
                    print("rssi: {} ; mac: {}".format(dev.rssi,dev.addr))
            except:
                raise Exception("Error occured")
