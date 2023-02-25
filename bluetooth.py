from bluepy.btle import Scanner, DefaultDelegate

class bluetooth(DefaultDelegate): 
    def _init_(self):
        DefaultDelegate.__init__(self)
    def scan_for_devices():
            try:
                ble_list = Scanner().scan(10.0)
            except:
                raise Exception("Error occured")
