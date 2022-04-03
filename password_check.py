password = input("Enter password:")
while len(password) < 6:
    print("Length of the password should not be less than 6")
    password = input("Enter password:")
else:
    print("*"*len(password))