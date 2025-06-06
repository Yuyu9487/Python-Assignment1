import main
import fileManager


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
    appointments = fileManager.readFile("Appointment.txt")
    #data = [(id, name, contact, age), (id, name, contact, age), (id, name, contact, age), ..
    user = input("Enter Your ID: ")
    print("="*88)
    for i in range(len(appointments)): 
        if appointments[i][0] == user:
            print("Your ID:".rjust(15), appointments[i][0])
            print("Your Name:".rjust(15), appointments[i][1])
            print("Your Contact:".rjust(15), appointments[i][2])
            print("Your Age:".rjust(15), appointments[i][3])
            break
    else:
        print("ID not found.")
        return
    return




def record_patient_observation(): #me as nurse have to record to the specific Patient ID for future reference
    # 拿到病人的观察记录文件
    patient_id = (input("Enter Patient ID: ")) 
    if patient_id == "":
        print("Error:Patient ID cannot be blank.")
    elif not patient_id.isdigit():
        print("Error:Patient ID must be number.")
    else:
        patient_id = int(patient_id)
   
    patient_observation = fileManager.readFile("patient_observations/" + str(patient_id) + ".txt")

    # 写入资讯/收据数据
    blood_pressure = (input("Enter Blood Pressure (🩸C): "))
    pulse_rate = (input("Enter Pulse Rate (💓): "))
    temperature = str(float(input("Enter Temperature (🌡️): ")))
    symptoms = (input("Enter Symptoms (🩺): "))
    date = input("Enter Date (**/**/****): ")

    observation_id = len(patient_observation)
    patient_observation.append([int(observation_id), blood_pressure, pulse_rate, temperature, symptoms, date])

    fileManager.writeFile("patient_observations/" + str(patient_id) + ".txt", 6, patient_observation) # will auto create path that not found 
    print("Observation recorded successfully.", "ID", observation_id)
    return



def view_doc__medical_records(): #get record from (patient_medical_records) that will insert by 'kwx'
    user = input("Patient ID: ") 
    medical_records = fileManager.readFile("patient_medical_records/"+ user +".txt") 
    for x in medical_records:
        print("ID: ",x[0],"\nProblem:",x[1],"\nTime:",x[3],"\nPrice:",x[4],"\nDate:",x[5])
              

    


def administer_medicine(): #to comfirm/record that medicine has given to the patient, 
    print(f"\n{"=" *12} Administer Medicine {"=" *12}")
    ID = input("Enter Patient ID: ")
    Medicine = input("Medicine Type: ")
    Quantity = input("how many miligram/gram of medicine: ")

    print("ID:",ID,"\nMedicine Type:",Medicine,"\nQUantity:", Quantity + "\n"     *2 + "SUCCESSFULLY RECORDED")






    return
