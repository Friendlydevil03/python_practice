class Mobile:
    def __init__(self):
        self.__battery_level = 100

    def use_phone(self, mins):
        self.__battery_level -= mins * 0.5

    def charge_phone(self):
        self.__battery_level = 100

    def get_battery_status(self):
        return f"Battery: {self.__battery_level}%"

phone = Mobile()
phone.use_phone(20)
print(phone.get_battery_status())
