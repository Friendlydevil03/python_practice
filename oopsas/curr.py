
class SecuritySystem:
    def __init__(self, watermark, hologram, serial_code):
        self.watermark = watermark
        self.hologram = hologram
        self.serial_code = serial_code

    def show_security_features(self):
        print(f"Watermark Design : {self.watermark}")
        print(f"Hologram Type    : {self.hologram}")
        print(f"Serial Code      : {self.serial_code}")


class PrintingSystem:
    def __init__(self, ink_type, paper_quality, print_capacity):
        self.ink_type = ink_type
        self.paper_quality = paper_quality
        self.print_capacity = print_capacity

    def show_printing_details(self):
        print(f"Ink Type         : {self.ink_type}")
        print(f"Paper Quality    : {self.paper_quality}")
        print(f"Print Capacity   : {self.print_capacity} notes/hour")


class QualityControl:
    def __init__(self, quality_grade, inspection_level):
        self.quality_grade = quality_grade
        self.inspection_level = inspection_level

    def show_quality_details(self):
        print(f"Quality Grade    : {self.quality_grade}")
        print(f"Inspection Level : {self.inspection_level}")


class CurrencyPress(SecuritySystem, PrintingSystem,QualityControl):
    def __init__(self, country, denomination, watermark, hologram, serial_code,ink_type, paper_quality, print_capacity,quality_grade, inspection_level):
        SecuritySystem.__init__(self, watermark, hologram, serial_code)
        PrintingSystem.__init__(self, ink_type, paper_quality, print_capacity)
        QualityControl.__init__(self, quality_grade, inspection_level)
        self.country = country
        self.denomination = denomination

    def display_currency_details(self):
        print(f"Country          : {self.country}")
        print(f"Denomination     : {self.denomination}")
        SecuritySystem.show_security_features(self)
        PrintingSystem.show_printing_details(self)
        QualityControl.show_quality_details(self)

note = CurrencyPress("India","₹500","Mahatma Gandhi Portrait","3D Security Thread","IND2025A500","Special Magnetic Ink",
"Cotton-based Security Paper",10000,10,10)

note.display_currency_details()
