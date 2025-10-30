try:
    user_number = int(input("Enter a number: "))
    
except ValueError:
    pass
else:
    print(f"You entered the number: {user_number}")
