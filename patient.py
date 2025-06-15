import fileManager
#Patient function
def Patient():
    ID = -1
    while True:
        if ID == -1:
            print("\n================== Patient Login Menu ==================")
            print("1.Login")
            print("2.Back To Menu")
            user = input("Your Choice:").strip()
            match user:
                case "1":
                    ID = Login()
                case "2":
                    break
                case _:
                    print("\nError. Please Enter A Valid Input.\n")
        else:
            print("\n================== Patient Menu ==================")
            print("1.View Personal Medical Records")
            print("2.View Appointment")
            print("3.Update Infomation")
            print("4.Access Billing Details And Payment History")
            print("5.Back To Menu")
            user = input("Your Choice:").strip()
            match user:
                case "1":
                    view_patient_medical_record(ID)
                case "2":
                    view_appointment(ID)
                case "3":
                    update_info(ID)
                case "4":
                    view_payment(ID)
                case "5":
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")

def Login():
    patientInfo = fileManager.readFile("patient.txt")
    userName = input("\nEnter your Name: ").strip()
    userPassword = input("Enter your Password: ").strip()
    if userName == "":
        print("\nError:Name connot be blank!\n")
        return -1
    elif userPassword == "":
        print("\nError:Password connot be blank!\n")
        return -1
    for info in patientInfo:
        if info[1] == userName and info[2] == userPassword:
            print("\nSuccessful login!\n")
            return int(info[0])
    print("\nError:Name or Password error!\n")
    return -1

def view_patient_medical_record(ID):
    my_medical_records = fileManager.readFile("patient_medical_records/" + str(ID) + ".txt")
    number = 0
    if len(my_medical_records) > 0:
        for medical_record in my_medical_records:
            number += 1
            print("\n" + "=" * 34 + " Medical Record " + str(number) + "=" * 34)
            print("Problem:".rjust(13), medical_record[1])
            print("Detail:".rjust(13), medical_record[2])
            print("Medical plan:".rjust(13), medical_record[3])
            print("Price:".rjust(13), medical_record[4])
            print("Date:".rjust(13), medical_record[5])
        print("=" * 89 + "\n")
    else:
        print("\nYou don't have any medical record!")

def view_appointment(ID):
    appointments = fileManager.readFile("Appointment.txt")
    doctors = fileManager.readFile("doctor.txt")
    print("\n" + "=" * 38 + " Appointment " + "=" * 38)
    for appointment in appointments:
        # find the appointment which is for this patient
        if int(appointment[1]) == ID:
            # get doctor name
            doctorName = "empty"
            for doctor in doctors:
                if doctor[0] == appointment[1]:
                    doctorName = doctor[1]
                    break
            
            # print appointment
            print("ID:", appointment[0].ljust(3), "Doctor:", doctorName.ljust(20), "Date:", appointment[2].ljust(10), "Start time:", appointment[3].ljust(6), "End time:", appointment[4].ljust(6))
    print("=" * 89 + "\n")

def update_info(ID):
    patientInfo = fileManager.readFile("patient.txt")
    for i in range(0, len(patientInfo)):
        # find patient Information
        if int(patientInfo[i][0]) == ID:
            # select the information witch user want to update
            user = int(input("\nWhat would you like to Update?\n1.Name\n2.Password\n3.Age\n4.Contact Number\n5.Address\n6.Abort\nYour Choice:").strip())
            match user:
                case 1:
                    update = input("\nEnter Patient Name:").strip()
                case 2:
                    update = input("\nEnter Patient Password:").strip()
                case 3:
                    update = input("\nEnter Patient Age:").strip()
                case 4:
                    update = input("\nEnter Patient Contact Number:").strip()
                case 5:
                    update = input("\nEnter Patient Address:").strip()
                case _:
                    print("Invalid service choice.")
                    break
            # check update is correct or not, then update user informationa
            if update == "":
                print("\nError:Input cannot be blank.")
            elif user == 3 and not update.isdigit():
                print("\nError:Age cannot be not digit.")
            elif user == 4 and not update.isdigit():
                print("\nError:Patient cannot be not digit.")
            else:
                confirm = input(f"\nSystem will be overwrite {patientInfo[i][user]} with {update}.\n1.Confirm\n2.Cancel\nAre you sure?:").strip()
                if confirm == "1":
                    patientInfo[i][user] = update
                    fileManager.writeFile("patient.txt", patientInfo)
                    print("\nUpdated Sussessful!")
                else:
                    print("Invalid service choice.")
            break

def view_payment(ID):
    my_payments = fileManager.readFile("patient_payments/" + str(ID) + ".txt")
    print("\n" + "=" * 34 + " Payment History " + "=" * 34)
    for payment in my_payments:
        print("ID:", payment[0], "Price:", payment[1], "Settled Payment:", payment[2])
    print("=" * 85 + "\n")