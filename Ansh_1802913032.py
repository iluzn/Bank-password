name=input()
Dob=input()
Contact=input()

password=Contact[0:3]+name[-3:]+Dob[-4:]
print(password)
