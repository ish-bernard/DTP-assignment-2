# Convert age using isdigit()

age = input("Enter your age")

if age.isdigit():
    age = int(age)
    print("valid age:", age)
else:
    print("invalid input. please enter digits only.")
