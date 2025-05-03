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
def UpdatePatRec():
    return
def viewappoint():
    return
def Timetable():
    return