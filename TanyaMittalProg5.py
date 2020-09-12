name = str(input())
dob = str(input())
phoneno = str(input())

password = ''
password = phoneno[0:3] + name[len(name)-3:] + dob[len(dob)-4:]
print(password)
