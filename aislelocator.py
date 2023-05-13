from mfrc522 import SimpleMFRC522
import digitalio
import board
from adafruit_rgb_display import hx8357
from bluepy.btle import Scanner
from PIL import Image, ImageDraw, ImageFont

class AisleLocator:
    # First define some constants to allow easy resizing of shapes.
    BORDER = 20
    FONTSIZE = 36

    def __init__(self):
        self.reader = None
        self.disp = None
        self.spi = None
        self.height = None
        self.width = None
        self.mem_text = ""
        self.near_text = "Welcome to SuperMarket"
        self.goto_text = "If member -> Hold card near reader"
        self.iffound_text = "If not member -> Wait 5 seconds"

    def display_setup(self):
        # Setup SPI bus using hardware SPI:
        # Configuration for CS and DC pins (these are PiTFT defaults):
        BAUDRATE = 24000000
        cs_pin = digitalio.DigitalInOut(board.CE1)
        dc_pin = digitalio.DigitalInOut(board.D24)
        reset_pin = digitalio.DigitalInOut(board.D25)
        self.spi = board.SPI()
        self.disp = hx8357.HX8357(self.spi, rotation=180, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=BAUDRATE)
        # Make sure to create image with mode 'RGB' for full color.
        if self.disp.rotation % 180 == 90:
            self.height = self.disp.width  # we swap height/width to rotate it to landscape!
            self.width = self.disp.height
        else:
            self.width = self.disp.width  # we swap height/width to rotate it to landscape!
            self.height = self.disp.height

    def rfid_read(self):
        self.reader = SimpleMFRC522()
        member_id = self.reader.read_id_no_block()
        return member_id

    def bluetooth(self):

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
        if my_list[max_index] != "none":
            return my_list[max_index].addr
        else:
            return "none"


    def update_display(self):
        FONTSIZE = 24
        image = Image.new("RGB", (self.width, self.height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)
        # Draw a white filled box as the background
        draw.rectangle((0, 0, self.width, self.height), fill=(255, 255, 255))
        self.disp.image(image)
        # Load a TTF Font
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)

        # Draw Some Text
        mem = self.mem_text
        (font_width, font_height) = font.getsize(mem)
        draw.text(
            (self.width - font_width, 0),
            mem,
            font=font,
            fill=(0, 0, 0),
        )
        loc = self.near_text
        (font_width, font_height) = font.getsize(loc)
        draw.text(
            (self.width // 2 - font_width // 2, (self.height  - (3 * font_height))  // 2 - font_height // 2),
            loc,
            font=font,
            fill=(0, 0, 0),
        )
        go = self.goto_text
        (font_width, font_height) = font.getsize(go)
        draw.text(
            (self.width // 2 - font_width // 2, (self.height + (3 * font_height)) // 2 - font_height // 2),
            go,
            font=font,
            fill=(0, 0, 0),
          )
        found = self.iffound_text
        draw.text(
            (self.width // 2 - font_width // 2, (self.height + (6 * font_height)) // 2 - font_height // 2),
            found,
            font=font,
            fill=(0, 0, 0),
        )
        # Display image.
        self.disp.image(image)
    def update_mem_text(self, new_mem_text):
        self.mem_text = new_mem_text

    def update_near_text(self, new_near_text):
        self.near_text = new_near_text

    def update_goto_text(self, new_goto_text):
        self.goto_text = new_goto_text 

    def update_iffound_text(self, new_iffound_text):
        self.iffound_text = new_iffound_text
