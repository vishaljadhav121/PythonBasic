#program to print multiplication table of entered number
a=int(input("Enter a number"))
for i in range(1,11):
	print(f"{a} * {i} = {a*i}")