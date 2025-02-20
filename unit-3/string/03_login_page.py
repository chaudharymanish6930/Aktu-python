passwords=input("enter passowrd").split()
acceptable=[]

for password in passwords:
    upper=False
    lower=False
    length=False
    number=False
    special=False
    if 6<=len(password)<=12:
        lenght=True
    for j in password:
        if j.isupper():
            upper=True
        elif j.islower():
            lower=True
        elif j.isdigit():
            number=True
        elif j in('@',"$",'#'):
            special=True
        else: pass
    if all(upper,lower,lenght,number,special):
        acceptable.append(password)

    print("acceptable passords:",''.join(acceptable))
