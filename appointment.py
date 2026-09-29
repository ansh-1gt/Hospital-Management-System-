appointments = []


def book_appointment():
    print("\n--- Book Appointment ---")

    patient_id = input("Enter Patient ID: ")
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Date: ")
    time = input("Enter Time: ")

    appointment = [patient_id, doctor, date, time]
    appointments.append(appointment)

    print("Appointment booked successfully.")


def show_appointments():
    print("\n--- Appointment Details ---")

    if len(appointments) == 0:
        print("No appointments available.")
        return

    for appointment in appointments:
        print("\nPatient ID:", appointment[0])
        print("Doctor:", appointment[1])
        print("Date:", appointment[2])
        print("Time:", appointment[3])