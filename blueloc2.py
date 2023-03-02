from bluepy.btle import Scanner

#B1: 90:e2:02:b1:96:c3
#B2: d0:b5:c2:96:6b:f3
#B3: 78:a5:04:90:82:69
#B4: ec:11:27:54:4b:42
#B5: b4:99:4c:79:cc:a1

# create list for my bluetooth devices
my_list = []
# create list for devices that are scanned
ble_list = Scanner().scan(10.0)

# if the device MAC address equals the MAC address of my bluetooth devices the put them in my_list
try:
  for dev in ble_list:
    if dev.addr == "90:e2:02:b1:96:c3" or dev.addr == "d0:b5:c2:96:6b:f3" or dev.addr == "78:a5:04:90:82:69" \
    or dev.addr == "ec:11:27:54:4b:42" or dev.addr == "b4:99:4c:79:cc:a1":
      my_list.append(dev)
except:
  raise Exception("Error occured")

# max (never can reach) number for the RSSI
max_num = -10000
# max (never can reach) number for the index
max_index = -1

# check which index has the lowest RSSI number:
for i in range(len(my_list)):
  if my_list[i].rssi >= max_num: 
    max_num = my_list[i].rssi
    max_index = i

# compare the address to the bluetooth addresses and print the statement of the one you are near
if my_list[max_index].addr == "90:e2:02:b1:96:c3":
  print("You are near bluetooth 1")
elif my_list[max_index].addr == "d0:b5:c2:96:6b:f3":
  print("You are near bluetooth 2")
elif my_list[max_index].addr == "78:a5:04:90:82:69":
  print("You are near bluetooth 3")
elif my_list[max_index].addr == "ec:11:27:54:4b:42":
  print("You are near bluetooth 4")
elif my_list[max_index].addr == "b4:99:4c:79:cc:a1":
  print("You are near bluetooth 5")
else:
  print("You are not near any devices")
    


