def readFile(path : str):
    try:
        with open(path, "r") as file:
            content = file.read()
        rawDatas = content.split("\n")
        datalist = []
        group = []
        for rawData in rawDatas:
            datas = rawData.split("/#")
            for data in datas:
                if data != '':
                    group.append(data)
            if len(group) > 0:
                datalist.append(group)
                group = []
        return datalist
    except:
        print(path, "have not found!")
        print("Creating", path, "\n")
        f = open(path, "x")
        f.close()
        return []

def writeFile(path : str, data):
    write = ""
    for group in data:
        for var in group:
            write += str(var) + "/#"
        write = write[:-2]
        write += "\n"
    write = write[:-2]
    try:
        with open(path, "w") as file:
            file.write(write)
    except:
        print("\n", path, "can not found!\n")

def viewAllPatient():
    patients = readFile("patient.txt")
    if len(patients) > 0:
        for patient in patients:
            print(f"ID:", patient[0].ljust(3), "Name:", patient[1].ljust(20), "Age:", patient[3].ljust(3), "Contact Number:", patient[4].ljust(12), "Address:", patient[5])
        print(f"Total patients: {len(patients)}")
    else:
        print("\nError: Patient file is empty!\n")

def viewAllDoctor():
    doctors = readFile("doctor.txt")
    if len(doctors) > 0:
        for doctor in doctors:
            print(f"ID:", doctor[0].ljust(3), "Name:", doctor[1].ljust(20), "Contact Number:", doctor[3].ljust(12))
        print(f"Total doctors: {len(doctors)}")
    else:
        print("\nError: Doctor file is empty!\n")

def viewAllNurse():
    nurses = readFile("nurse.txt")
    if len(nurses) > 0:
        for nurse in nurses:
            print(f"ID:", nurse[0].ljust(3), "Name:", nurse[1].ljust(20), "Contact Number:", nurse[3].ljust(12))
        print(f"Total nurses: {len(nurses)}")
    else:
        print("\nError: Nurse file is empty!\n")