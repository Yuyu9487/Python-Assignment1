import main
import fileManager
#Patient function
# patient: [id, name, password, contant number]
def Patient():
    ID = -1
    while True:
        if ID == -1:
            print("\n============================\nPatient Menu\n============================")
            print("1.Sign In")
            print("2.Login")
            print("3.Back To Menu")
            user = input("Your Choice:")
            match user:
                case "1":
                    ID = SignIn()
                    break
                case "2":
                    ID = Login()
                    break
                case "3":
                    main.main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")
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
                    ID = MedicalRec()
                    break
                case "2":
                    ID = Pat_viewappoint()
                    break
                case "3":
                    ID = updateinfo()
                    break
                case "4":
                    ID = Paymenthistory()
                    break
                case "5":
                    main.main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")

def SignIn():
    patientInfo = fileManager.readFile("patient.txt")
    user = [input("Enter your Name: "), input("Enter your Password: "), input("Enter your Contact Number: ")]
    for user_input in user:
        if user_input == "":
            print("input can not be Null!")
            return -1
    ID = 0
    allID = []
    for info in patientInfo:
        allID.append(info[0])
    while ID < 10000:
        if ID in allID:
            ID += 1
        else:
            patientInfo.append([str(i), user[0], user[1], user[2]])
            fileManager.writeFile("patient.txt", 4, patientInfo)
            return i
    return -1

def Login():
    patientInfo = fileManager.readFile("patient.txt")
    user = [input("Enter your Name: "), input("Enter your Password: ")]
    for info in patientInfo:
        if info[1] == user[0] and info[2] == user[1]:
            return info[0]
    return -1

def view_patient_medical_records():
    return
def view_appointment():
    return
def update_info():
    patientInfo = fileManager.readFile("patient.txt")
    for info in patientInfo:
        if info[0] == user:
            print("")
            user = input("Enter your Name: ")
            user = input("Enter your Name: ")
            break
    return
def view_payment():
    return