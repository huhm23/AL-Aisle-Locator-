from bluepy.btle import Scanner

while True:
        try:
                ble_list = Scanner().scan(5.0)
                MR_list = []
                for dev in ble_list:
                        MR_list.append("mac: {} ; rssi: {}".format(dev.addr, dev.rssi))
print(MR_list)
