name = str(input())
dob = str(input())
number = str(input())

password = ''
password = number[0:3] + name[len(name)-3:] + dob[len(dob)-4:]
print(password)
