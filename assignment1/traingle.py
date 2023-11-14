
z1=float(input("enter the first Sides of a triangle:"))

z2=float(input("enter the second Sides of a triangle: "))

z3=float(input("enter the  third Sides of a triangle: "))


if z3 < (z1 + z2) and z2 < (z3 + z1) and z1 < (z2 + z3) :

    print(" its possible")

else:

    print("its impossible")