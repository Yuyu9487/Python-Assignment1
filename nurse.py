import main
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
                    main.main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")
        else:
            print("1.View Doctor's Appointment\n2.Record Patient's Observation\n3.View Prescriptions\n4.Administer Medicine To Patients\n5.Back To Menu")
            user = input("Your Choice:").strip()
            match user:
                case "1":
                    view_appointment(id)
                case "2":
                    record_patient_observation(id)
                case "3":
                    view_patient_medical_records(id)
                case "4":
                    administer_medicine(id)
                case "5":
                    main.main()
                case _:
                    print("Error. Please Enter A Valid Input.")

def Login():
    nurseInfo = fileManager.readFile("nurse.txt")
    userName = input("=======================\nEnter your Name: ").strip()
    userPassword = input("Enter your Password: ").strip()
    if userName == "":
        print("Error:Name connot be blank!")
        return -1
    elif userPassword == "":
        print("Error:Password connot be blank!")
        return -1
    for info in nurseInfo:
        if info[1] == userName and info[2] == userPassword:
            print("Successful login!")
            return int(info[0])
        else:
            print("Error:Enter error!")
    return -1

def view_appointment(id): #view doctor's appointment
    print("="*30, "doctor", "="*30)
    fileManager.viewAllDoctor()
    print("="*68)
    appointments = fileManager.readFile("Appointment.txt")
    user = input("Enter patient ID: ").strip()
    print("="*88)
    for i in range(len(appointments)): 
        if appointments[i][0] == user:
            print("Your ID:".rjust(15), appointments[i][0], "Your Name:".rjust(15), appointments[i][1], "Your Contact:".rjust(15), appointments[i][2], "Your Age:".rjust(15), appointments[i][3])
            break
    else:
        print("ID not found.")
        return
    return

def record_patient_observation(id): #me as nurse have to record to the specific Patient ID for future reference
    # 拿到病人的观察记录文件
    patient_id = input("Enter Patient ID: ").strip()
    if patient_id == "":
        print("Error:Patient ID cannot be blank.")
    elif not patient_id.isdigit():
        print("Error:Patient ID must be number.")
    else:
        patient_id = int(patient_id)
   
    patient_observation = fileManager.readFile("patient_observations/" + str(patient_id) + ".txt")

    # 写入资讯/收据数据
    blood_pressure = input("Enter Blood Pressure (🩸C): ").strip()
    pulse_rate = input("Enter Pulse Rate (💓): ").strip()
    temperature = input("Enter Temperature (🌡️): ").strip()
    symptoms = input("Enter Symptoms (🩺): ").strip()
    date = input("Enter Date (01/12/25): ").strip()

    observation_id = len(patient_observation)
    patient_observation.append([int(observation_id), blood_pressure, pulse_rate, temperature, symptoms, date])

    fileManager.writeFile("patient_observations/" + str(patient_id) + ".txt", 6, patient_observation) # will auto create path that not found 
    print("Observation recorded successfully.", "ID", observation_id)

def view_patient_medical_records(id): #get record from (patient_medical_records) that will insert by 'kwx'
    user = input("Patient ID: ") 
    medical_records = fileManager.readFile("patient_medical_records/"+ user +".txt") 
    for x in medical_records:
        print("ID: ",x[0],"\nProblem:",x[1],"\nTime:",x[3],"\nPrice:",x[4],"\nDate:",x[5])

def administer_medicine(id): #to comfirm/record that medicine has given to the patient, 
    print(f"\n{"=" *12} Administer Medicine {"=" *12}")
    ID = input("Enter Patient ID: ")
    Medicine = input("Medicine Type: ")
    Quantity = input("how many miligram/gram of medicine: ")

    print("ID:",ID,"\nMedicine Type:",Medicine,"\nQUantity:", Quantity + "\n"*2 + "SUCCESSFULLY RECORDED")