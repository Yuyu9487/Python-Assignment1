import main
import fileManager
import re
#Doctor Funtion
MEDICAL_HISTORY_FILE="patient_observation.txt"
APPOINTMENT_FILE="patient.txt"

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
                    Blocklist()
                    break
                case "5":
                    main.main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")
def Medlogs():
    pid = input("Enter Patient ID: ").strip()
    found = False
    with open(MEDICAL_HISTORY_FILE, "r") as f:
        for line in f:
            if line.startswith(pid):
                print(line.strip())
                found = True
    if not found:
        print("No records found.")

def UpdatePatRec():
    # Read from medical history file
    with open("patient_observation.txt", "r") as file:
        lines = file.readlines()

    # For demonstration: update first line (normally you'd search by ID or name)
    if lines:
        lines[0] = "Updated patient info\n"

    # Write back to the same file
    with open("patient_observation.txt", "w") as file:
        file.writelines(lines)
    
def viewappoint():
    return
def Blocklist():
    user = input("============================\n1.Block Schedule\n2.Unblock Schedule\n3.Abort\nYour choice:")
    if user == "" or user.isdigit() == False:
        print("Invalid input, ID must be digits and cannot be null.")
    else:
        user = int(user)
        match user:
            case 1:
                date = input("Enter the date in DD/MM/YY(ex:06/09/25),seperated by '/'.:")
                pattern = ("^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})$")
                try: 
                    if re.match(pattern,date):
                        Appointment = fileManager.readFile("AppointmentBlockList.txt")

                        for info in Appointment:
                            if info[0] == date:
                                print(f"Error: Date [{date}] already exist")
                                Blocklist()
                                break

                        #already check all, and no repeating date are found
                        print(f"{date} blocked successfully!")
                        Appointment.append([date])
                        fileManager.writeFile("AppointmentBlockList.txt", 1, Appointment)
                        Blocklist()

                    else:
                        raise ValueError("Date does not match DD/MM/YY format or input is invalid")
                except ValueError as Error:
                    print(Error)
            case 2:
                date = input("Enter the date in DD/MM/YY(ex:06/09/25),seperated by '/'.:")
                pattern = ("^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})$")
                try: 
                    if re.match(pattern,date):
                        Appointment = fileManager.readFile("AppointmentBlockList.txt")
                        for info in Appointment:
                            if info[0] == date:
                                print(f"Date: [{date}] unblocked successfully.")
                                Appointment.remove([info[0]])
                                fileManager.writeFile("AppointmentBlockList.txt", 1, Appointment)
                                Blocklist()
                                break
                        #date not exist
                        print(f"Error: Date [{date}] does not exist")
                        Blocklist()

                    else:
                        raise ValueError("Date does not match DD/MM/YY format or input is invalid")
                except ValueError as Error:
                    print(Error)
            case 3:
                print("Bring you back to receptionist menu...")
                Doctor()
            case _:
                print("Error, Invalid Input.")
                Doctor()
            







                    



                

