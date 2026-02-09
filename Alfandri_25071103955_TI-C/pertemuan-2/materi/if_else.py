#
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#Shorthand If

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")

#Logical Operator
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

#Nested If

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")

#Pass Statement

score = 85

if score > 90:
    pass # This is excellent
print("Score processed")
