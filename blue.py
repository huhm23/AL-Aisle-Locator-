from bluepy.btle import Scanner

while True:
        ble_list = Scanner().scan(10.0, passive = True)
        try:
                MR_list = []
                for dev in ble_list:
                        if dev.addr == "90:e2:02:b1:96:c3":
                                MR_list.append("mac: {} ; rssi: {}".format(dev.addr, dev.rssi))
                        elif dev.addr == "d0:b5:c2:96:6b:f3":
                                MR_list.append("mac: {} ; rssi: {}".format(dev.addr, dev.rssi))
                        print(MR_list)
        except:
                raise Exception("Error occured")
                
#print(MR_list)
