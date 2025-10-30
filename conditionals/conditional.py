age = int(input("Enter your age: "))
if age > 18:
    print("You are an adult.")
# elif age > 0 and age < 18:
elif 0 < age < 18:
    print("You are a minor.")
elif age <=0:   
    print("Invalid age entered.")
# if age == 18:
else:
    print("You are exactly 18 years old.")
