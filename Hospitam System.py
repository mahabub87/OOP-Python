class Patient:
    def __init__(self, patient_id, name, age, gender, ailment):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.ailment = ailment

    def __str__(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Ailment: {self.ailment}"


class HospitalSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self):
        patient_id = input("Enter Patient ID: ")
        if patient_id in self.patients:
            print("Patient ID already exists. Try again.")
            return
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        gender = input("Enter Patient Gender (M/F): ")
        ailment = input("Enter Patient Ailment: ")
        self.patients[patient_id] = Patient(patient_id, name, age, gender, ailment)
        print(f"Patient {name} added successfully.")

    def view_patient(self):
        patient_id = input("Enter Patient ID to view: ")
        if patient_id in self.patients:
            print(self.patients[patient_id])
        else:
            print("Patient not found.")

    def update_patient(self):
        patient_id = input("Enter Patient ID to update: ")
        if patient_id in self.patients:
            print("Current Information:")
            print(self.patients[patient_id])
            print("Enter new details (leave blank to keep current value):")
            name = input("New Name: ") or self.patients[patient_id].name
            age = input("New Age: ")
            age = int(age) if age else self.patients[patient_id].age
            gender = input("New Gender (M/F): ") or self.patients[patient_id].gender
            ailment = input("New Ailment: ") or self.patients[patient_id].ailment
            self.patients[patient_id] = Patient(patient_id, name, age, gender, ailment)
            print("Patient information updated successfully.")
        else:
            print("Patient not found.")

    def delete_patient(self):
        patient_id = input("Enter Patient ID to delete: ")
        if patient_id in self.patients:
            del self.patients[patient_id]
            print("Patient record deleted successfully.")
        else:
            print("Patient not found.")

    def list_all_patients(self):
        if self.patients:
            print("Listing All Patients:")
            for patient in self.patients.values():
                print(patient)
        else:
            print("No patient records found.")

    def run(self):
        while True:
            print("\n--- Hospital System Menu ---")
            print("1. Add Patient")
            print("2. View Patient")
            print("3. Update Patient")
            print("4. Delete Patient")
            print("5. List All Patients")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.add_patient()
            elif choice == '2':
                self.view_patient()
            elif choice == '3':
                self.update_patient()
            elif choice == '4':
                self.delete_patient()
            elif choice == '5':
                self.list_all_patients()
            elif choice == '6':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


# Running the Hospital Management System
hospital_system = HospitalSystem()
hospital_system.run()
