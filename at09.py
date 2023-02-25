from bluepy.btle import Scanner, DefaultDelegate

class bluetooth(DefaultDelegate): 
    def _init_(self):
        DefaultDelegate.__init__(self)
