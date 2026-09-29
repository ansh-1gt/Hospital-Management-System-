
patients = []
appointments = []

while True:

    print("\n===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. Show Patients")
    print("3. Find Patient")
    print("4. Book Appointment")
    print("5. Show Appointments")
    print("6. Exit")

    choice = input("Choose an option: ")

    # Add a new patient
    if choice == "1":
        print("\n--- Add Patient ---")

        patient_id = input("Patient ID: ")
        name = input("Patient Name: ")
        age = input("Age: ")
        disease = input("Disease: ")

        patients.append([patient_id, name, age, disease])

        print("Patient has been added.")

    # Show all patients
    elif choice == "2":
        print("\n--- Patients ---")

        if len(patients) == 0:
            print("There are no patients yet.")
        else:
            for patient in patients:
                print("\nPatient ID:", patient[0])
                print("Name:", patient[1])
                print("Age:", patient[2])
                print("Disease:", patient[3])

    # Find a patient
    elif choice == "3":
        print("\n--- Find Patient ---")

        search_id = input("Enter Patient ID: ")
        patient_found = False

        for patient in patients:
            if patient[0] == search_id:
                print("\nPatient found!")
                print("Patient ID:", patient[0])
                print("Name:", patient[1])
                print("Age:", patient[2])
                print("Disease:", patient[3])

                patient_found = True
                break

        if patient_found == False:
            print("No patient with this ID was found.")

    # Book an appointment
    elif choice == "4":
        print("\n--- Book Appointment ---")

        patient_id = input("Patient ID: ")
        doctor_name = input("Doctor Name: ")
        date = input("Date: ")
        time = input("Time: ")

        appointments.append([patient_id, doctor_name, date, time])

        print("Appointment booked.")

    # Show appointments
    elif choice == "5":
        print("\n--- Appointments ---")

        if len(appointments) == 0:
            print("There are no appointments.")
        else:
            for appointment in appointments:
                print("\nPatient ID:", appointment[0])
                print("Doctor:", appointment[1])
                print("Date:", appointment[2])
                print("Time:", appointment[3])

    # Exit
    elif choice == "6":
        print("\nThank you for using the Hospital Management System.")
        break

    # Wrong menu option
    else:
        print("Please enter a valid option.")