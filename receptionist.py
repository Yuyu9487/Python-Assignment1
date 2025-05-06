import main
import fileManager

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
    Entered = False
    while Entered == False:
        checkid = fileManager.readFile("patient.txt")
        
        regid = input("Enter New Patient ID:")
        for info in checkid:
            if info[0] == regid:
                print(f"Error:ID {regid} already exist.")
                
            elif regid == "":
                print("Error:Cannot be blank.")
            elif regid.isdigit() == False:
                print("Error:ID must be number.")
            else:#next step

                regname = input("Enter Patient Name:")
                if regname == "":
                    print("Error:Name cannot be blank.")
                else:#next step
                    
                    regpass = input("Enter Patient Password:")
                    if regpass == "":
                        print("Error:Password cannot be blank.")

                    else:#nextstep
                        regcontact = input("Enter Patient Contact Number:")
                        if regcontact == "":
                            print("Error:Cannot be blank.")
                        elif regcontact.isdigit() == False:
                            print("Error:ID must be number.")
                        else:
                            Entered = True
                            
                        
    



    
    
def UpdatePatDes():
    return
def MakeAppoint():
    return
def RepPay():
    return