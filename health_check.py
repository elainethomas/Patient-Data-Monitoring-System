def add_health_check():
    print("--------Add Health Check--------")

    health_id=input("Enter Health Check ID:")
    patient_id=input("Enter Patient ID:")
    date=input("Enter Date:")
    weight=input("Enter Weight (kg):")
    height=input("Enter Height (cm):")
    blood_pressure=input("Enter Blood Pressure:")
    blood_sugar=input("Enter Blood Sugar:")

    file=open("health_check.txt" , "a")
    file.write(health_id + "|" + patient_id + "|" + date + "|" + weight + "|" + height + "|" + blood_pressure + "|" + blood_sugar + "\n" )
    file.close()
    print("Health check added successfully!")


def view_health_check():
    print("--------Health Check Records--------")

    file=open("health_check.txt", "r")

    for line in file:
        data = line.strip().split("|")

        print("Health Check ID:",data[0])
        print("Patient ID:",data[1])
        print("Date:",data[2])
        print("Weight:",data[3])
        print("Height:",data[4])
        print("Blood Pressure:",data[5])
        print("Blood Sugar:",data[6])
        print("-----------------------------------")

    file.close()


def calculate_bmi():
    print("---------Calculate BMI--------")
    patient_id=input("Enter Patient ID:")
    file=open("health_check.txt","r")
    found=False
    for line in file:
        data=line.strip().split("|")

        if data[1]==patient_id:
            weight=float(data[3])
            height=float(data[4])

            height_m=height/100
            bmi=weight/(height_m*height_m)

            print("Pateint ID:",data[1])
            print("Weight:",weight,"kg")
            print("Height:",height,"cm")
            print("BMI:",round(bmi,2))

            if bmi < 18.5:
                print("Category: Underweight")
            elif bmi < 25:
                print("Category : Normal")
            elif bmi < 30 : 
                print("Category Overweight")
            else: 
                print("Category: Obesity")

            found=True
            break
    file.close()
    if found==False:
        print("Health Check record not found.")