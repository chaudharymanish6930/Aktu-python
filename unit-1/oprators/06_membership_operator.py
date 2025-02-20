# 'in' in the membership
li=[1,2,3,4,"manish"]
a=3
if a in li:
    print("present")
else:
    print("not present")

b="manish"
if b in li:
    print("present")
else:
    print("not present")

# 'in not' in membership
# li=[1,2,3,4,"manish"]
a=7
if a not in li:
    print("not present")
else:
    print("present")

b="man"
if b not in li:
    print("not present")
else:
    print("present")