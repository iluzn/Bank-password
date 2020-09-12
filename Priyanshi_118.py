Name=input()
Date=input()
Phonenum=int(input())
password=str(Phonenum)[0:3]+Name[-3:].lower()+Date[-4:]
print(password)
