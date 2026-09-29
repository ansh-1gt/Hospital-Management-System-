from Patient import add_patient, show_patients, find_patient
from appointment import book_appointment, show_appointments
from functions import show_menu


print("Welcome to Hospital Management System")

while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        show_patients()

    elif choice == "3":
        find_patient()

    elif choice == "4":
        book_appointment()

    elif choice == "5":
        show_appointments()

    elif choice == "6":
        print("\nThank you for using the Hospital Management System.")
        break

    else:
        print("\nPlease enter a valid choice.")