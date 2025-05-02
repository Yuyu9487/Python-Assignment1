def readFile(path : str):
    with open(path, "r") as file:
        content = file.read()
    return content
    file.close()

def writeFile(path : str, user):
    with open(path, "w") as file:
        file.write(user)
    file.close()

# read file example
def example():
    fileData = readFile(file.txt)
    fileDatas = fileData.split("#")
    i = 3
    for x in fileDatas:
        match i % 3:
            case 0:
                # print name
                pass
            case 1:
                # print age
                pass
            case 2:
                # print address
                pass
        i += 1
