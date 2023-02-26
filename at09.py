from bluepy.btle import DefaultDelegate

class bluetooth(DefaultDelegate): 
    def _init_(self):
        DefaultDelegate.__init__(self)
