import main
import fileManager
import re
#Receptionist function
def Receptionist():
    print("\n============================\nReceptionist Menu\n============================")
    print("1.Register New Patient\n2.Update Patient Details\n3.Appointment Fuctions For Patient\n4.Process Payemnt\n5.Back To Menu")
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
                            fileManager.writeFile("patient.txt", 4, patfile)
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
                    print("Bringing you back to receptionist menu...")
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
                             print("Bringing you back to receptionist menu...")
                                
                        case _:
                            print("Error, Invalid Input.")
                                

        if userid != info[0]: 
            print(f"Error, Patient ID {userid} does not exist.")
            
    Receptionist()

def MakeAppoint():
    userid = input("============================\nEnter Patient ID: ")
    Appointment_fuction(userid)

def Appointment_fuction(userid):
    patientInfo = fileManager.readFile("patient.txt")
    if userid == "" or userid.isdigit() == False:
        print("Invalid input, ID must be digits and cannot be null.")
        Receptionist()
    else:
        for info in patientInfo:
            if info[0] == userid:
                print(f"Patient [{info[1]}] Appointment List.")
                user = input("============================\nWhat would you like to do?\n1.Schedule Appointment\n2.View Patient's Appointment\n3.Cancel Appointment\n4.Abort\nYour Choice:")
                if user == "" or user.isdigit() == False:
                    print("Invalid input, ID must be digits and cannot be null.")
                    Appointment_fuction(userid)
                else:
                    user = int(user)
                match user:
                    case 1:
                        date = input("============================\nEnter the date in DD/MM/YY(ex:06/09/25),seperated by '/'.:")
                        pattern = ("^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})$")
                        try: 
                            if re.match(pattern,date):
                                Appointmentblock = fileManager.readFile("AppointmentBlockList.txt")
                                Appointment = fileManager.readFile("Appointment.txt")

                                for appointinfo in Appointment:
                                    if date in appointinfo[1] and userid in appointinfo[0]:
                                        print(f"Error: Appointment at [{date}] already exist.")
                                        Appointment_fuction(userid)
                                        break

                                for dateinfo in Appointmentblock:
                                    if date in dateinfo[0]:
                                        print(f"Error: Doctor has this date [{date}] blocked for appointment.")
                                        Appointment_fuction(userid)
                                        break

                                #already check all, and no repeating date are found
                                print(f"Appointment made for [{info[1]}] at [{date}] successfully!")
                                
                                Appointment.append([info[0],date])
                                fileManager.writeFile("Appointment.txt", 2, Appointment)
                                Appointment_fuction(userid)


                            else:
                                raise ValueError("Date does not match DD/MM/YY format or input is invalid")
                        except ValueError as Error:
                            print(Error)
                            Appointment_fuction(userid)

                    case 2:
                        Appointment = fileManager.readFile("Appointment.txt")
                        display = []
                        for appointinfo in Appointment:
                            if userid == appointinfo[0]:
                                display.append(appointinfo[1])
                        if display == []:
                            print(f"Patient {info[1]} doesn't have any upcoming appointments.")
                        else:
                            print(f"Patient {info[1]} has appointment(s) at {display}.")
                        Appointment_fuction(userid)
                    
                    case 3:
                        date = input("============================\nEnter the date in DD/MM/YY(ex:06/09/25),seperated by '/'.:")
                        pattern = ("^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})$")
                        try: 
                            if re.match(pattern,date):
                                Appointmentblock = fileManager.readFile("AppointmentBlockList.txt")
                                Appointment = fileManager.readFile("Appointment.txt")

                                for appointinfo in Appointment:
                                    if date in appointinfo[1] and userid in appointinfo[0]:
                                        print(f"Cancel Appointment at [{date}] for [{info[1]}] successfully.")
                                        Appointment.remove([appointinfo[0],appointinfo[1]])
                                        fileManager.writeFile("Appointment.txt", 2, Appointment)
                                        Appointment_fuction(userid)
                                        break
                                print(f"Patient [{info[1]}] doesn't have the following appointment at [{date}]")
                                Appointment_fuction(userid)

                            else:
                                raise ValueError("Date does not match DD/MM/YY format or input is invalid")
                        except ValueError as Error:
                            print(Error)
                            Appointment_fuction(userid)
                    case 4:
                        print("Bringing you back to receptionist menu...")
                        Receptionist()
            break
        print(f"Error: Patient ID {userid} can't be found.")
        Receptionist()
    return
def RepPay():
    return