class hospital_members:
    def __init__(self,name,gender,age,contact_no,address):
        self.name = name
        self.gender = gender
        self.age = age
        self.contact_no = contact_no
        self.address = address

    def hospital_details(self):
        print("---------hos_details---------")
        print(f"name:{self.name}")
        print(f"gender:{self.gender}")
        print(f"age:{self.age}")
        print(f"contact:{self.contact_no}")
        print(f"address:{self.address}")

class Doctor(hospital_members):
    def __init__(self, name, gender, age, contact_no, address, specialization, license, year_of_experience,availability):
        super().__init__(name, gender, age, contact_no, address)
        self.specialization = specialization
        self.license = license
        self.year_of_experience = year_of_experience
        self.availability = availability

    def doctor_details(self):
        hospital_members.hospital_details(self)
        print("---------doc_details---------")
        print(f"specialization:{self.specialization}")
        print(f"license:{self.license}")
        print(f"year_of_experience:{self.year_of_experience}")
        print(f"availability:{self.availability}")

class Nurse(hospital_members):
    def __init__(self,name,gender,age,contact_no,address,assigned_ward,shift,employee_id,year_of_service):
        super().__init__(name,gender,age,contact_no,address)
        self.assigned_ward = assigned_ward
        self.shift = shift
        self.employee_id = employee_id
        self.year_of_service = year_of_service

    def nurse_details(self):
        hospital_members.hospital_details(self)
        print("---------nurse_details---------")
        print(f"shift:{self.shift}")
        print(f"employee_id:{self.employee_id}")
        print(f"year_of_service:{self.year_of_service}")
        print(f"assigned_ward:{self.assigned_ward}")


class Patient(hospital_members):
    def __init__(self,name,gender,age,contact_no,address,room_no,medical_history,admitted_date):
        super().__init__(name,gender,age,contact_no,address)
        self.room_no = room_no
        self.medical_history = medical_history
        self.admitted_date = admitted_date

    def patient_details(self):
        hospital_members.hospital_details(self)
        print("---------paitent_details---------")
        print(f"admitted_date: {self.admitted_date}")
        print(f"room_no: {self.room_no}")
        print(f"medical_history: ")
        for condition in self.medical_history:
            print(f" - {condition}")

# Create multiple Doctor objects
doctors = [
    Doctor("Jill", "Male", 50, "98709866", "42/21", "Eye Specialist", "LIC12345", 16, "Yes"),
    Doctor("Anu", "Female", 40, "99887766", "12/45", "Cardiologist", "LIC67890", 12, "No")
]

# Create multiple Nurse objects
nurses = [
    Nurse("Mani", "Male", 35, "675685856", "25/621", "Ward-12", "Day", "N124", 8),
    Nurse("Sita", "Female", 29, "87654321", "45/321", "Ward-10", "Night", "N129", 5)
]

# Create multiple Patient objects
patients = [
    Patient("Ras", "Female", 20, "124324325", "423/3221", "35", ["Fever", "Cold", "Allergy"], "12/11/2025"),
    Patient("Kumar", "Male", 45, "78654321", "50/11", "12", ["Diabetes", "Hypertension"], "10/10/2025")
]

# Print all Doctor details
print("\n=== DOCTORS LIST ===")
for i,doctor in enumerate(doctors,start=1):
    print(f"\ndoctor-{i}")
    doctor.doctor_details()

# Print all Nurse details
print("\n=== NURSES LIST ===")
for i,nurse in enumerate(nurses,start=1):
    print(f"\nnurse-{i}")
    nurse.nurse_details()

# Print all Patient details
print("\n=== PATIENTS LIST ===")
for i,patient in enumerate(patients,start=1):
    print(f"\npaitent-{i}")
    patient.patient_details()