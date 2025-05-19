#readFile = [(id, name), (id, name), (id, name), ..]
# read = 3/#id/#name/#age/#id/#name/#age

def readFile(path : str):
    try:
        with open(path, "r") as file:
            content = file.read()
        data = content.split("/#")
        try:
            number = int(data[0])
        except:
            number = 0
        datalist = []
        group = []
        groupNumber = 0
        while groupNumber < len(data) - 1:
            for i in range(0, number):
                group.append(data[i + groupNumber + 1])
            datalist.append(group)
            group = []
            groupNumber += number
        return datalist
    except:
        print(path, "have not found!")
        print("Creating", path, "\n")
        f = open(path, "x")
        f.close()
        return []

def writeFile(path : str, number : int, data):
    write = ""
    write += str(number)
    for group in data:
        for var in group:
            write += "/#" + str(var)
    try:
        with open(path, "w") as file:
            file.write(write)
    except:
        print("\n", path, "can not found!\n")

def viewAllPatient():
    patients = readFile("patient.txt")
    if len(patients) > 0:
        print("\n============================")
        for patient in patients:
            print(f"ID:", patient[0].ljust(3), "Name:", patient[1].ljust(20), "Contact Number:", patient[3].ljust(12), "Age:", patient[4].ljust(3), "Address:", patient[5])
        print(f"Total patient: {len(patients)}\n============================\n")
    else:
        print("\nError: Patient file is empty!\n")