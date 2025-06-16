import fileManager

#Receptionist function
def Receptionist():
    while True:
        print("\n============================\nReceptionist Menu\n============================")
        print("1.Register Individuals\n2.Update Details\n3.Schedule Appointment For Patient\n4.Process Payment\n5.Back To Menu")
        user = input("Your Choice:")
        match user:
            case "1":
                RegisterMenu()
            case "2":
                UpdateDetailMenu()
            case "3":
                MakeAppoint()
            case "4":
                RepPay()
            case "5":
                print("Bringing you back...")
                break
            case _:
                print("Error: Please Enter A Valid Input.")
                
def RegisterMenu():
    while True:
        user = input("============================\nRegister Menu\n1.Patient\n2.Doctor\n3.Nurse\n4.Abort\nYour Choice:")
        match user:
            case "1":
                Registerindividual("Patient")
            case "2":
                Registerindividual("Doctor")
            case "3":
                Registerindividual("Nurse")
            case "4":
                print("Bringing you back...")
                break
            case _:
                print("Error: Invalid Input")
            
def Registerindividual(individual):
    Entered = False
    while Entered == False:
        match individual:
            case "Patient":
                file = "patient.txt"
            case "Doctor":
                file = "doctor.txt"
            case "Nurse":
                file = "nurse.txt"

        readfile = fileManager.readFile(file)

        registerName = input(f"Enter {individual} Name:")
        if registerName == "":
            print("Error:Name cannot be blank.")
            break

        registerPassword = input(f"Enter {individual} Password:")
        if registerPassword == "":
            print("Error:Password cannot be blank.")
            break

        if individual == "Patient":
            registerAge = input("Enter Patient Age:")
            if registerAge == "":
                print("Error:Age cannot be blank.")
                break
            elif registerContact.isdigit() == False:
                print("Error:Age must be number.")
                break

        registerContact = input(f"Enter {individual} Contact Number:")
        if registerContact == "":
            print("Error:Contact Number Cannot be blank.")
            break
        elif registerContact.isdigit() == False:
            print("Error:Contact Number must be number.")
            break

        if individual == "Patient":
            registerAddress = input("Enter Patient Address:")
            if registerAddress == "":
                print("Error:Address Cannot be blank.")
                break
        
        i = 0
        allID = []
        for info in readfile:
            allID.append(int(info[0]))
        while i < 10000:
            if i in allID:
                i += 1
            else:
                Entered = True
                if individual == "Patient":
                    readfile.append([str(i), registerName, registerPassword, registerAge, registerContact, registerAddress])
                else:
                    readfile.append([str(i), registerName, registerPassword, registerContact])
                fileManager.writeFile(file, readfile)
                print(f"{individual} ID: {i} added successfully!")
                break

def UpdateDetailMenu():
    while True:
        user = input("============================\nUpdate Menu\n1.Patient\n2.Doctor\n3.Nurse\n4.Abort\nYour Choice:")
        match user:
            case "1":
                print("="*30, "Patient", "="*30)
                fileManager.viewAllPatient()
                Updateindividual("Patient")
            case "2":
                print("="*30, "Doctor", "="*30)
                fileManager.viewAllDoctor()
                Updateindividual("Doctor")
            case "3":
                print("="*30, "Nurse", "="*30)
                fileManager.viewAllNurse()
                Updateindividual("Nurse")
            case "4":
                print("Bringing you back...")
                break
            case _:
                print("Error: Invalid Input.")
                break

def Updateindividual(individual):
    match individual:
        case "Patient":
            file = "patient.txt"
        case "Doctor":
            file = "doctor.txt"
        case "Nurse":
            file = "nurse.txt"
    readfile = fileManager.readFile(file)
    userid = input("============================\nEnter your ID: ")
    if userid == "" or userid.isdigit() == False:
        print("Invalid input, ID must be digits and cannot be null.")
    else: #info is reading the file one individual by individual at a time
        for info in readfile:
            if info[0] == userid:
                print(f"{individual}: {info[1]} found.")
                while True:
                    if individual == "Patient":
                        user = input("============================\nWhat would you like to Update?\n1.Name\n2.Password\n3.Age\n4.Contact Number\n5.Address\n0.Abort\nYour Choice:")
                    else:
                        user = input("============================\nWhat would you like to Update?\n1.Name\n2.Password\n3.Contact Number\n0.Abort\nYour Choice:")
                    if user == "" or user.isdigit() == False:
                        print("Invalid input, input must be digits and cannot be null.")

                    user = int(user)
                    if user == 1:
                        update = input(f"Enter {individual} Name:")

                    elif user ==2:
                        update = input(f"Enter {individual} Password:")

                    elif user ==3:
                        if individual == "Patient":
                            update = input(f"Enter {individual} Age:")
                        else:
                            update = input(f"Enter {individual} Contact Number:")

                    elif user ==4:
                        if individual == "Patient":
                            update = input(f"Enter {individual} Contact Number:")
                        else:
                            print("Invalid Response, Please try again.")
                            break

                    elif user ==5:
                        if individual == "Patient":
                            update = input(f"Enter {individual} Address:")
                        else:
                            print("Invalid Response, Please try again.")
                            break

                    elif user ==0:
                        print("Bringing you back...")
                        break
                    else:
                        print("Invalid Response, Please try again.")
                        break

                    #checking update
                    if update == "":
                        print("Error:Input cannot be blank.")
                    elif info[user] == update:
                        print("Error, new value must be different from old value.")
                    elif user ==3 and update.isdigit() == False:
                        if individual == "Patient":
                            print("Age must be digits.")
                        else:
                            print("Contact Number must be digits.")
                    elif user ==4 and update.isdigit() == False:
                        print("Contact Number must be digits.")

                    else:
                        print("="*30)
                        confirm = input(f"System will be overwrite {info[user]} with {update}.\n1.Confirm\n2.Abort\nAre you sure?:")
                        match confirm:
                            case "1":
                                readfile.remove([info[0], info[1], info[2], info[3], info[4], info[5]])
                                info[user] = update
                                readfile.append([info[0], info[1], info[2], info[3], info[4], info[5]])
                                fileManager.writeFile(file, readfile)
                                print("Updated")
                                break
                            case "2":
                                print("Bringing you back...")
                                break

                            case _:
                                print("Error: Invalid Input.")
                                break

        if userid != info[0]: 
            print(f"Error: {individual} ID {userid} does not exist.")

###Appointment
def MakeAppoint():
    print("="*30, "patient", "="*30)
    fileManager.viewAllPatient()
    print("="*30, "doctor", "="*30)
    fileManager.viewAllDoctor()
    print("=" * 68)
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

    #patientName, doctorName = patientName, doctorName
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

    user = input("="*70 + "\nWhat would you like to do?\n1.Schedule Appointment\n2.View Appointment\n3.Cancel Appointment\n4.Abort\nYour Choice:")
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
        case _:
            print("Error: Invalid Input")

def scheduleAppointment(patientId, doctorId, patientName, doctorName):
    date = input("============================\nEnter the date in DD/MM/YY(ex:06/09/25),seperated by '/'.:")
    startTime = input("Enter the starting time of the appointment in [24 hour format](ex:0945)")
    endTime = input("Enter the end time of the appointment in [24 hour format](ex:2300)")
    if not fileManager.checkDate(date):
        print("Date does not match DD/MM/YY format or input is invalid")
        Appointment_fuction(patientId, doctorId, patientName, doctorName)
        return
    if fileManager.checkTime(startTime) and fileManager.checkTime(endTime):
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
            if doctorId == appointBlockInfo[1] and date == appointBlockInfo[2]:
                print(f"Error: Doctor {doctorName} has this date [{date}] blocked for appointment.")
                Appointment_fuction(patientId, doctorId, patientName, doctorName)
                return

        #already check all, and no repeating date are found
        print(f"Appointment made for [{patientName}] at [{date}] successfully!")
        
        Appointment.append([patientId, doctorId, date, startTime, endTime])
        fileManager.writeFile("Appointment.txt", Appointment)
    else:
        print("Start/End time does not match XXXX format or input is invalid")
    Appointment_fuction(patientId, doctorId, patientName, doctorName)

def viewAppointment(patientId, doctorId, patientName, doctorName):
    Appointments = fileManager.readFile("Appointment.txt")
    print("\n" + "=" * 24 + " Appointment " + "=" * 24)
    print("Patient name: ", patientName)
    print("Doctor name: ", doctorName)
    totalAppointment = 0
    if len(Appointments) > 0:
        for Appointment in Appointments:
            if Appointment[0] == patientId and Appointment[1] == doctorId:
                totalAppointment += 1
                print("Number:", str(totalAppointment).ljust(3), "Date:", Appointment[2].ljust(9), "Start Time:", Appointment[3].ljust(5), "End Time:", Appointment[4])
        print(f"Total appointment: {totalAppointment}")
    else:
        print(patientName, "and", doctorName, "don't have appointment yet.")
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
    fileManager.writeFile("Appointment.txt", Appointments)
    Appointment_fuction(patientId, doctorId, patientName, doctorName)

###payment###
def RepPay():
    print("="*30, "patient", "="*30)
    fileManager.viewAllPatient()
    userid = input("="*70 + "\nEnter Patient ID: ")
    if userid == "" or userid.isdigit() == False:
        print("Invalid input, ID must be digits and cannot be null.")
    else:
        paymentfuction(userid)

def paymentfuction(userid):
    patients = fileManager.readFile("patient.txt")
    info = []
    Found = False
    for patient in patients:
        if patient[0] == userid:
            Found = True
            info = patient
            break
    while Found:
        print(f"============================\nPatient [{patient[1]}] Payment List.")
        user = input(f"----------------------------\nWhat would you like to do?\n1.Add outstanding amount.\n2.View patient's payment history.\n3.Process payment.\n4.Back to receptionist menu.\nYour Choice:")
        if user == "" or user.isdigit() == False:
            print("Invalid input, ID must be digits and cannot be null.")
            break
        user = int(user)
        match user:
            case 1: #add outstanding payment
                price = input("How much does the patient has to pay?")
                if price == "":
                    print("Error:Price cannot be blank.")
                    
                elif price.isdigit() == False:
                    print("Error:Price must be number.")
                    
                paymentList = fileManager.readFile("patient_payments/"+ str(userid) +".txt")
                id = 0
                for payment in paymentList:
                        id += 1
                        
                paymentList.append([str(id),price,"No"])
                fileManager.writeFile("patient_payments/"+ str(userid) +".txt", paymentList)
                print("Outstanding Payment Added Successfully!")
                
            case 2:
                viewpayment(info)

            case 3:
                viewpayment(info)
                if totalamount != 0:
                    pay = input(f"Which payment id does {info[1]} wishes to pay?")
                    if pay == "" or pay.isdigit() == False:
                        print("Invalid input, ID must be digits and cannot be null.")
                        break
                    paymentList = fileManager.readFile("patient_payments/"+ str(userid) +".txt")
                    for payment in paymentList:
                        if pay == payment[0]:
                            if payment[2] == "Yes":
                                print("Error:Payment is already paid before!")
                                break
                            confirm = input(f"Payment ID {payment[0]} for {info[1]} is {payment[1]}.\n1.Yes\n2.No\nMark payment as paid?:")
                            match confirm:
                                case "1":
                                    if payment[2] == "No":
                                        paymentList.remove([payment[0], payment[1], payment[2]])
                                        payment[2] = "Yes"
                                        paymentList.append([payment[0], payment[1], payment[2], ])
                                        fileManager.writeFile("patient_payments/"+ str(userid) +".txt", paymentList)
                                        print("Payment made successfully!")
                                case "2":
                                    print("Bringing you back...")
                                case _:
                                    print("Error: Invalid input, only 1 or 2 is valid.")
                            break
                    if pay != payment[0]:
                        print("Error: PaymentID does not exist.")
                else:
                    print("There's no payment to be made.")
            case 4:
                print("Bringing you back to main menu.")
                break
    if not Found:
        print(f"Error: Patient ID: {userid} doesn't exist.")

def viewpayment(info):
    global totalamount
    paymentList = fileManager.readFile("patient_payments/"+ str(info[0]) +".txt")

    print("\n" + "=" * 24 + " Payment " + "=" * 24)
    print(f"Patient name: {info[1]}\n{"-"*57}")
    print("PaymentID\tAmount(RM)\tSettled Payment")
    for payment in paymentList:
        print(f"{payment[0]}\t\t{payment[1]}\t\t{payment[2]}")

    totalamount = 0
    for payment in paymentList:
        if payment[2] == "No":
            totalamount += int(payment[1])
    if totalamount == 0:
        print(f"{info[1]} has no outstanding payment.")
    else:
        print(f"Total outstanding amount: RM{totalamount}")
    print("=" * 57 + "\n")