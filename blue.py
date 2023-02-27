from bluepy.btle import Scanner

while True:
        try:
                ble_list = Scanner().scan(10.0)
                for dev in ble_list:
                        print(dev)
                #print(ble_list)
