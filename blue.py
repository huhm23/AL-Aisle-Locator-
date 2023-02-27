from bluepy.btle import Scanner

while True:
        try:
                ble_list = Scanner().scan(10.0)
                print(ble_list)
