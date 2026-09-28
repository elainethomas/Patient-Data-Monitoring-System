import patient
import appointment
import vaccination
import health_check
import reports

def main():
    while True:
        print()
        print("---------------------------------------------")
        print("     PATIENT HEALTH MONITORING SYSTEM        ")
        print("---------------------------------------------")
        print("1. Patient Management")
        print("2. Appointment Management")
        print("3. Vaccination Management")
        print("4. Health Check")
        print("5. Reports")
        print("6. Exit")

        choice=input("Enter your Choice:")

        if choice== "1":
            while True:
                print()
                print("--------Patient Management--------")
                print("1. Add Patient")
                print("2. View Patient")
                print("3. Search Patient")
                print("4. Update Patient")
                print("5. Back")

                patient_choice=input("Enter your choice:")

                if patient_choice == "1":
                    patient.add_patient()
                elif patient_choice == "2":
                    patient.view_patient()
                elif patient_choice == "3":
                    patient.search_patient()
                elif patient_choice == "4":
                    patient.update_patient()
                elif patient_choice == "5":
                    break
                else:
                    print("Invalid Choice!")

        elif choice == "2":
            while True:
                print()
                print("--------Appointment Management--------")
                print("1. Book Appointment")
                print("2. View Appointment")
                print("3. Search Appointment")
                print("4. Cancel Appointment")
                print("5. Back")

                appointment_choice=input("Enter your choice:")

                if appointment_choice == "1":
                    appointment.book_appointment()
                elif appointment_choice == "2":
                    appointment.view_appointment()
                elif appointment_choice == "3":
                    appointment.search_appointment()
                elif appointment_choice == "4":
                    appointment.cancel_appointment()
                elif appointment_choice == "5":
                    break
                else:
                    print("Invalid Choice!")

        elif choice == "3":
            while True:
                print()
                print("--------Vaccination Management--------")
                print("1. Add Vaccination")
                print("2. View Vaccination")
                print("3. Search Vaccination")
                print("4. Back")

                vaccination_choice=input("Enter your choice:")

                if vaccination_choice == "1":
                    vaccination.add_vaccination()
                elif vaccination_choice == "2":
                    vaccination.view_vaccination()
                elif vaccination_choice == "3":
                    vaccination.search_vaccination()
                elif vaccination_choice == "4":
                    break
                else:
                    print("Invalid Choice!")

        elif choice == "4":
            while True:
                print()
                print("--------Health Check--------")
                print("1.Add Health Check")
                print("2. View Health Check")
                print("3. Calculate BMI")
                print("4. Back")

                health_choice=input("Enter your Choice:")
                if health_choice == "1":
                    health_check.add_health_check()
                elif health_choice == "2":
                    health_check.view_health_check()
                elif health_choice == "3":
                    health_check.calculate_bmi()
                elif health_choice == "4":
                    break
                else:
                    print("Invalid Choice!")

        elif choice== "5":
            while True:
                print()
                print("--------Reports--------")
                print("1. Patient Report")
                print("2. Appointment Report")
                print("3. Vaccination Report")
                print("4. Health Report")
                print("5. Back")

                report_choice=input("Enter your Choice:")

                if report_choice == "1":
                    reports.patient_report()
                elif report_choice == "2":
                    reports.appointment_report()
                elif report_choice == "3":
                    reports.vaccination_report()
                elif report_choice == "4":
                    reports.health_report()
                elif report_choice == "5":
                    break
                else:
                    print("Invalid Choice!")
        elif choice == "6":
            print("Thank you for using Paient Health Monitoring System!")

        else: 
            print("Invalid choice! Please try again.")

main()