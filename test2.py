from bluepy import Scanner, btle

b1 = btle.Peripheral("90:e2:02:b1:96:c3")

print(b1.rssi)
