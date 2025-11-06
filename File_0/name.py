name = input("Enter your name: ")

file = open("employees.txt", "a")
file.write(f"{name}\n")
file.close()