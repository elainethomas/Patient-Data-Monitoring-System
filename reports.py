def patient_report():
    print("---------Patient Report--------")

    file=open("patient.txt", "r")

    total_patients=0
    high_risk=0
    low_risk=0

    for line in file:
        data=line.strip().split("|")

    total_patients +=1
    if data[6].lower()== "high":
        high_risk+=1
    elif data[6].lower=="low":
        low_risk+=1
    file.close()

    print("Total Patients:",total_patients)
    print("High Risk Patients:",high_risk)
    print("Low Risk Patients:",low_risk)

def appointment_report():
    print("--------Appointment Report--------")
    file=open("appointment.txt", "r")
    total_appointment=0
    for line in file:
        data=line.strip().split("|")
        total_appointment+=1
    file.close()
    print("Total Appointments:",total_appointment)


def vaccination_report():
    print("--------Vaccination Report--------")
    file=open("vaccination.txt", "r")
    total_vaccination=0
    given=0
    due=0
    for line in file:
        data=line.strip().split("|")
        total_vaccination+=1
        if data[4].lower()=="given":
            given+=1
        elif data[4].lower=="due":
            due+=1
    file.close()
    print("Total Vaccination Records:",total_vaccination)
    print("Vaccinations Given:",given)
    print("Vaccination Due:",due)

    if due>0:
        print()
        print("--------Due Vaccination--------")
        file=open("vaccination.txt","r")
        for line in file:
           data=line.strip().split("|")
           if data[4].lower()=="due":
            print("Patient ID:",data[1])
            print("Vaccine:",data[2])
            print("Due Date:",data[3])
            print("-----------------------------")
        file.close()


def health_report():
    print("--------Health Report--------")
    file=open("health_check.txt","r")
    total_check=0
    for line in file:
        data=line.strip().split("|")
        total_check+=1
    file.close()
    print("Total Health Checks:",total_check)
    print()
    print("--------BMI Report--------")
    file=open("health_check.txt","r")

    for line in file:
        data=line.strip().split("|")

        patient_id=data[1]
        weight=float(data[3])
        height=float(data[4])

        height_m=height/100
        bmi=weight/(height_m*height_m)
        print("Patient_ID:",patient_id)
        print("BMI:",round(bmi,2))
        if bmi < 18.5:
                print("Category: Underweight")
        elif bmi < 25:
                print("Category : Normal")
        elif bmi < 30 : 
                print("Category Overweight")
        else: 
                print("Category: Obesity")
        print("-------------------------------")
    file.close()