import fileManager

def Nurse():
    id = -1
    print("\n============================\nNurse Menu\n============================")
    while True:
        if id == -1:
            print("1.login")
            print("2.Back To Menu")
            user = input("Your Choice:").strip()
            match user:
                case "1":
                    id = Login()
                case "2":
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")
        else:
            print("1.View Doctor's Appointment\n2.Record Patient's Observation\n3.View Prescriptions\n4.Administer Medicine To Patients\n5.Back To Menu")
            user = input("Your Choice:").strip()
            match user:
                case "1":
                    view_doctor_appointment(id)
                case "2":
                    record_patient_observation(id)
                case "3":
                    view_patient_medical_records(id)
                case "4":
                    administer_medicine(id)
                case "5":
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")

def Login():
    nurseInfo = fileManager.readFile("nurse.txt")
    userName = input("=======================\nEnter your Name: ").strip()
    userPassword = input("Enter your Password: ").strip()
    if userName == "":
        print("Error:Name cannot be blank!")
        return -1
    elif userPassword == "":
        print("Error:Password cannot be blank!")
        return -1
    for info in nurseInfo:
        if info[1] == userName and info[2] == userPassword:
            print("Successful login!")
            return int(info[0])
    print("Error:Enter error!")
    return -1

def view_doctor_appointment(id): #view doctor's appointment
    print("="*30, "doctor", "="*30)
    fileManager.viewAllDoctor()
    print("="*68)
    appointments = fileManager.readFile("Appointment.txt")
    user = input("Enter Doctor ID: ").strip()
    if user == "":
        print("Error:Doctor ID cannot be empty!")
        return
    elif not user.isdigit():
        print("Error:Doctor ID must be number!")
        return
    print("="*88)
    for i in range(len(appointments)): 
        if appointments[i][1] == user:
            print("Patient ID:", appointments[i][0].ljust(15), "Date:", appointments[i][2].ljust(15), "Start Time:", appointments[i][3].ljust(15), "End Time:", appointments[i][4].ljust(15))
            break
    else:
        print("ID not found.")

def record_patient_observation(id): #me as nurse have to record to the specific Patient ID for future reference
    patient_id = input("Enter Patient ID: ").strip()
    if patient_id == "":
        print("Error:Patient ID cannot be blank.")
        return
    elif not patient_id.isdigit():
        print("Error:Patient ID must be number.")
        return
   
    patient_observation = fileManager.readFile("patient_observations/" + patient_id + ".txt")

    # write information
    blood_pressure = input("Enter Blood Pressure (🩸C): ").strip()
    if blood_pressure == "":
        print("Error:Blood Pressure cannot be empty!")
        return
    elif not blood_pressure.isdigit():
        print("Error:Blood Pressure must be number.")
        return
    
    pulse_rate = input("Enter Pulse Rate (💓): ").strip()
    if pulse_rate == "":
        print("Error:Pulse Rate cannot be empty!")
        return
    elif not pulse_rate.isdigit():
        print("Error:Pulse Rate must be number.")
        return
    
    temperature = input("Enter Temperature (🌡️): ").strip()
    if temperature == "":
        print("Error:Temperature cannot be empty!")
        return
    elif not temperature.isdigit():
        print("Error:Temperature must be number.")
        return
    
    symptoms = input("Enter Symptoms (🩺): ").strip()
    if symptoms == "":
        print("Error:Symptoms cannot be empty!")
        return
    
    date = input("Enter Date (DD/MM/YY): ").strip()
    if date == "":
        print("Error:Date cannot be empty!")
        return
    elif not fileManager.checkDate(date):
        print("Error:Date is wrong!")
        return

    observation_id = len(patient_observation)
    patient_observation.append([int(observation_id), blood_pressure, pulse_rate, temperature, symptoms, date])

    fileManager.writeFile("patient_observations/" + patient_id + ".txt", patient_observation) # will auto create path that not found 
    print("Observation recorded successfully.", "ID", observation_id)

def view_patient_medical_records(id): #To view Medical History such as, history current time,price of medicine,more and more
    user = input("Patient ID: ") 
    if user == "":
        print("Error:Patient ID cannot be empty!")
        return
    elif not user.isdigit():
        print("Error:Patient ID must be number.")
        return
    
    medical_records = fileManager.readFile("patient_medical_records/"+ user +".txt") 
    for medical_record in medical_records:
        print("ID: ",medical_record[0],"\nProblem:",medical_record[1],"\nTime:",medical_record[3],"\nPrice:",medical_record[4],"\nDate:",medical_record[5])

def administer_medicine(id): #Record nurse gave medicine to patient
    print(f"\n{"=" *12} Administer Medicine {"=" *12}")
    ID = input("Enter Patient ID: ")

    Medicine = input("Medicine Type: ")
    if Medicine == "":
        print("Error:Medicine cannot be empty!")
        return
    
    Quantity = input("how many miligram/gram of medicine: ")
    if Quantity == "":
        print("Error:Quantity of medicine cannot be empty!")
        return
    elif not Quantity.isdigit():
        print("Error:Quantity of medicine must be number.")
        return
    print("ID:",ID,"\nMedicine Type:",Medicine,"\nQUantity:", Quantity + "\n"*2 + "SUCCESSFULLY RECORDED")