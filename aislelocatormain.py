import RPi.GPIO as GPIO
import time
import aislelocator
from mfrc522 import SimpleMFRC522
import digitalio
import board
from adafruit_rgb_display import hx8357
from bluepy.btle import Scanner
from PIL import Image, ImageDraw, ImageFont

alo = aislelocator.AisleLocator()

dict_of_mem = {792484197301 : "Haelyne", 433775815228 : "Dana", 18421623527 : "Shantanu",\
227198741089 : "Ufuk", 776100096646 : "Professor Fund", 636981127801 : "Dean"}

dict_of_places = {"A1": "milk", "A2": "eggs", "A3": "chips",\
 "A4": "banana", "A5": "canned foods", "You are not near any devices" : ""}

dict_of_shopping_list = {"name" : "Haelyne", "shopping list" : ["eggs", "banana"]}

dict_of_next = {"A1" : "Go to A2", "A2" : "Go to A3", "A3" : "Go to A4", "A4" : "Go to A5", "A5" : "Go to A1"}

dict_of_near = {"You are not near any devices" : "Move to near a sign" , "A1" : "You are near A1", "A2" : "You are near A2",\
 "A3" : "You are near A3", "A4" : "You are near A4", "A5" : "You are near A5"}

dict_of_location = {"none" : "You are not near any devices", "90:e2:02:b1:96:c3" : "A1", "d0:b5:c2:96:6b:f3" : "A2",\
"78:a5:04:90:82:69" : "A3", "ec:11:27:54:4b:42" : "A4", "b4:99:4c:79:cc:a1" : "A5"} 


def name_of_member():
    member_id = alo.rfid_read() 
    if member_id:
        if member_id in dict_of_mem.keys():
            return ("Hello " + dict_of_mem[member_id])
    else:
        return "Not a member"

def place_A():
    location = alo.bluetooth()
    if location in dict_of_location.keys():
        return dict_of_location[location]

def where_A():
    where = place_A()
    if where in dict_of_near.keys():
        area = dict_of_near[where]
    item = dict_of_places[where]
    if item in dict_of_shopping_list["shopping list"]:
        dict_of_shopping_list["shopping list"].remove(item)
        return area, item 
def next_A():
    current = place_A()
    if current in dict_of_next.keys():
        next = dict_of_next[current]
        return next


# Screen will print first "You are near A1, the Milk section" -> "Go to A2" ->
# "You are near A2, the Eggs section" -> "Go to A3" -> "You are near A3, the Chips section" -> "Go to A4" ->
# "You are near A3, the Bananas section"

####main

alo.display_setup()  #run once
alo.update_display()
time.sleep(3)
member = name_of_member()
print(member)
alo.update_mem_text(member)  #run once
while True:
    alo.update_iffound_text("")
    new_loc , item = where_A()
    next_area = next_A()
    print(next_area)
    alo.update_near_text(new_loc)
    alo.update_goto_text(next_area)
    alo.update_display()
    if len(dict_of_shopping_list["shopping list"]) == 0:
        alo.update_near_text("Thank you for shopping with us")
        alo.update_goto_text("")
        alo.update_display()
        break
    if item != None and member[6:] == dict_of_shopping_list["name"]:
        alo.update_goto_text("You are near the " + item)
        alo.update_near_text("")
        alo.update_display()
        time.sleep(5)
        continue
GPIO.cleanup()

