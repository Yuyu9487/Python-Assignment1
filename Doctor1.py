import main

def Doctor():
    print ("Doctor Page")
    print ("1. View medical history and treatment logs of patients.")
    print ("2. Update patient records with diagnosis, prescriptions, and treatment plans.")
    print ("3. View own appointment list ")
    print ("4. Block/unblock availability for certain days.")

user=input("Please select your option!")

if user==1:
    patienthistory="Please insert the patient's name."
    print ("The patient that you chose is", patienthistory)
    import medical_history
    