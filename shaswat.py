name=input()
dob=input()
cont=input()
password=cont[:3]+name[len(name)-3:]+dob[len(dob-4):]
print(password)
