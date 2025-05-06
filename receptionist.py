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
        patfile = fileManager.readFile("patient.txt")
        
        regid = input("Enter New Patient ID:")
        for info in patfile:
            if info[0] == regid:
                print(f"Error:ID {regid} already exist.")
                break
            elif regid == "":
                print("Error:Cannot be blank.")
                break
            elif regid.isdigit() == False:
                print("Error:ID must be number.")
                break
            else:#next step

                regname = input("Enter Patient Name:")
                if regname == "":
                    print("Error:Name cannot be blank.")
                    break
                else:#next step
                    
                    regpass = input("Enter Patient Password:")
                    if regpass == "":
                        print("Error:Password cannot be blank.")
                        break

                    else:#nextstep
                        regcontact = input("Enter Patient Contact Number:")
                        if regcontact == "":
                            print("Error:Cannot be blank.")
                            break
                        elif regcontact.isdigit() == False:
                            print("Error:Contact Number must be number.")
                            break
                        else:
                            Entered = True
                            patfile.append([regid, regname, regpass, regcontact])
                            fileManager.writeFile("patient.txt", 4, patfile)
                            print("Patient added successfully!")
                            Receptionist()
                            break

def UpdatePatDes():
    
    return
def MakeAppoint():
    return
def RepPay():
    return