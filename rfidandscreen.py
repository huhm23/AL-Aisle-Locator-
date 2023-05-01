import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from bluepy.btle import Scanner
from adafruit_rgb_display import hx8357

def rfid():
    reader = SimpleMFRC522()

    print("Hold a tag near the reader")
    print("Reading tag in 1 second...")
    time.sleep(1)
    id = reader.read_id_no_block()
    text = ''
    if id:
        idnum = hex(id)
    else:
        text = "No tag detected"

    if idnum == "0xb883bd33b5":
        text = "Hello Haelyne"
    elif idnum == "0x944f08aa79":
        text = "Hello Dean"
    elif idnum == "0x64ff0daa3c":
        text = "Hello Dana"
    elif idnum == "0xb4b32baa86":
        text = "Hello Professor Fund"
    elif idnum == "0x34e619aa61":
        text = "Hello Ufuk"
    else:
        text = "Nothing was scanned. Please try again."
    return text

def bluetooth():

    # create list for my bluetooth devices
    # the "none" is for when there are not any bluetooth devices near
    my_list = ["none"]
    # create list for devices that are scanned
    ble_list = Scanner().scan(3.0)

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
        if my_list[i] == "none":
            pass
        elif my_list[i].rssi >= max_num:
            max_num = my_list[i].rssi
            max_index = i

    # compare the address to the bluetooth addresses and print the statement of the one you are near
    if my_list[max_index] == "none":
        area = "You are not near any devices"
    elif my_list[max_index].addr == "90:e2:02:b1:96:c3":
        area = "You are near bluetooth 1"
    elif my_list[max_index].addr == "d0:b5:c2:96:6b:f3":
        area = "You are near bluetooth 2"
    elif my_list[max_index].addr == "78:a5:04:90:82:69":
        area = "You are near bluetooth 3"
    elif my_list[max_index].addr == "ec:11:27:54:4b:42":
        area = "You are near bluetooth 4"
    else:
        area = "You are near bluetooth 5"
    return area

def screen():
    # First define some constants to allow easy resizing of shapes.
    BORDER = 20
    FONTSIZE = 36
    
    # Configuration for CS and DC pins (these are PiTFT defaults):
    cs_pin = digitalio.DigitalInOut(board.CE1)
    dc_pin = digitalio.DigitalInOut(board.D24)
    reset_pin = digitalio.DigitalInOut(board.D25)
    
    # Config for display baudrate (default max is 24mhz):
    BAUDRATE = 24000000
    
    # Setup SPI bus using hardware SPI:
    spi = board.SPI()
    
    disp = hx8357.HX8357(spi, rotation=180,cs=cs_pin,dc=dc_pin,rst=reset_pin,baudrate=BAUDRATE)
    
    # Make sure to create image with mode 'RGB' for full color.
    if disp.rotation % 180 == 90:
        height = disp.width  # we swap height/width to rotate it to landscape!
        width = disp.height
    else:
        width = disp.width  # we swap height/width to rotate it to landscape!
        height = disp.height
    
    image = Image.new("RGB", (width, height))
    
    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    # Draw a white filled box as the background
    draw.rectangle((0, 0, width, height), fill=(255, 255, 255))
    disp.image(image)
    # Load a TTF Font
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)
    
    # Draw Some Text
    mem = rfid()
    (font_width, font_height) = font.getsize(mem)
    draw.text(
        (width - font_width, 0),
        mem,
        font=font,
        fill=(0, 0, 0),
    )
    disp.image(image)
    
    place = bluetooth()
    (font_width, font_height) = font.getsize(place)
    draw.text(
        (width//2 - font_width//2, height//2 - font_height//2),
        place,
        font=font,
        fill=(0, 0, 0),
    )
    # Display image.
    disp.image(image)


screen()

