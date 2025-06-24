#program to find maximum between three numbers
a=int(input("Enter a first number"))
b=int(input("Enter a second number"))
c=int(input("Enter a third number"))
if a > b and a > c :
	print(f"{a} is Maximum")
elif b > a and b > c  :
	print(f"{a} is Maximum")
else :
	print(f"{c} is Maximum")