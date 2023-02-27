from bluepy.btle import Scanner

while True:
        try:
        #10.0 sec scanning
                ble_list = Scanner().scan(10.0)
                for dev in ble_list:
           # print("rssi: {} ; mac: {}".format(dev.rssi,dev.addr))
                        if dev.addr == "90:E2:02:B1:96:C3":
                                print("mac: ; rssi: ".format(dev.addr, dev.rssi))
        except:
                raise Exception("Error occured")
