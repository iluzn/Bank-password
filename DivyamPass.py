name=input();
dob=input();
phnos=input();
DOB=str(dob);
len0=len(name);
len1=len(DOB);
password=phnos[0:3]+name[len0-3:len0]+DOB[len1-4:len1];
print(password)
