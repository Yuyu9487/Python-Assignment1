import doctor
import nurse
import patient
import receptionist

def main():
    while True:
        print("\n============================\nWelcome to Best Clinic!\n============================")
        print("1.Receptionist\n2.Doctor\n3.Nurse\n4.Patient\n5.Leave")
        user = input("Enter Your Role:")
        match user:
            case "1":
                receptionist.Receptionist()
            case "2":
                doctor.Doctor()
            case "3":
                nurse.Nurse()
            case "4":
                patient.Patient()
            case "5":
                print("See You again!")
                break
            case _:
                print("Role not found, Please try again.")

main()