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
        appointment = fileManager.readFile("Appointment.txt")
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
                    i = 0
                    allID = []
                    for info in patfile:
                        allID.append(int(info[0]))
                    while i < 10000:
                        if i in allID:
                            i += 1
                        else:
                            Entered = True
                            patfile.append([str(i), regname, regpass, regcontact])
                            appointment.append([str(i),"Null"])
                            fileManager.writeFile("patient.txt", 4, patfile)
                            fileManager.writeFile("Appointment.txt",2,appointment)
                            print(f"Patient ID: {i} added successfully!")
                            
                            break
                    break
    Receptionist()

def UpdatePatDes():
    patientInfo = fileManager.readFile("patient.txt")
    userid = input("============================\nEnter your ID: ")
    if userid == "" or userid.isdigit() == False:
        print("Invalid input, ID must be digits and cannot be null.")
    else:
        for info in patientInfo:
            if info[0] == userid:
                print(f"User {info[1]} found.")
                user = input("============================\nWhat would you like to Update?\n1.Name\n2.Password\n3.Contact Number\n4.Abort\nYour Choice:")
                if user == "" or user.isdigit() == False:
                    print("Invalid input, ID must be digits and cannot be null.")
                    Receptionist()
                else:
                    user = int(user)
                if user == 1:
                    update = input("Enter Patient Name:")
                elif user ==2:
                    update = input("Enter Patient Password:")
                elif user ==3:
                    update = input("Enter Patient Contact Number:")
                elif user ==4:
                    print("Bring you back to receptionist menu...")
                else:
                    print("Invalid Response, Please try again.")
                    

                if update == "":
                    print("Error:Input cannot be blank.")
                elif info[user] == update:
                    print("Error, new value must be different from old value.")
                else:
                    confirm = input(f"============================\nSystem will be overwrite [{info[user]}] with [{update}].\n1.Confirm\n2.Abort\nAre you sure?:")
                    
                    
                    match confirm:
                        case "1":
                            patientInfo.remove([info[0], info[1], info[2], info[3]])
                            info[user] = update
                            patientInfo.append([info[0], info[1], info[2], info[3]])
                            fileManager.writeFile("patient.txt", 4, patientInfo)
                            print("Updated")
                                
                        case "2":
                             print("Bring you back to receptionist menu...")
                                
                        case _:
                            print("Error, Invalid Input.")
                                

        if userid != info[0]: 
            print(f"Error, Patient ID {userid} does not exist.")
            
    Receptionist()

def MakeAppoint():
    patientInfo = fileManager.readFile("Appointment.txt")
    userid = input("============================\nEnter Patient ID: ")
    if userid == "" or userid.isdigit() == False:
        print("Invalid input, ID must be digits and cannot be null.")
    else:
        for info in patientInfo:
            if info[0] == userid:
                print(f"User found.")
                user = input("============================\nWhat would you like to do?\n1.Schedule Appointment\n2.View Patient's Appointment\n3.Cancel Appointment\n4.Abort\nYour Choice:")
                if user == "" or user.isdigit() == False:
                    print("Invalid input, ID must be digits and cannot be null.")
                    Receptionist()
                else:
                    user = int(user)


                if user == 1:
                    date = input("Enter the date in DD/MM/YY,seperated by '/'")
                    

                    if info[1] == "Null":
                        info[2] = []
                elif user ==2:
                    update = input("Enter Patient Password:")
                elif user ==3:
                    update = input("Enter Patient Contact Number:")
                elif user ==4:
                    print("Bring you back to receptionist menu...")
                else:
                    print("Invalid Response, Please try again.")

    print("Hello")
    return
def RepPay():
    return