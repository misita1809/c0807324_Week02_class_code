"""Name: Misita Sankhala
Std Id: C0807324
Emerging Technologies
Week02"""

import area_of_circle, reverse_name
print("\n---------------Area of Circle-------------------\n")
radius = float(input("Enter Radius of Circle: "))
print(f"Area of Circle with Radius {radius} is {area_of_circle.area(radius)}")

print("\n\n--------------------Reverse--------------------\n")
f_name = input("Enter your First name: ")
l_name = input("Enter your Last name: ")
print(f"The Reverse of {f_name} {l_name} is {reverse_name.reverse(f_name,l_name)}")