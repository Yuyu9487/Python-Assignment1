import main
import fileManager
import os
#Nurse Functions
def Nurse():
    print("\n============================\nNurse Menu\n============================")
    print("1.View Doctor's Appointment\n2.Record Patient's Observation\n3.View Prescriptions\n4.Administer Medicine To Patients\n5.Back To Menu")
    while True:
        user = input("Your Choice:")
        match user:
                case "1":
                    view_appointment()
                    break
                case "2":
                    record_patient_observation()
                    break
                case "3":
                    view_doc__medical_records()
                    break
                case "4":
                    administer_medicine()
                    break
                case "5":
                    main.main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")

def view_appointment(): #view doctor's appointment
    nurseinfo = fileManager.readFile("nurseinfo.txt")
    #data = [(id, name, contact, age), (id, name, contact, age), (id, name, contact, age), ..
    user = input("Enter Your ID: ")
    for i in range(len(nurseinfo)):
        if nurseinfo[i][0] == user:
            print("Your ID:", nurseinfo[i][0])
            print("Your Name:", nurseinfo[i][1])
            print("Your Contact:", nurseinfo[i][2])
            print("Your Age:", nurseinfo[i][3])
            break
    else:
        print("ID not found.")
        return
    return


def record_patient_observation():
    # 拿到病人的观察记录文件
    patient_id = (input("Enter Patient ID: ")) 
    if patient_id == "":
        print("Error:Patient ID cannot be blank.")
    elif not patient_id.isdigit():
        print("Error:Patient ID must be number.")
    else:
        patient_id = int(patient_id)
        return
    #ensure the file is exist
    folder_path = "patient_observation"
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path,f"{patient_id}.txt")
    patient_observations = fileManager.readfile(file_path)
    # patient_observation = fileManager.readFile("patient_observation.txt")
    patient_observation = fileManager.readFile("patient_observation/" + str(patient_id) + ".txt")
    # patient_observation = [[id, blood_pressure, pulse_rate, ...], [id, ...], [id, ...], ...]

    # 写入资讯/收据数据
    blood_pressure = (input("Enter Blood Pressure (🩸C): "))
    pulse_rate = (input("Enter Pulse Rate (💓): "))
    temperature = str(float(input("Enter Temperature (🌡️): ")))
    symptoms = (input("Enter Symptoms (🩺): "))
    date = input("Enter Date (**/**/****): ")

    observation_id = len(patient_observation)
    patient_observation.append([int(observation_id), blood_pressure, pulse_rate, temperature, symptoms, date])

    fileManager.writeFile("patient_observation/" + str(patient_id) + ".txt", 6, patient_observation)

    # observation = f"Patient ID: {patient_id}, Blood Pressure: {blood_pressure}C, Pulse Rate: {pulse_rate}bpm, Temperature: {temperature}C, Symptoms: {symptoms}\n"
    # with open("patient_observation.txt", "a") as file:
    #     file.write(observation)



    

    return
def view_doc__medical_records():
    print('hello')
def administer_medicine():
    return


#def nurseupdateinfo():
    nurseinfo = fileManager.readfile("nureseinfo.txt")
    #data = [(id, name, contact, age), (id, name, contact, age), (id, name, contact, age), ..
    user = input("Enter Your ID:")
    for i in range(len(nurseinfo)):
        if nurseinfo[i][0] == user:
            print("Your ID:", nurseinfo[i][0])
            print("Your Name:", nurseinfo[i][1])
            print("Your Contact:", nurseinfo[i][2])
            print("Your Age:", nurseinfo[i][3])
            break
    else:
        print("ID not found.")
        return