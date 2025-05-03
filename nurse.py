import main
import fileManager
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
    nurseinfo = fileManager.readFile("nurseinfo.txt")
    #data = [(id, name, contact, age), (id, name, contact, age), (id, name, contact, age), ..
    user = input("Enter Your ID: ")
    for i in range(len(nurseinfo)):
        if nurseinfo[i][0] == user:
            print("Your ID:", nurseinfo[i][0])
            print("Your Name:", nurseinfo[i][1])
            print("Your Contact:", nurseinfo[i][2])
            print("Your Age:", nurseinfo[i][3])
            break
    else:
        print("ID not found.")
        return
    return
def Recpatient():
    return
def viewprescript():
    return
def Givemeds():
    return


#def nurseupdateinfo():
    nurseinfo = fileManager.readfile("nureseinfo.txt")
    #data = [(id, name, contact, age), (id, name, contact, age), (id, name, contact, age), ..
    user = input("Enter Your ID:")
    for i in range(len(nurseinfo)):
        if nurseinfo[i][0] == user:
            print("Your ID:", nurseinfo[i][0])
            print("Your Name:", nurseinfo[i][1])
            print("Your Contact:", nurseinfo[i][2])
            print("Your Age:", nurseinfo[i][3])
            break
    else:
        print("ID not found.")
        return