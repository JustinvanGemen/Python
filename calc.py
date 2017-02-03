#Defining calculator functions.
def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
#Starting a while loop so that the program can repeat if asked to do so.
while True:
#Asking user to select an operation.
	print("Select operation.")
	print("1.Add +")
	print("2.Subtract -")
	print("3.Multiply *")
	print("4.Divide /")
	
	while True:
		try:
			choice = int(input("Enter your choice(1/2/3/4):"))
			break
		except:
			print("That is not an available choice.")
#Asking user for their first number and checking if it is an int.
	while True:
		try:
			num1 = int(input("Enter first(left) number: "))
			break
		except NameError:
			print("That's not a number!")
#Asking user for their second number and checking if it is an int.
	while True:
		try:
			num2 = int(input("Enter second(right) number: "))
			break
		except NameError:
			print("That's not a number!")
#Going through ifs to give them their answer.
	if choice == 1:
		print num1,"+",num2,"=", add(num1,num2) 
	elif choice == 2:
		print num1,"-",num2,"=", subtract(num1,num2) 
	elif choice == 3:
		print num1,"*",num2,"=", multiply(num1,num2)
	elif choice == 4:
		try:
			print num1,"/",num2,"=", divide(num1,num2)
		except ZeroDivisionError:
			input("Dividing By Zero is not possible, press enter to exit the program.")
	else:
		print("Your input was invalid.")
#Asking them to press a key to exit program.
	while True:
		answer = raw_input('Run again? (Yes/No): ')
		if answer in ('Yes', 'No'):
			break
		print 'Invalid input.'
		if answer == Yes:
			continue
		else:
			print 'Goodbye'
			break
quit(0)