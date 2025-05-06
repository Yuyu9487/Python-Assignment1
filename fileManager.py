#readFile = [(id, name), (id, name), (id, name), ..]
# read = 3/#id/#name/#age/#id/#name/#age

def readFile(path : str):
    try:
        with open(path, "r") as file:
            content = file.read()
        data = content.split("/#")
        number = int(data[0])
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
        print("\n", path, "can not found!\n")
        return []

def writeFile(path : str, number : int, data):
    write = ""
    write += str(number)
    for group in data:
        for var in group:
            write += "/#" + var
    try:
        with open(path, "w") as file:
            file.write(write)
    except:
        print("\n", path, "can not found!\n")