class Patient:
    def __init__(self, name, disease):
        self.__name = name
        self.__disease = disease

    def get_info(self):
        return f"Patient: {self.__name}, Disease: {self.__disease}"

    def update_disease(self, new_disease):
        self.__disease = new_disease

p1 = Patient("Ravi", "Flu")
print(p1.get_info())
p1.update_disease("Recovered")
print(p1.get_info())
