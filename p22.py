# Exercise 4: What wil the output of following code
import random
a=int(input("Guess a number between 1 to 10 :"))
number=random.randint(1,10)
if(a == number):
	print("You entered a correct nummber") 
elif (a < number):
	print("😢,Too low,Try again")
else:
	print("😢,Too high,Try again")

print("It is ", number)