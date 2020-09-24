#Example : 01
#Let take 2 integers:

a=input(int())
b=input(int())

#relation one:

if a>b:
    print("a is bigger")
elif a<b:
    print("b is bigger")
elif a==b:
    print("Two are equal")
else:
    print("Try again")

#relation two:

if a>b:
    print("a is bigger")
elif a<b:
    print("b is greater")
elif a==b:
    print("Two are equal")
else:
    print("Try again")

#relation three:

if a>b:
    print("a is greater")
elif b<a:
    print("a is large")
elif b==a:
    print("Same")
elif b!=a:
    print("Not Equal")
elif b>=a:
    print("b is equal or large")
elif a>=b:
    print("a is bigger or equal")
elif a%b==0:
    print("Reminder")
else:
    print("Something Else")

#relation four:
if b>=a:
    print("b is equal and large")
elif a>b:
    print("a is bigger")
elif a>=b:
    print("a is equal or big")
else:
    print("New")

-------------------------------------

#relation five:
    if a/b==17:
        print("Devide")
    else:
        print("Anything")
