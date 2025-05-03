import main
#Nurse Functions
def Nurse():
    print("\n============================\nNurse Menu\n============================")
    print("1.View Doctor's Appointment\n2.Record Patient's Observation\n3.View Prescriptions\n4.Administer Medicine To Patients\n5.Back To Menu")
    while True:
        user = input("Your Choice:")
        match user:
                case "1":
                    viewdocappoint()
                    break
                case "2":
                    Recpatient()
                    break
                case "3":
                    viewprescript()
                    break
                case "4":
                    Givemeds()
                    break
                case "5":
                    main.main()
                    break
                case _:
                    print("Error. Please Enter A Valid Input.")

def viewdocappoint():
    return
def Recpatient():
    return
def viewprescript():
    return
def Givemeds():
    return