from bluepy.btle import Scanner

while True:
        try:
                ble_list = Scanner().scan(10.0)
                for dev in ble_list:
                        if dev.addr == "90:e2:02:b1:96:c3":
                                print("mac: {} ; rssi: {}".format(dev.addr, dev.rssi))
                        elif dev.addr == "d0:b5:c2:96:6b:f3":
                                print("mac: {} ; rssi: {}".format(dev.addr, dev.rssi))
                        else:
                                pass 
        except:
                raise Exception("Error occured")
