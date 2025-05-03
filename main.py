import doctor
import nurse
import patient
import receptionist

def main():
    print("\n============================\nWelcome to Best Clinic!\n============================")
    print("1.Receptionist\n2.Doctor\n3.Nurse\n4.Patient\n5.Leave")
    while True:
        user = input("Enter Your Role:")
        match user:
            case "1":
                receptionist.Receptionist()
                break
            case "2":
                doctor.Doctor()
                break
            case "3":
                nurse.Nurse()
                break
            case "4":
                patient.Patient()
                break
            case "5":
                print("See You again!")
                break
            case _:
                print("Role not found, Please try again.")

main()