print ("Weclome to my calculator")
print ("")
print ("Please type if you would like to add, subtract, divide or multiply!: ")

addorsub = input()

if addorsub == str("add"):
	print ("Please enter the first number you would like to add:")
	int1 = input()
	print ("Please enter the second number you would like to add:")
	int2 = input()
	print ("Your answer is: " , int(int1) + int(int2) )

if addorsub == str("subtract"):
	print ("Please enter the first number you would like to subtract:")
	int1 = input()
	print ("Please enter the second number you would like to subtract:")
	int2 = input()
	print ("Your answer is: " , int(int1) - int(int2) )

if addorsub == str("multiply"):
	print ("Please enter the first number you would like to multiply:")
	int1 = input()
	print ("Please enter the second number you would like to multiply:")
	int2 = input()
	print ("Your answer is: " , int(int1) * int(int2) )

if addorsub == str("divide"):
	print ("What is the number you would like to divide: ")
	int1 = input()
	print ("How many times would you like to divide into it: ")
	int2 = input()
	print ("Your answer is: " , int(int1) / int(int2) )
