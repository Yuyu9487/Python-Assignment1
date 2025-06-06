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
                
                case "2":
                    UpdatePatientRecords()
                  
                case "3":
                    ViewAppointment()
                  
                case "4":
                    Appointment_Block_List()

                case "5":
                    main.main()

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
    fileManager.writeFile ("patient_medical_records/" + str(PatientID) + ".txt", 6 , MedicalRecord)
    
def ViewAppointment():
    PatientID = input("Enter Patient ID: ").strip()
    found = False
    Appointment = fileManager.readFile("Appointment.txt")
    for appointment in Appointment:
        if appointment[0] == PatientID:
            print(f"PatientID: {appointment[0]}, Doctor ID: {appointment[1]}, Date: {appointment[2]}, Start Time: {appointment[3]}, End Time: {appointment[4]}")
            found = True
    if not found:
        print("No appointment found for the given Patient ID.")
    return

def Appointment_Block_List():
    DoctorID = input("Enter Doctor ID: ").strip()
    print("Choose a service:\n1. View block list\n2. Insert block list\n3. Delete block list")
    service = input("Enter your service number (1/2/3): ").strip()
    
    BlockLists = fileManager.readFile("AppointmentBlockList.txt")  # 放外面，避免后面读取不到
    found = False

    if service == "1":
        for blocklist in BlockLists:
            if blocklist[1] == DoctorID:
                print(f"ID: {blocklist[0]} | PatientID: {blocklist[1]} | Not Available Date: {blocklist[2]} | Start Time: {blocklist[3]} | End Time: {blocklist[4]}")
                found = True
        if not found:
            print("No block list found for the given Doctor ID.")

    elif service == "2":
        NotAvailableDate = input("Enter the not available date (e.g. 2024-12-01): ").strip()
        NotAvailableStartTime = input("Enter the not available start time (e.g. 09:00): ").strip()
        NotAvailableEndTime = input("Enter the not available end time (e.g. 12:00): ").strip()
        new_id = str(len(BlockLists) + 1)
        BlockLists.append([new_id, DoctorID, NotAvailableDate, NotAvailableStartTime, NotAvailableEndTime])
        fileManager.writeFile("AppointmentBlockList.txt", 5, BlockLists)
        print("New block added successfully.")

    elif service == "3":
        print("Current Block List:")
        for blocklist in BlockLists:
            if blocklist[1] == DoctorID:
                print(f"ID: {blocklist[0]} | Date: {blocklist[2]} | Start: {blocklist[3]} | End: {blocklist[4]}")
        
        delete_id = input("Enter the Block ID you want to delete: ").strip()
        BlockLists = [item for item in BlockLists if item[0] != delete_id or item[1] != DoctorID]
        fileManager.writeFile("AppointmentBlockList.txt", 5, BlockLists)
        print(f"Block ID {delete_id} deleted (if it existed).")

    else:
        print("Invalid service choice.")
    return