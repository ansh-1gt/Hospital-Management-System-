patients = []
appointments = []

while True:

    print("\n==============================")
    print("   HOSPITAL MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Book Appointment")
    print("5. View Appointments")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = input("Enter Age: ")
        disease = input("Enter Disease: ")

        patient = [patient_id, name, age, disease]

        patients.append(patient)

        print("Patient added successfully!")

    elif choice == "2":

        if len(patients) == 0:
            print("No patients found.")

        else:
            print("\n--- Patient List ---")

            for patient in patients:
                print("--------------------")
                print("Patient ID:", patient[0])
                print("Name:", patient[1])
                print("Age:", patient[2])
                print("Disease:", patient[3])

    elif choice == "3":

        search_id = input("Enter Patient ID: ")

        found = False

        for patient in patients:

            if patient[0] == search_id:

                print("\nPatient Found!")
                print("Patient ID:", patient[0])
                print("Name:", patient[1])
                print("Age:", patient[2])
                print("Disease:", patient[3])

                found = True

        if found == False:
            print("Patient not found.")

    elif choice == "4":

        patient_id = input("Enter Patient ID: ")
        doctor = input("Enter Doctor Name: ")
        date = input("Enter Date: ")
        time = input("Enter Time: ")

        appointment = [patient_id, doctor, date, time]

        appointments.append(appointment)

        print("Appointment booked successfully!")

    elif choice == "5":

        if len(appointments) == 0:
            print("No appointments found.")

        else:
            print("\n--- Appointment List ---")

            for appointment in appointments:

                print("--------------------")
                print("Patient ID:", appointment[0])
                print("Doctor:", appointment[1])
                print("Date:", appointment[2])
                print("Time:", appointment[3])

    elif choice == "6":

        print("Thank you for using Hospital Management System!")
        break

    else:

        print("Invalid choice.")