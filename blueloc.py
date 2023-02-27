from bluepy.btle import Scanner

while True:
        try:
        #10.0 sec scanning
                ble_list = Scanner().scan(10.0)
                for dev in ble_list:
           # print("rssi: {} ; mac: {}".format(dev.rssi,dev.addr))
                        if dev.addr == "90:e2:02:b1:96:c3":
                                print("mac: ; rssi: ".format(dev.addr, dev.rssi))
        except:
                raise Exception("Error occured")
