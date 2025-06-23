# readFile function is used to read the file contents and return a double layer list for data.
def readFile(path : str):
    # first try to read the content in file and format the content.
    try:
        with open(path, "r") as file:
            content = file.read()
        # if file is empty then return a empty list
        if len(content) < 1:
            return []
        # split content with new line character to get a list that elements are each line in content.
        content = content.split("\n")
        datalist = []
        for line in content:
            # split line with "/#" to get a list that elements are each information in line.
            datas = line.split("/#")
            if len(datas) > 0:
                datalist.append(datas)
        return datalist
    # if the file doesn't exist then try to create the file, and return a empty list to avoid the variable error.
    except:
        print(path, "have not found!")
        print("Creating", path)
        try:
            f = open(path, "x")
            f.close()
        except:
            print("Creating", path, "fail!")
        return []

# writeFile function is used to write the data in file with a double layer data list, similar to the list that readFile function return.
def writeFile(path: str, data: list):
    try:
        # sort data list with first element.
        data.sort(key = lambda group : int(group[0]))
        with open(path, "w") as file:
            lines = []
            # loop each information group in data list, and join "/#" between the elements of group to combine the elements to a string line.
            for group in data:
                line = "/#".join(str(var) for var in group)
                lines.append(line)
            # after combining, join new line character between each line, and write it into file.
            file.write("\n".join(lines))
    except:
        print("\n", path, "cannot be found!\n")

# display all patient and the total patient amount.
def viewAllPatient():
    file = readFile("patient.txt")
    if len(file) > 0:
        for patient in file:
            print(f"ID:", patient[0].ljust(3), "Name:", patient[1].ljust(20), "Age:", patient[3].ljust(3), "Contact Number:", patient[4].ljust(12), "Address:", patient[5])
        print(f"Total patients: {len(file)}")
    else:
        print("\nError: Patient file is empty!\n")

# display all doctor and the total doctor amount.
def viewAllDoctor():
    file = readFile("doctor.txt")
    if len(file) > 0:
        for doctor in file:
            print(f"ID:", doctor[0].ljust(3), "Name:", doctor[1].ljust(20), "Contact Number:", doctor[3].ljust(12))
        print(f"Total doctors: {len(file)}")
    else:
        print("\nError: Doctor file is empty!\n")

# display all nurse and the total nurse amount.
def viewAllNurse():
    file = readFile("nurse.txt")
    if len(file) > 0:
        for nurse in file:
            print(f"ID:", nurse[0].ljust(3), "Name:", nurse[1].ljust(20), "Contact Number:", nurse[3].ljust(12))
        print(f"Total nurses: {len(file)}")
    else:
        print("\nError: Nurse file is empty!\n")

# check date with many validation, if the date is correct then return true, otherwise return false.
def checkDate(date:str):
    if len(date) == 8 and (date[0:2] + date[3:5] + date[6:8]).isdigit() and date[2] == "/" and date[5] == "/" and 13 > int(date[3:5]) > 0 and int(date[0:2]) > 0:
        if int(date[6:8]) % 4 == 0 and int(date[3:5]) == 2 and int(date[0:2]) < 30:
            return True
        if int(date[3:5]) == 2 and int(date[0:2]) < 29:
            return True
        if int(date[3:5]) in (1, 3, 5, 7, 8, 10, 12) and int(date[0:2]) < 32:
            return True
        if int(date[3:5]) in (4, 6, 9, 11) and int(date[0:2]) < 31:
            return True
    return False

# check time with simple validation, if the time is correct then return true, otherwise return false.
def checkTime(time:str):
    if len(time) == 4 and time.isdigit() and 24 > int(time[:2]) > -1 and 60 > int(time[2:]) > -1:
        return True
    return False