class Battery:
    ID = None
    def __init__(self,battery,type):
        if Battery.ID is None:
            Battery.ID = self
        else:
            raise Exception("single Ton")
        self.battery = battery
        self.type = type


    def Battery_details(self):
        print(f"{"-"*10}Battery Details{"-"*10}")
        print(f"Has a battery:{self.battery}\ntype_of_battery: {self.type}")
        print(f"{"-"*10}{"-"*25}")


class Mobile:
    Brand ="Apple"
    bat = Battery("True","Li-ion")
    def __init__(self,Model,SIM,GPS):
        self.Model = Model
        self.SIM = SIM
        self.GPS = GPS

    def Mobile_details(self):
        Mobile.bat.Battery_details()
        print(f"{"-" * 10}Mobile Details{"-" * 10}")
        print(f"Brand: {self.Brand}\nModel:{self.Model}\nSIM_solt:{self.SIM}\nGPS:{self.GPS}")
        print(f"{"-" * 10}{"-" * 25}")

m1 = Mobile("17",True,True)
m1.Mobile_details()
# m1.bat.Battery_details()
# bat1 = Battery("5000mah","Li-ion")

