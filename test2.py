from bluepy.btle import Scanner

my_list = []
try:
  ble_list = Scanner().scan(10.0)
  for dev in ble_list:
    if dev.addr == "90:e2:02:b1:96:c3" or dev.addr == "d0:b5:c2:96:6b:f3":
      my_list.append(dev)
except:
  raise Exception("Error occured")

max_num = -10000
max_index = -1
  
for i in range(len(my_list)):
  if my_list[i].rssi > max_num:
    max_num = my_list[i].rssi
    max_index = i 

print(f"mac: {my_list[max_index].addr} ; rssi: {my_list[max_index].rssi}")
