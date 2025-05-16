import main
#Doctor Funtion
MEDICAL_HISTORY_FILE="patient_observation.txt"
APPOINTMENT_FILE="patient.txt"

def Doctor():
    print("\n============================\nDoctor Menu\n============================")
    print("1.Patient's Medical Logs/Treatment History\n2.Update Patient Record\n3.View Appointment List\n4.Block/Unblock Schedule\n5.Back To Menu")
    while True:
        user = input("Your Choice:")
        match user:
                case "1":
                    Medlogs()
                    print()
                    break
                case "2":
                    UpdatePatRec()
                    break
                case "3":
                    viewappoint()
                    break
                case "4":
                    Timetable()
                    break
                case "5":
                    main.main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")
def Medlogs():
    pid = input("Enter Patient ID: ").strip()
    found = False
    with open(MEDICAL_HISTORY_FILE, "r") as f:
        for line in f:
            if line.startswith(pid):
                print(line.strip())
                found = True
    if not found:
        print("No records found.")

def UpdatePatRec():
   def update_patient_record(patient_id):
    if patient_id in Medlogs:
        print(f"\nUpdating record for {Medlogs[patient_id]['name']} (ID: {patient_id})")

        diagnosis = input("Enter diagnosis: ")
        treatment = input("Enter treatment: ")
        allergy = input("Enter allergy: ")

        Medlogs[patient_id]["diagnosis"] = diagnosis
        Medlogs[patient_id]["treatment"] = treatment
        Medlogs[patient_id]["allergy"] = allergy

        print("\n✅ Patient record updated successfully!")
    else:
        print("❌ Patient ID not found.")

# Example usage:
patient_id = input("Enter Patient ID to update: ")
UpdatePatRec(patient_id)

# Optional: print updated record
print("\nUpdated Record:")
print(Medlogs.get(patient_id, "No record found."))
    
    
def viewappoint():
    id= input("Enter patient ID:").strip()
    found=False
    with open("nurseinfo.txt", "r") as f:  # 假设文件名为 nurseinfo.txt
            for line in f:
                fields = line.strip().split(",")  # 用逗号分隔字段（可按实际格式修改）
                if fields and fields[0] == id:
                    print("Appointment Details:")
                    print(line.strip())
                    found = True
                    break  # 如果只要找一条匹配的记录，就可以中断
    print("❌ nurseinfo.txt file not found.")
    return

    if not found:
        print("No records found.")
    return

def Timetable():
    return