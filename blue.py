from bluepy.btle import Scanner

while True:
        try:
        #10.0 sec scanning
                ble_list = Scanner().scan(10.0, passive = True)
                MR_list = []
                for dev in ble_list:
                        if dev.addr == "90:e2:02:b1:96:c3":
                                MR_list.append("mac: {} ; rssi: {}".format(dev.addr, dev.rssi))
                                print(MR_list)
        except:
                raise Exception("Error occured")
                
#print(MR_list)
