def validate_password(password):
    # 1. Data type check
    try:
        if not isinstance(password, str):
            raise TypeError
    except TypeError:
        print("Error: Password must be a string.")
        return False

    # 2. Length check
    if len(password) < 10:
        print("Error: Password must be at least 10 characters long.")
        return False

    # 3. Strength checks
    upper_case, lower_case,digit = False, False, False
    for char in password:
        if char.isupper():
            upper_case = True
        elif char.islower():
            lower_case = True
        elif char.isdigit():
            digit = True

    if upper_case and lower_case and digit:
        return True
    else:
        print("Error: Password must include uppercase, lowercase, and a digit.")
        return False


# Test calls
print(validate_password("abcD123"))              # Too short, False
print(validate_password("SuperPasswordWithoutNumber"))  # No digit, False
print(validate_password("Helloworld123"))        # All criteria met, True
print(validate_password(1234567890123))          # Incorrect data type, False
