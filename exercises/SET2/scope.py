def main():
    name = input("What is your name?").strip()
    if name == "":
        hello()
    else:
        hello(name)

def hello(to="Students"):
    print("Hello,", to)

main()