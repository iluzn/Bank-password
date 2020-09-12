name = input("Enter the  name : ")
phon = input("Enter the phone number : ")
dob = input("Enter the date of birth : ")
password = phon[0:3] + name[-3:] + dob[-4:]
print("Password is " + password)
