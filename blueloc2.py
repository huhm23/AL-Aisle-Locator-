from bluepy.btle import Scanner

#B1: 90:e2:02:b1:96:c3
#B2: d0:b5:c2:96:6b:f3
#B3: 78:a5:04:90:82:69
#B4: ec:11:27:54:4b:42
#B5: b4:99:4c:79:cc:a1

my_list = []
ble_list = Scanner().scan(10.0)
try:
  for dev in ble_list:
    if dev.addr == "90:e2:02:b1:96:c3" or dev.addr == "d0:b5:c2:96:6b:f3" or dev.addr == "78:a5:04:90:82:69" \
    or dev.addr == "ec:11:27:54:4b:42" or dev.addr == "b4:99:4c:79:cc:a1":
      my_list.append(dev)
except:
  raise Exception("Error occured")
for dev in my_list:
  print(f"mac: {my_list[dev].addr} ; rssi: {my_list[dev].rssi}")

max_num = -10000
max_index = -1
  
for i in range(len(my_list)):
  if my_list[i].rssi >= max_num: 
    max_num = my_list[i].rssi
    max_index = i

if my_list[max_index].addr == "90:e2:02:b1:96:c3":
  print("You are near bluetooth 1")
elif my_list[max_index].addr == "d0:b5:c2:96:6b:f3":
  print("You are near bluetooth 2")
elif my_list[max_index].addr == "78:a5:04:90:82:69":
  print("You are near bluetooth 2")
elif my_list[max_index].addr == "ec:11:27:54:4b:42":
  print("You are near bluetooth 2")
else:
  print("You are near bluetooth 3")
    

print(f"mac: {my_list[max_index].addr} ; rssi: {my_list[max_index].rssi}")
