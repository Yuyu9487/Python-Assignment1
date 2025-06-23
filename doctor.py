import fileManager #to save data, record data, view data, format

def Doctor():
    id = -1 #no one login yet
    print("\n============================\nDoctor Menu\n============================")
    while True:
        if id == -1:
            print("1.login")
            print("2.Back To Menu")
            user = input("Your Choice:").strip() #strip means to remove the extra spaces 
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
                    view_patient_medical_records(id) #the argument id is to save the data
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
    doctorInfo = fileManager.readFile("doctor.txt") #read the file from "doctor.txt" and save in doctorInfo and record in fileManager
    userName = input("=======================\nEnter your Name: ").strip()
    userPassword = input("Enter your Password: ").strip()
    if userName == "":
        print("Error:Name cannot be blank!")
        return -1
    elif userPassword == "":
        print("Error:Password cannot be blank!")
        return -1
    for info in doctorInfo:
        if info[1] == userName and info[2] == userPassword:
            print("Successful login!")
            return int(info[0])
    print("Error:Enter error!")
    return -1 #back to main menu

def view_patient_medical_records(id):
    print("="*30, "Patient", "="*30)
    fileManager.viewAllPatient() #save the data in viewAllPatient and record in fileManager
    print("="*67)
    found = False
    PatientID = input("Enter Patient ID: ").strip()
    if PatientID == "" or not PatientID.isdigit():
        print("Please enter again!")
        return
    MedicalRecords = fileManager.readFile("patient_medical_records/" + str(PatientID) + ".txt") #read file from "patient_medical_records.txt" and save data in MedicalRecords and record in fileManager
    print ("="*30, "Patient", "="*30)
    for MedicalRecord in MedicalRecords:
        print("Patient ID:", MedicalRecord[0].ljust(3), "Patient Problem:", MedicalRecord[1].ljust(3), "Patient Details:", MedicalRecord[2].ljust(9), "Price:", MedicalRecord[3].ljust(5), "Date:", MedicalRecord[4].rjust(5)) #if the id is matched
        found = True
    if not found:
        print("Patient don't have medical records.")
    print("="*67)

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
    if not fileManager.checkDate(Date): #if the format  is not following the format in fileManager, it will return to the main menu
        print("Please enter again!")
        return
    MedicalRecord.append ([PatientID,PatientProblem,PatientDetail,MedicalPlan,Price,Date]) #if the data format  is matched, then it will save in MedicalRecord
    fileManager.writeFile ("patient_medical_records/" + PatientID + ".txt", MedicalRecord) #if the data format is correct, it will write file in "patient_medical_records.txt" and record in fileManager
    
def ViewAppointment(id):
    found = False
    Appointment = fileManager.readFile("Appointment.txt")
    print("="*30, "Appointment", "="*30)
    for appointment in Appointment:
        if int(appointment[1]) == id: #if id is matched
            print("Patient ID:", appointment[0].ljust(3), "Date:", appointment[2].ljust(9), "Start Time:", appointment[3].ljust(5), "End Time:",appointment[4].rjust(5))
            found = True
    if not found:
        print("You don't have appointment.")
    print("="*70)

def Appointment_Block_List(id): #if doctor id and patient id is matched
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
            if int(blocklist[1]) == id: #if the id  is matched, it will display below things
                print("ID:", blocklist[0].ljust(3), "Not Available Date:", blocklist[2].ljust(9), "Start Time:", blocklist[3].ljust(5), "End Time:",blocklist[4].rjust(5))
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
        blocklistID = [int(blocklist[0]) for blocklist in BlockLists] 
        new_id = 0
        while True:
            if new_id not in blocklistID:
                break
            new_id += 1
        BlockLists.append([new_id, id, NotAvailableDate, NotAvailableStartTime, NotAvailableEndTime]) #if the id is not found in data, then it will create a new id for  it 
        fileManager.writeFile("AppointmentBlockList.txt", BlockLists)
        print("New block added successfully.")

    elif service == "3":
        print("Current Block List:") #the user can choose the block list based on the options
        for blocklist in BlockLists:
            if int(blocklist[1]) == id:
                print(f"ID: {blocklist[0]} | Date: {blocklist[2]} | Start: {blocklist[3]} | End: {blocklist[4]}")
        
        delete_id = input("Enter the Block ID you want to delete: ").strip()
        if delete_id == "" or not delete_id.isdigit():
            print("Please enter again!")
            return
        BlockLists = [item for item in BlockLists if item[0] != delete_id] #if the condition is match, it will record the data. if the condition is not maatch, it will not save
        fileManager.writeFile("AppointmentBlockList.txt", BlockLists)
        print(f"Block ID {delete_id} deleted (if it existed).")

    else:
        print("Invalid service choice.")
    return