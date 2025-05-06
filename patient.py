import main
import fileManager
#Patient function
def Patient():
    print("1.Sign In")
    print("2.Login")
    print("\n============================\nPatient Menu\n============================")
    print("1.View Personal Medical Records")
    print("2.View Appointment")
    print("3.Update Infomation")
    print("4.Access Billing Details And Payment History")
    print("5.Back To Menu")
    while True:
        user = input("Your Choice:")
        match user:
            case "1":
                SignIn()
                break
            case "2":
                Login()
                break
            case _:
                print("Error. Please Enter A Valid Input.")

def SignIn():
    patientInfo = fileManager.readFile("patient.txt")
    user = [input("Enter your Name: "), input("Enter your Password: "), input("Enter your Contact Number: ")]
    i = 0
    allID = []
    for info in patientInfo:
        allID.append(info[0])
    while i < 10000:
        if i in allID:
            i += 1
        else:
            patientInfo.append([str(i), user[0], user[1], user[2]])
            fileManager.writeFile("patient.txt", 4, patientInfo)
            break

def Login():
    patientInfo = fileManager.readFile("patient.txt")
    user = [input("Enter your Name: "), input("Enter your Password: ")]
def MedicalRec():
    return
def Pat_viewappoint():
    return
def updateinfo():
    patientInfo = fileManager.readFile("patient.txt")
    user = input("Enter your ID: ")
    for info in patientInfo:
        if info[0] == user:
            user = input("Enter your Name: ")
    return
def Paymenthistory():
    return