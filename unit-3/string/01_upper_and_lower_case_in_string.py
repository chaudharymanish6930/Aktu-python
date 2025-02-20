def count_case(string):
    upper_case=0
    lower_case=0
    for i in string:
        if i.isupper():
            upper_case+=1
        elif i.islower(): 
            lower_case+=1
    print("no of upper case:",upper_case)
    print("no of lower case:",lower_case)

user_input=input("enter a string:")
count_case(user_input)

# x="Manish Choudhary"
# for i in x:
#     if i.upper():
#         print(i)