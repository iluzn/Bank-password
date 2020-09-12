name=input()
dob=input()
contact=input()
passw= contact[:3] + name[-3:] + dob[-4:]
print(passw)
