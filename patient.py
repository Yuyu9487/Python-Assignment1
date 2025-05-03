import main
import fileManager
#Patient function
def Patient():
    print("\n============================\nPatient Menu\n============================")
    print("1.View Personal Medical Records\n2.View Appointment\n3.Update Infomation\n4.Access Billing Details And Payment History\n5.Back To Menu")
    while True:
        user = input("Your Choice:")
        match user:
                case "1":
                    MedicalRec()
                    break
                case "2":
                    Pat_viewappoint()
                    break
                case "3":
                    updateinfo()
                    break
                case "4":
                    Paymenthistory()
                    break
                case "5":
                    main.main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")

def MedicalRec():
    return
def Pat_viewappoint():
    return
def updateinfo():
    patientInfo = fileManager.readFile("patient.txt")
    # data = [(id, name, contact)]
    print(patientInfo[0])
    print(patientInfo[1])
    return
def Paymenthistory():
    return