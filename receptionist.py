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

        regpass = input("Enter Patient Password:")
        if regpass == "":
            print("Error:Password cannot be blank.")
            break

        regage = input("Enter Patient Age:")
        if regage == "":
            print("Error:Age cannot be blank.")
            break
        elif regage.isdigit() == False:
            print("Error:Age must be number.")
            break

        regcontact = input("Enter Patient Contact Number:")
        if regcontact == "":
            print("Error:Contact Number Cannot be blank.")
            break
        elif regcontact.isdigit() == False:
            print("Error:Contact Number must be number.")
            break

        regaddress = input("Enter Patient Address:")
        if regaddress == "":
            print("Error:Address Cannot be blank.")
            break

        i = 0
        allID = []
        for info in patfile:
            allID.append(int(info[0]))
        while i < 10000:
            if i in allID:
                i += 1
            else:
                Entered = True
                patfile.append([str(i), regname, regpass, regage, regcontact, regaddress])
                fileManager.writeFile("patient.txt", 6, patfile)
                print(f"Patient ID: {i} added successfully!")
                
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
                user = input("============================\nWhat would you like to Update?\n1.Name\n2.Password\n3.Age\n4.Contact Number\n5.Address\n6.Abort\nYour Choice:")
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
                    update = input("Enter Patient Age:")
                elif user ==4:
                    update = input("Enter Patient Contact Number:")
                elif user ==5:
                    update = input("Enter Patient Address:")
                elif user ==6:
                    print("Bringing you back to receptionist menu...")
                else:
                    print("Invalid Response, Please try again.")
                    

                if update == "":
                    print("Error:Input cannot be blank.")
                elif info[user] == update:
                    print("Error, new value must be different from old value.")
                elif user ==3 and update.isdigit() == False:
                    print("Age must be digits.")
                elif user ==4 and update.isdigit() == False:
                    print("Contact Number must be digits.")
                else:
                    confirm = input(f"============================\nSystem will be overwrite [{info[user]}] with [{update}].\n1.Confirm\n2.Abort\nAre you sure?:")
                    
                    
                    match confirm:
                        case "1":
                            patientInfo.remove([info[0], info[1], info[2], info[3], info[4], info[5]])
                            info[user] = update
                            patientInfo.append([info[0], info[1], info[2], info[3], info[4], info[5]])
                            fileManager.writeFile("patient.txt", 6, patientInfo)
                            print("Updated")
                                
                        case "2":
                             print("Bringing you back to receptionist menu...")
                                
                        case _:
                            print("Error, Invalid Input.")

        if userid != info[0]: 
            print(f"Error, Patient ID {userid} does not exist.")
    Receptionist()

def MakeAppoint():
    print("============================")
    patientId = input("Enter Patient ID: ")
    doctorId = input("Enter Doctor ID: ")
    Appointment_fuction(patientId, doctorId)

def Appointment_fuction(patientId, doctorId, patientName = None, doctorName = None):
    if patientId == "" or patientId.isdigit() == False:
        print("Invalid input, ID must be digits and cannot be null.")
        Receptionist()
        return
    if doctorId == "" or doctorId.isdigit() == False:
        print("Invalid input, ID must be digits and cannot be null.")
        Receptionist()
        return
    
    patientName, doctorName = patientName, doctorName
    if patientName == None or doctorName == None:
        patientInfo, doctorInfo = fileManager.readFile("patient.txt"), fileManager.readFile("doctor.txt")
        for info in patientInfo:
            if info[0] == patientId:
                patientName = info[1]
        for info in doctorInfo:
            if info[0] == doctorId:
                doctorName = info[1]
        if patientName == None:
            print(f"Error: Patient ID {patientId} can't be found.")
            return
        elif doctorName == None:
            print(f"Error: Doctor ID {doctorId} can't be found.")
            return
    
    user = input("============================\nWhat would you like to do?\n1.Schedule Appointment\n2.View Appointment\n3.Cancel Appointment\n4.Abort\nYour Choice:")
    if user == "" or user.isdigit() == False:
        print("Invalid input, ID must be digits and cannot be null.")
        Appointment_fuction(patientId, doctorId, patientName, doctorName)
    else:
        user = int(user)
    match user:
        case 1:
            scheduleAppointment(patientId, doctorId, patientName, doctorName)
        case 2:
            viewAppointment(patientId, doctorId, patientName, doctorName)
        case 3:
            cancelAppointment(patientId, doctorId, patientName, doctorName)
        case 4:
            print("Bringing you back to receptionist menu...")
            Receptionist()
    Receptionist()

def scheduleAppointment(patientId, doctorId, patientName, doctorName):
    date = input("============================\nEnter the date in DD/MM/YY(ex:06/09/25),seperated by '/'.:")
    datepattern = ("^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})$")
    startTime = input("Enter the starting time of the appointment in [24 hour format](ex:0945)")
    endTime = input("Enter the end time of the appointment in [24 hour format](ex:2300)")
    timepattern = ("^([01][0-9]|[2][0-3])([05][0-9])")
    if not re.match(datepattern,date):
        raise ValueError("Date does not match DD/MM/YY format or input is invalid")
        Appointment_fuction(patientId, doctorId, patientName, doctorName)
        return
    if re.match(timepattern,startTime) and re.match(timepattern,endTime):
        startTime, endTime = int(startTime), int(endTime)
        if endTime <= startTime:
            print("Error: End time cannot be same or early than starting time.")
            Appointment_fuction(patientId, doctorId, patientName, doctorName)
            return

        Appointmentblock = fileManager.readFile("AppointmentBlockList.txt")
        Appointment = fileManager.readFile("Appointment.txt")

        for appointInfo in Appointment:
            if date == appointInfo[2] and startTime < int(appointInfo[4]) and endTime > int(appointInfo[3]):
                if patientId == appointInfo[0]:
                    print(f"Error: Patient {patientName} have Appointment at [{date}]!")
                    Appointment_fuction(patientId, doctorId, patientName, doctorName)
                    return
                elif doctorId == appointInfo[1]:
                    print(f"Error: Doctor {doctorName} have Appointment at [{date}]!")
                    Appointment_fuction(patientId, doctorId, patientName, doctorName)
                    return

        for appointBlockInfo in Appointmentblock:
            if doctorId == appointBlockInfo[0] and date == appointBlockInfo[1]:
                print(f"Error: Doctor {doctorName} has this date [{date}] blocked for appointment.")
                Appointment_fuction(patientId, doctorId, patientName, doctorName)
                return

        #already check all, and no repeating date are found
        print(f"Appointment made for [{patientName}] at [{date}] successfully!")
        
        Appointment.append([patientId, doctorId, date, startTime, endTime])
        fileManager.writeFile("Appointment.txt", 5, Appointment)
    else:
        raise ValueError("Start/End time does not match XX:XX format or input is invalid")
    Appointment_fuction(patientId, doctorId, patientName, doctorName)

def viewAppointment(patientId, doctorId, patientName, doctorName):
    Appointments = fileManager.readFile("Appointment.txt")
    print("\n" + "=" * 24 + " Appointment " + "=" * 24)
    print("Patient name: ", patientName)
    print("Doctor name: ", doctorName)
    totalAppointment = 0
    for Appointment in Appointments:
        if Appointment[0] == patientId and Appointment[1] == doctorId:
            totalAppointment += 1
            print("Number:", str(totalAppointment).ljust(3), "Date:", Appointment[2].ljust(9), "Start Time:", Appointment[3].ljust(5), "End Time:", Appointment[4])
    print(f"Total appointment: {totalAppointment}")
    print("=" * 61 + "\n")
    Appointment_fuction(patientId, doctorId, patientName, doctorName)

def cancelAppointment(patientId, doctorId, patientName, doctorName):
    Appointments = fileManager.readFile("Appointment.txt")
    myAppointments = []

    print("\n" + "=" * 21 + " Cancel Appointment " + "=" * 21)
    print("Patient name: ", patientName)
    print("Doctor name: ", doctorName)
    for Appointment in Appointments:
        if patientId in Appointment[0] and doctorId in Appointment[1]:
            myAppointments.append(Appointment)
            print("Number:", str(len(myAppointments)).ljust(3), "Date:", Appointment[2].ljust(9), "Start Time:", Appointment[3].ljust(6), "End Time:", Appointment[4].ljust(6))
    print(f"Total appointment: {len(myAppointments)}")
    print("=" * 62)

    cancelNumber = input("Please enter the appointment number that you want to cancel: ")
    if cancelNumber == "" or not cancelNumber.isdigit():
        print("Invalid input, ID must be digits and cannot be null.")
        Appointment_fuction(patientId, doctorId, patientName, doctorName)
        return
    cancelNumber = int(cancelNumber)

    print(f"Cancel Appointment at [{myAppointments[cancelNumber - 1][2]}] for Patient [{myAppointments[cancelNumber - 1][0]}] and Doctor [{myAppointments[cancelNumber - 1][1]}] successfully.")
    Appointments.remove(myAppointments[cancelNumber - 1])
    fileManager.writeFile("Appointment.txt", 5, Appointments)
    Appointment_fuction(patientId, doctorId, patientName, doctorName)

def RepPay():   
    userid = input("============================\nEnter Patient ID: ")
    if userid == "" or userid.isdigit() == False:
        print("Invalid input, ID must be digits and cannot be null.")
        Receptionist()
    paymentfuction(userid)

def paymentfuction(userid):
    patientInfo = fileManager.readFile("patient.txt")
    for info in patientInfo:
        if info[0] == userid:
            print(f"Patient [{info[1]}] Payment List.")
            user = input("============================\nWhat would you like to do?\n1.Add outstanding amount.\n2.Process payemnt.\n3.Abort\nYour Choice:")
            if user == "" or user.isdigit() == False:
                print("Invalid input, ID must be digits and cannot be null.")
                paymentfuction(userid)
            user = int(user)

            match user:
                case 1:
                    price = input("How much does the patient has to pay?")
                    if price == "":
                        print("Error:Price cannot be blank.")
                        paymentfuction(userid)
                    elif price.isdigit() == False:
                        print("Error:Price must be number.")
                        paymentfuction(userid)
                    payment = fileManager.readFile("payment.txt")
                    id = 0
                    for payid in payment:
                        if userid == payid[0]:
                            id += 1
                            
                    payment.append([info[0],str(id),"RM"+price,"No"])
                    print(payment)
                    fileManager.writeFile("payment.txt", 4, payment)
                    print("Added Successfully!")
                    paymentfuction(userid)
                    











 #                               priceid = input("Enter the ID of payment you wish to change:")
  #                              display.append[paymentinfo]
#
 #                       if display == []:
  #                          print(f"Patient {info[1]} doesn't have any upcoming payments.")
   #                     else:
    #                        print(f"Patient {info[1]} has appointment(s) at {display}.")

                                


