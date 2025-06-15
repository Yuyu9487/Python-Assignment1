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

def writeFile(path: str, data: list):
    try:
        # sort data with first element
        data.sort(key = lambda group : group[0])
        with open(path, "w") as file:
            lines = []
            for group in data:
                line = "/#".join(str(var) for var in group)
                lines.append(line)
            file.write("\n".join(lines))
    except:
        print("\n", path, "cannot be found!\n")

def viewAllPatient():
    file = readFile("patient.txt")
    if len(file) > 0:
        for patient in file:
            print(f"ID:", patient[0].ljust(3), "Name:", patient[1].ljust(20), "Age:", patient[3].ljust(3), "Contact Number:", patient[4].ljust(12), "Address:", patient[5])
        print(f"Total patients: {len(file)}")
    else:
        print("\nError: Patient file is empty!\n")

def viewAllDoctor():
    file = readFile("doctor.txt")
    if len(file) > 0:
        for doctor in file:
            print(f"ID:", doctor[0].ljust(3), "Name:", doctor[1].ljust(20), "Contact Number:", doctor[3].ljust(12))
        print(f"Total doctors: {len(file)}")
    else:
        print("\nError: Doctor file is empty!\n")

def viewAllNurse():
    file = readFile("nurse.txt")
    if len(file) > 0:
        for nurse in file:
            print(f"ID:", nurse[0].ljust(3), "Name:", nurse[1].ljust(20), "Contact Number:", nurse[3].ljust(12))
        print(f"Total nurses: {len(file)}")
    else:
        print("\nError: Nurse file is empty!\n")

def viewpayment(info):
    payments = readFile("patient_payments/"+ str(info[0]) +".txt")
    totalamount = 0

    print("\n" + "=" * 24 + " Payment " + "=" * 24)
    print(f"Patient name: {info[1]}\n{"-"*57}")
    print("PaymentID\tAmount(RM)\tSettled Payment")
    for payment in payments:
        print(payment[0],payment[1],payment[2])
        if payment[2] == "No":
            totalamount += int(payment[1])

    if totalamount == 0:
        print(f"{info[1]} has no outstanding payment.")
    else:
        print(f"Total outstanding appointment: RM{totalamount}")
    print("=" * 57 + "\n")