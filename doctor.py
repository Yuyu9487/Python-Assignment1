import main
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
                    Timetable()
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
def Timetable():
    return