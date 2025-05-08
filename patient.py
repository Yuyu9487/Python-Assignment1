import main
import fileManager
#Patient function
def Patient(input_ID = -1):
    ID = input_ID
    while True:
        if ID == -1:
            print("\n============================\nPatient Login Menu\n============================")
            print("1.Login")
            print("2.Back To Menu")
            user = input("Your Choice:")
            match user:
                case "1":
                    ID = Login()
                case "2":
                    main.main()
                    break
                case _:
                    print("\nError. Please Enter A Valid Input.\n")
        else:
            print("\n============================\nPatient Menu\n============================")
            print("1.View Personal Medical Records")
            print("2.View Appointment")
            print("3.Update Infomation")
            print("4.Access Billing Details And Payment History")
            print("5.Back To Menu")
            user = input("Your Choice:")
            match user:
                case "1":
                    view_patient_medical_record(ID)
                    break
                case "2":
                    view_appointment(ID)
                    break
                case "3":
                    update_info(ID)
                    break
                case "4":
                    view_payment(ID)
                    break
                case "5":
                    main.main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")

def Login():
    patientInfo = fileManager.readFile("patient.txt")
    userName = input("\nEnter your Name: ")
    userPassword = input("Enter your Password: ")
    if userName == "":
        print("\nError:Name connot be blank!\n")
        return -1
    elif userPassword == "":
        print("\nError:Password connot be blank!\n")
        return -1
    for info in patientInfo:
        if info[1] == userName and info[2] == userPassword:
            print("\nSuccessful login!\n")
            return info[0]
        else:
            print("\nError:Enter error!\n")
    return -1

def view_patient_medical_record(ID):
    patient_medical_record_info = fileManager.readFile("patient_medical_records/" + ID + ".txt")
    return

def view_appointment(ID):
    return

def update_info(ID):
    patientInfo = fileManager.readFile("patient.txt")
    for i in range(0, len(patientInfo)):
        if patientInfo[i][0] == ID:
            user = int(input("\nWhat would you like to Update?\n1.Name\n2.Password\n3.Contact Number\n4.Abort\nYour Choice:"))
            match user:
                case 1:
                    update = input("\nEnter Patient Name:")
                case 2:
                    update = input("\nEnter Patient Password:")
                case 3:
                    update = input("\nEnter Patient Contact Number:")
                case _:
                    Patient(ID)

            if update == "":
                print("\nError:Input cannot be blank.")
            else:
                confirm = input(f"\nSystem will be overwrite {patientInfo[i][user]} with {update}.\n1.Confirm\n2.Abort\nAre you sure?:")
                match confirm:
                    case "1":
                        patientInfo[i][user] = update
                        fileManager.writeFile("patient.txt", 4, patientInfo)
                        print("\nUpdated Sussessful!")
                        Patient(ID)
                    case _:
                        Patient(ID)
            break
    return

def view_payment(ID):
    return