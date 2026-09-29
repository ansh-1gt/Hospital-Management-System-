patients = []


def add_patient():
    print("\n--- Add Patient ---")

    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease: ")

    patient = [patient_id, name, age, disease]
    patients.append(patient)

    print("Patient added successfully.")


def show_patients():
    print("\n--- Patient Details ---")

    if len(patients) == 0:
        print("No patients available.")
        return

    for patient in patients:
        print("\nPatient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Disease:", patient[3])


def find_patient():
    print("\n--- Find Patient ---")

    patient_id = input("Enter Patient ID: ")

    for patient in patients:
        if patient[0] == patient_id:
            print("\nPatient found!")
            print("Patient ID:", patient[0])
            print("Name:", patient[1])
            print("Age:", patient[2])
            print("Disease:", patient[3])
            return

    print("Patient not found.")