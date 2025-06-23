def readFile(path : str):   # path(parameter name) is a name when whatever the result of this function got is hold the input value on this 'path' name
    try:                    # str = string, str here expect string
        with open(path, "r") as file:
            content = file.read()
        if len(content) < 1:
            return []
        content = content.split("\n")
        datalist = []            #datalist = [content]
        for line in content:
            datas = line.split("/#")
            if len(datas) > 0:
                datalist.append(datas) #datalist []
        return datalist          #datalist is the big list [] that will store small list of each line in "patient observation.txt" that store in 'datas'
                                 #seperate ("/#") with the datas variable and it will become 
    except:
        print(path, "have not found!")
        print("Creating", path)
        try:
            f = open(path, "x")
            f.close()
        except:
            print("Creating", path, "fail!")
        return []

def writeFile(path: str, data: list):
    try:
        # sort data with first element
        data.sort(key = lambda group : int(group[0]))
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
        print(f"Total doctors: {len(file)}")  # ask haoyu how it works, so when retrieve information it uses indedx, and when print display 3 with len function?
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

def checkDate(date:str):
    if len(date) == 8 and (date[0:2] + date[3:5] + date[6:8]).isdigit() and date[2] == "/" and date[5] == "/" and 13 > int(date[3:5]) > 0 and int(date[0:2]) > 0:
        if int(date[6:8]) % 4 == 0 and int(date[3:5]) == 2 and int(date[0:2]) < 30:
            return True
        if int(date[3:5]) == 2 and int(date[0:2]) < 29:
            return True
        if int(date[3:5]) in (3,1,  5, 7, 8, 10, 12) and int(date[0:2]) < 32:
            return True
        if int(date[3:5]) in (4, 6, 9, 11) and int(date[0:2]) < 31:
            return True
    return False

def checkTime(time:str):
    if len(time) == 4 and time.isdigit() and 24 > int(time[:2]) > -1 and 60 > int(time[2:]) > -1:
        return True
    return False