class Engine_system:
    def __init__(self,engine_type,engine_power):
        self.engine_type = engine_type
        self.engine_power = engine_power

    def Engine_details(self):
        print(f"engine_type:{self.engine_type}")
        print(f"engine_power:{self.engine_power}")

class Wing_system:
    def __init__(self,wing_type,wing_span,wing_material):
        self.wing_type = wing_type
        self.wing_span = wing_span
        self.wing_material = wing_material

    def Wing_details(self):
        print(f"wing_type:{self.wing_type}")
        print(f"wing_span:{self.wing_span}")
        print(f"wing_material:{self.wing_material}")

class Airplane_details(Engine_system,Wing_system):
    def __init__(self,engine_type,engine_power,wing_type,wing_span,wing_material,manufacturer,model_name,lenght,capacity,fuel_capacity,no_of_engines):
        Engine_system.__init__(self,engine_type,engine_power)
        Wing_system.__init__(self,wing_type,wing_span,wing_material)
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.lenght = lenght
        self.capacity = capacity
        self.fuel_capacity = fuel_capacity
        self.no_of_engines = no_of_engines

    def air_details(self):
        Engine_system.Engine_details(self)
        Wing_system.Wing_details(self)
        print(f"manufacturer:{self.manufacturer}")
        print(f"model_name:{self.model_name}")
        print(f"length:{self.lenght}")
        print(f"capacity:{self.capacity}")
        print(f"fuel_capacity:{self.fuel_capacity}")
        print(f"no_of_engines:{self.no_of_engines}")

details = Airplane_details("turbofan","120000ibs","Fixed_wings",60,"aluminum","boeing","airbus","2000m","250","500L","6")
details.air_details()