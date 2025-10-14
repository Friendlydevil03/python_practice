class Camera:
    def take_photo(self):
        print("Photo captured")

class Phone:
    def make_call(self):
        print("Calling...")

class Smartphone(Camera, Phone):
    def browse(self):
        print("Browsing internet")

samsung = Smartphone()
samsung.take_photo()
samsung.make_call()
samsung.browse()
