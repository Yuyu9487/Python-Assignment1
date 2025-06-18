import main
import fileManager
import re
#Doctor Funtion
APPOINTMENT_FILE="patient.txt"

def Doctor():
    id = -1
    print("\n============================\nDoctor Menu\n============================")
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
            print("1.Patient's Medical Records/Treatment History")
            print("2.Update Patient Record")
            print("3.View Appointment List")
            print("4.Block/Unblock Schedule")
            print("5.Back To Menu")
            user = input("Your Choice:")
            match user:
                case "1":
                    view_patient_medical_records(id)
                case "2":
                    UpdatePatientRecords(id)
                case "3":
                    ViewAppointment(id)
                case "4":
                    Appointment_Block_List(id)
                case "5":
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")

def Login():
    doctorInfo = fileManager.readFile("doctor.txt")
    userName = input("=======================\nEnter your Name: ").strip()
    userPassword = input("Enter your Password: ").strip()
    if userName == "":
        print("Error:Name connot be blank!")
        return -1
    elif userPassword == "":
        print("Error:Password connot be blank!")
        return -1
    for info in doctorInfo:
        if info[1] == userName and info[2] == userPassword:
            print("Successful login!")
            return int(info[0])
        else:
            print("Error:Enter error!")
    return -1

def view_patient_medical_records(id):
    print("="*30, "Patient", "="*30)
    fileManager.viewAllPatient()
    print("="*67)
    PatientID = input("Enter Patient ID: ").strip()
    if PatientID == "" or not PatientID.isdigit():
        print("Please enter again!")
        return
    MedicalRecords = fileManager.readFile("patient_medical_records/" + str(PatientID) + ".txt")
    if len(MedicalRecords) > 0:
        for MedicalRecord in MedicalRecords:
            print(f"Patient ID:{MedicalRecord[0]},Patient Problem:{MedicalRecord[1]},Patient Details:{MedicalRecord[2]},Medical Plan:{MedicalRecord[3]},Price:{MedicalRecord[4]},Date:{MedicalRecord[5]}")
    else:
        print("patient don't have medical records.")

def UpdatePatientRecords(id):
    print("="*30, "Patient", "="*30)
    fileManager.viewAllPatient()
    print("="*67)
    PatientID = input("Enter your ID:").strip()
    if PatientID == "" or not PatientID.isdigit():
        print("Please enter again!")
        return
    MedicalRecord=fileManager.readFile("patient_medical_records/" + PatientID + ".txt")
    PatientProblem=input("Enter the problem:")
    if PatientProblem == "":
        print("Please enter again!")
        return
    PatientDetail=input("Enter the details:")
    if PatientDetail == "":
        print("Please enter again!")
        return
    MedicalPlan=input("Enter the medical plan:")
    if MedicalPlan == "":
        print("Please enter again!")
        return
    Price=input("Enter the price:")
    if Price == "":
        print("Please enter again!")
        return
    elif Price.isdigit()==False:
        print("Please enter again!")
        return
    Date=input("Enter the date (eg: 24/4/25):")
    if not fileManager.checkDate(Date):
        print("Please enter again!")
        return
    MedicalRecord.append ([PatientID,PatientProblem,PatientDetail,MedicalPlan,Price,Date]) 
    fileManager.writeFile ("patient_medical_records/" + PatientID + ".txt", MedicalRecord)
    
def ViewAppointment(id):
    found = False
    Appointment = fileManager.readFile("Appointment.txt")
    print("="*30, "Appointment", "="*30)
    for appointment in Appointment:
        if int(appointment[1]) == id:
            print("Patient ID:", appointment[0].ljust(3), "Date:", appointment[2].ljust(9), "Start Time:", appointment[3].ljust(5), "End Time:",appointment[4].rjust(5))
            found = True
    if not found:
        print("You don't have appointment.")
    print("="*70)

def Appointment_Block_List(id):
    print("Choose a service:\n1. View block list\n2. Insert block list\n3. Delete block list")
    service = input("Enter your service number (1/2/3): ").strip()
    if service == "" or not service.isdigit():
        print("Please enter again!")
        return
    
    BlockLists = fileManager.readFile("AppointmentBlockList.txt")  # 放外面，避免后面读取不到
    found = False

    if service == "1":
        print("="*30, "Appointment Block List", "="*30)
        for blocklist in BlockLists:
            if int(blocklist[1]) == id:
                print("ID:", blocklist[0].ljust(3), "PatientID:", blocklist[1].ljust(3), "Not Available Date:", blocklist[2].ljust(9), "Start Time:", blocklist[3].ljust(5), "End Time:",blocklist[4].rjust(5))
                found = True
        if not found:
            print("No block list found for the given Doctor ID.")
        print("="*84)

    elif service == "2":
        NotAvailableDate = input("Enter the not available date (e.g. 01/12/25): ").strip()
        if not fileManager.checkDate(NotAvailableDate):
            print("Please enter again!")
            return
        NotAvailableStartTime = input("Enter the not available start time (e.g. 0900): ").strip()
        if not fileManager.checkTime(NotAvailableStartTime):
            print("Please enter again!")
            return
        NotAvailableEndTime = input("Enter the not available end time (e.g. 1200): ").strip()
        if not fileManager.checkTime(NotAvailableEndTime):
            print("Please enter again!")
            return
        blocklistID = [blocklist[0] for blocklist in BlockLists]
        new_id = 0
        while True:
            if new_id not in blocklistID:
                break
            new_id += 1
        BlockLists.append([new_id, id, NotAvailableDate, NotAvailableStartTime, NotAvailableEndTime])
        fileManager.writeFile("AppointmentBlockList.txt", BlockLists)
        print("New block added successfully.")

    elif service == "3":
        print("Current Block List:")
        for blocklist in BlockLists:
            if int(blocklist[1]) == id:
                print(f"ID: {blocklist[0]} | Date: {blocklist[2]} | Start: {blocklist[3]} | End: {blocklist[4]}")
        
        delete_id = input("Enter the Block ID you want to delete: ").strip()
        if delete_id == "" or not delete_id.isdigit():
            print("Please enter again!")
            return
        BlockLists = [item for item in BlockLists if item[0] != delete_id or int(item[1]) != id]
        fileManager.writeFile("AppointmentBlockList.txt", BlockLists)
        print(f"Block ID {delete_id} deleted (if it existed).")

    else:
        print("Invalid service choice.")
    return