def book_appointment():
    print("--------Book Appointment--------")

    appointment_id=input("Enter Appointment ID:")
    patient_id=input("Enter the Patient ID:")
    doctor=input("Enter Doctor Name:")
    date=input("Enter Date:")
    time=input("Enter Time:")
    reason=input("Enter Reason:")

    file=open("appointment.txt","a")
    file.write(appointment_id + "|" + patient_id + "|" + doctor + "|" + date + "|" + time + "|" + reason +  "\n")
    file.close()

    print("Appointment booked successfully!")


def view_appointment():
    print("--------Appointment List--------")
    file=open("appointment.txt", "r")
    for line in file:
        data=line.strip().split("|")
        print("Appointment ID:",data[0])
        print("Patient ID:",data[1])
        print("Doctor:",data[2])
        print("Date:",data[3])
        print("Time:",data[4])
        print("Reason:",data[5])
        print("--------------------------")

    file.close()


def search_appointment():
    print("--------Search Appointment--------")
    search_id=input("Enter Appointment ID:")
    file=open("appointment.txt", "r")
    found=False
    for line in file:
        data=line.strip().split("|")
        if data[0]==search_id:
           print("Appointment ID:",data[0])
           print("Patient ID:",data[1])
           print("Doctor:",data[2])
           print("Date:",data[3])
           print("Time:",data[4])
           print("Reason:",data[5])
        found=True
        break
    file.close()
    if found==False:
        print("Appointment not found")
        

def cancel_appointment():
    print("--------Cancel Appointment--------")
    cancel_id=input("Enter Appointment ID:")
    file=open("appointment.txt", "r")
    appointment=[]
    found=False
    for line in file:
        data=line.strip().split("|")
        if data[0]==cancel_id:
            found=True
        else:
            appointment.append(line.strip())
    file.close()
    if found==True:
        file=open("appointment.txt","w")

        for appointment in appointment:
            file.write(appointment + "\n")
        file.close()
        print("Appointment cancelled successfully!")
    else:
        print("Appointment not found")