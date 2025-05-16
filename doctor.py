import main
import fileManager
#Doctor Funtion
APPOINTMENT_FILE="patient.txt"

def Doctor():
    print("\n============================\nDoctor Menu\n============================")
    print("1.Patient's Medical Records/Treatment History\n2.Update Patient Record\n3.View Appointment List\n4.Block/Unblock Schedule\n5.Back To Menu")
    while True:
        user = input("Your Choice:")
        match user:
                case "1":
                    view_patient_medical_records()
                    break
                case "2":
                    UpdatePatientRecords()
                    break
                case "3":
                    ViewAppointment()
                    break
                case "4":
                    Timetable()
                    break
                case "5":
                    main.main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")

def view_patient_medical_records():
    PatientID = input("Enter Patient ID: ").strip()
    found = False
    MedicalRecords = fileManager.readFile("patient_medical_records/" + str(PatientID) + ".txt")
    for MedicalRecord in MedicalRecords:
        print(f"Patient ID:{MedicalRecord[0]},Patient Problem:{MedicalRecord[1]},Patient Details:{MedicalRecord[2]},Medical Plan:{MedicalRecord[3]},Price:{MedicalRecord[4]},Date:{MedicalRecord[5]}")

def UpdatePatientRecords():
    PatientID=int(input("Enter your ID:"))
    MedicalRecord=fileManager.readFile("patient_medical_records/" + str(PatientID) + ".txt")
    PatientProblem=input("Enter the problem:")
    PatientDetail=input("Enter the details:")
    MedicalPlan=input("Enter the medical plan:")
    Price=input("Enter the price:")
    Date=input("Enter the date:")
    MedicalRecord.append ([PatientID,PatientProblem,PatientDetail,MedicalPlan,Price,Date]) 
    fileManager.writeFile ("patient_medical_records/", 6 , MedicalRecord)
    
def ViewAppointment():
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

def Timetable():
    return