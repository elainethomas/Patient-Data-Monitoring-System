def add_vaccination():
    print("--------Add Vaccination--------")

    vaccination_id=input("Enter Vaccination ID:")
    patient_id=input("Enter Patient ID:")
    vaccine=input("Enter Vaccine Name:")
    date=input("Enter Date:")
    status=input("Enter Status (Given/Due):")
    cost=input("Enter Cost:")

    file=open("vaccination.txt","a")
    file.write(vaccination_id + "|" + patient_id + "|" + vaccine + "|" + date + "|" + status + "|" + cost)
    file.close()

    print("Vaccination record added successfully!")


def view_vaccination():
    print("--------Vaccination Records--------")
    file=open("vaccination.txt", "r")
    for line in file:
        data=line.strip().split("|")
        print("Vaccination ID:",data[0])
        print("Patient ID:",data[1])
        print("Vaccine:",data[2])
        print("Date:",data[3])
        print("Status:",data[4])
        print("Cost:",data[5])
        print("--------------------------")

    file.close()


def search_vaccination():
    print("--------Search Vaccination--------")
    patient_id=input("Enter Vaccination ID:")
    vaccine=input("Enter Vaccine Name:")
    file=open("vaccination.txt", "r")
    found=False
    for line in file:
        data=line.strip().split("|")
        if data[0]==patient_id and data[2].lower()==vaccine.lower():
           print("Vaccination ID:",data[0])
           print("Patient ID:",data[1])
           print("Vaccine:",data[2])
           print("Date:",data[3])
           print("Status:",data[4])
           print("Cost:",data[5])
           found=True
           break
    file.close()
    if found==False:
        print("Vaccination record not found") 

        vaccination_id=input("Enter New Vaccination ID:")
        date=input("Enter Due Date:")

        file=open("vaccination.txt", "a")

        file.write(vaccination_id + "|" + patient_id + "|" + vaccine + "|" + date + "|Due|0\n")
        file.close()
        print("Vaccination added as Due.")