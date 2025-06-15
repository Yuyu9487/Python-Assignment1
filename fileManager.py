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

def writeFile(path: str, data):
    try:
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
    filelocation = "patient.txt"
    sorting(file,filelocation)
    if len(file) > 0:
        file = readFile("patient.txt")
        for patient in file:
            print(f"ID:", patient[0].ljust(3), "Name:", patient[1].ljust(20), "Age:", patient[3].ljust(3), "Contact Number:", patient[4].ljust(12), "Address:", patient[5])
        print(f"Total patients: {len(file)}")
    else:
        print("\nError: Patient file is empty!\n")

def viewAllDoctor():
    file = readFile("doctor.txt")
    filelocation = "doctor.txt"
    sorting(file,filelocation)
    if len(file) > 0:
        file = readFile("doctor.txt")
        for doctor in file:
            print(f"ID:", doctor[0].ljust(3), "Name:", doctor[1].ljust(20), "Contact Number:", doctor[3].ljust(12))
        print(f"Total doctors: {len(file)}")
    else:
        print("\nError: Doctor file is empty!\n")

def viewAllNurse():
    file = readFile("nurse.txt")
    filelocation = "nurse.txt"
    sorting(file,filelocation)
    if len(file) > 0:
        file = readFile("nurse.txt")
        for nurse in file:
            print(f"ID:", nurse[0].ljust(3), "Name:", nurse[1].ljust(20), "Contact Number:", nurse[3].ljust(12))
        print(f"Total nurses: {len(file)}")
    else:
        print("\nError: Nurse file is empty!\n")

def viewpayment(info):
    global totalamount
    payment = readFile("patient_payments/"+ str(info[0]) +".txt")
    sorting(payment,"patient_payments/"+ str(info[0]) +".txt")
    payment = readFile("patient_payments/"+ str(info[0]) +".txt")

    print("\n" + "=" * 24 + " Payment " + "=" * 24)
    print(f"Patient name: {info[1]}\n{"-"*57}")
    print("PaymentID\tAmount(RM)\tSettled Payment")
    for payid in payment:
        print(payid[0],payid[1],payid[2])

    totalamount = 0
    for payid in payment:
        if payid[2] == "No":
            totalamount += int(payid[1])
    if totalamount == 0:
        print(f"{info[1]} has no outstanding payment.")
    
    else:
        print(f"Total outstanding appointment: RM{totalamount}")
    print("=" * 57 + "\n")

def sort_id(id):
    return int(id[0])

def sorting(file,filelocation):
    sorted = []
    for id in file:    
        sorted.append(id)
    sorted.sort(key=sort_id)

    writeFile(filelocation,sorted)
    #turns id which is (id[0]) into integer, then it will sort it according to integer