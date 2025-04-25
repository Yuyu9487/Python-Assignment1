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
    with open(r"file.txt", "a") as file:
        file.write(f"\n{user}")
    read()

main()