# Ask user for the number of rows
def triangle ():
    rows = int(input("Enter the number of rows: "))

# Loop through each row
    for i in range(1, rows + 1):
    # Print stars for the current row
        print("*" * i)

triangle