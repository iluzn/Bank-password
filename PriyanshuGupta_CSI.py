print("Enter your name")
name = input()
print("Enter your Date of Birth")
Dob = input()
print("Enter your Contact")
con = input()

res = ""

res += con[0:3]
res += name[-3:]
res += Dob[-4:]

print("Password will be :",res)
