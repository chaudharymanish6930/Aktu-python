t1=('f','i','a','b','b','e','r','e','g','e','q','s','t','e','d')

l1=list(t1)
l1.append("@")
print(l1)


s1="".join(t1)
print(s1)
s2=''.join(t1)
print(s2)

element=t1[3:5]
print(element)

y=0
for i in t1:
    if i=="e":
        y=y+1
print(y)

for i in t1:
    if i=="r":
        print("yes this exist")
for i in t1:
    if i=="b":
        print("yes this exist")
        break
for i in t1:
    if i=="e":
        print("yes, buddy it is exist")
 

l1=[item for item in l1 if item not in['b','b','e','r']]
t2=tuple(l1)
print(t2)

t3=t1[:3]+t1[7:]
print(t3)