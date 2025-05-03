import main

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
                    main.main()
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