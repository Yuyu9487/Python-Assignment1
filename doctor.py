import random
import main
#Doctor Funtion
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
    return
medical_logs = {
    "P001": [
        {"date": "2025-01-25", "Name":"Ali", "diagnosis": "Flu", "treatment": "Rest + Paracetamol", "Allergy":"Seafood"},
        {"date": "2025-03-15", "Name" :"Betty", "diagnosis": "Hypertension", "treatment": "Prescribed Amlodipine", "Allergy":"Seafood"}
    ],
    "P002": [
        {"date": "2025-01-20", "Name":"Chris", "diagnosis": "Back Pain", "treatment": "Physical therapy recommended", "Allergy":"Protein"}
    ],
    "P003": [
        {"date": "2024-11-25", "Name":"David", "diagnosis":"Asthma","treatment":"Inhaled Corticosteroids", "Allergy":"latex"}
    ]
}

def Medlogs():
    patient_id = input("Enter Patient ID: ").strip().upper()
    logs = medical_logs.get(patient_id)

    if not logs:
        print(f"No records found for Patient ID: {patient_id}")
        return

    print(f"\n--- Medical Logs for {patient_id} ---")
    for entry in logs:
        print(f"Date: {entry['date']}")
        print(f"Name: {entry['Name']}")
        print(f"Diagnosis: {entry['diagnosis']}")
        print(f"Treatment: {entry['treatment']}")
        print(f"Allergy:{entry['Allergy']}")
        print("-" * 30)

def UpdatePatRec():
    # Read from medical history file
    with open("medical_history.txt", "r") as file:
        lines = file.readlines()

    # For demonstration: update first line (normally you'd search by ID or name)
    if lines:
        lines[0] = "Updated patient info\n"

    # Write back to the same file
    with open("medical_history.py", "w") as file:
        file.writelines(lines)
    print("Patient record updated.")
def viewappoint():
    return
def Timetable():
    return