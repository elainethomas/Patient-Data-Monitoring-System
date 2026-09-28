def add_patient():
    print("--------Add Patient--------")
    patient_id =input("Enter Patient ID:")
    name=input("Enter Name:")
    age=input("Enter Age:")
    gender=input("Enter Gender:")
    phone=input("Enter Phone Number:")
    history=input("Enter Medical History:")
    risk=input("Enter Risk Factor:")

    file=open("patient.txt", "a")
    file.write(patient_id + "|" + name + "|" + age + "|" + gender + "|" + phone + "|" + history + "|" + risk)
    file.close()
    print("Patient added successfully!")


def view_patient():
    print("--------View Patient--------")
    file=open("patient.txt", "r")
    for line in file:
        print(line.strip())
    file.close()


def search_patient():
    print("--------Search Patient--------")
    search_id=input("Enter the ID")
    file=open("patient.txt","r")
    found=False

    for line in file:
        data=line.strip().split("|")

        if data[0]==search_id:
            print("Patient ID:", data[0])
            print("Name:", data[1])
            print("Age:", data[2])
            print("Gender:", data[3])
            print("Phone:", data[4])
            print("Medical History:", data[5])
            print("Risk Factor:", data[6])

            found=True
            break
    file.close()
    if found==False:
        print("Patient not Found")


def update_patient():
    print("---------Update Patient---------")

    update_id = input("Enter Patient ID: ")

    file = open("patient.txt", "r")

    patient = []

    found = False

    for line in file:
        data = line.strip().split("|")

        if data[0] == update_id:
            found = True

            print("Enter new details:")

            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            phone = input("Enter Phone: ")
            history = input("Enter Medical History: ")
            risk = input("Enter Risk Factor: ")

            new_data = update_id + "|" + name + "|" + age + "|" + gender + "|" + phone + "|" + history + "|" + risk

            patient.append(new_data)

        else:
            patient.append(line.strip())

    file.close()

    if found == True:
        file = open("patient.txt", "w")

        for patient in patient:
            file.write(patient + "\n")

        file.close()

        print("Patient updated successfully!")

    else:
        print("Patient not found.")


