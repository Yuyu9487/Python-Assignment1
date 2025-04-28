def main():
    print("\n============================\nWelcome to Best Clinic!\n============================")
    print("1.Receptionist\n2.Doctor\n3.Nurse\n4.Patient\n5.Leave")
    while True:
        user = input("Enter Your Role:")
        match user:
            case "1":
                Receptionist()
                break
            case "2":
                Doctor()
                break
            case "3":
                Nurse()
                break
            case "4":
                Patient()
                break
            case "5":
                print("See You again!")
                break
            case _:
                print("Role not found, Please try again.")
#Receptionist function
def Receptionist():
    print("\n============================\nReceptionist Menu\n============================")
    print("1.Register New Patient\n2.Update Patient Details\n3.Schedule Appointment For Patient\n4.Process Payemnt\n5.Back To Menu")
    while True:
        user = input("Your Choice:")
        match user:
                case "1":
                    Register()
                    break
                case "2":
                    UpdatePatDes()
                    break
                case "3":
                    MakeAppoint()
                    break
                case "4":
                    RepPay()
                    break
                case "5":
                    main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")
def Register():
    return
def UpdatePatDes():
    return
def MakeAppoint():
    return
def RepPay():
    return

    

#Doctor Funtion
def Doctor():
    print("\n============================\nDoctor Menu\n============================")
    print("1.Patient's Medical Logs/Treatment History\n2.Update Patient Record\n3.View Appointment List\n4.Block/Unblock Schedule\n5.Back To Menu")
    while True:
        user = input("Your Choice:")
        match user:
                case "1":
                    Medlogs()
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
                    main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")
def Medlogs():
    return
def UpdatePatRec():
    return
def viewappoint():
    return
def Timetable():
    return



#Nurse Functions
def Nurse():
    print("\n============================\nNurse Menu\n============================")
    print("1.View Doctor's Appointment\n2.Record Patient's Observation\n3.View Prescriptions\n4.Administer Medicine To Patients\n5.Back To Menu")
    while True:
        user = input("Your Choice:")
        match user:
                case "1":
                    viewdocappoint()
                    break
                case "2":
                    Recpatient()
                    break
                case "3":
                    viewprescript()
                    break
                case "4":
                    Givemeds()
                    break
                case "5":
                    main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")

def viewdocappoint():
    return
def Recpatient():
    return
def viewprescript():
    return
def Givemeds():
    return

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
                    main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")
def MedicalRec():
    return
def Pat_viewappoint():
    return
def updateinfo():
    return
def Paymenthistory():
    return

main()