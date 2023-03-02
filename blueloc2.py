from bluepy.btle import Scanner

my_list = []
try:
  ble_list = Scanner().scan(10.0)
  for dev in ble_list:
    if dev.addr == "90:e2:02:b1:96:c3" or dev.addr == "d0:b5:c2:96:6b:f3":
      my_list.append(dev)
      #if dev.rssi 
      #print("mac: {} ; rssi: {}".format(dev.addr, dev.rssi))
                        #else:
                                #pass 
except:
  raise Exception("Error occured")

max_num = -10000
max_index = -1
  
for i in range(len(my_list)):
  if my_list[i].rssi > max_num:
    max_num = my_list[i].rssi
    max_index = i
if my_list[max_index].addr == "90:e2:02:b1:96:c3":
  print("You are near bluetooth 1")
elif my_list[max_index].addr == "d0:b5:c2:96:6b:f3":
  print("You are near bluetooth 2") 
    

print(f"mac: {my_list[max_index].addr} ; rssi: {my_list[max_index].rssi}")
