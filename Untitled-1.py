def main():
    start = input(f"Welcome\n1.add\n2.read\nYour choice:")
    if start == "1":
        add()
    elif start == "2":
        read()

def read():
    with open(r"file.txt", "r") as file:
        content = file.read()
        print(content)
    main()

def add():
    user = input("What you want to write?:")
    #when use "w+", the file will be clean.
    with open(r"file.txt", "w+") as file:
        file.write(user)
        file.seek(0)
        content = file.read()
        print(content)
    main()

main()