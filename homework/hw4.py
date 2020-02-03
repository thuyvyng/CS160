
def Programmer():
	try:
		number = int(input("Insert number: "))
	except: 
		print("Incorrect Input! Exiting!")
		return 
	binary = ""
	while number > 0:
		rem = str(number % 2)
		number = number // 2
		binary = rem + binary
	print(binary)
	
	question2 = input("Continue Programmer Mode? Y/N ")
	if question2 == "Y":
		Programmer()
		return	
	elif question2 == "N":
		print("Exiting mode ")
		return
	else:
		print("Incorrect Input! Exiting. ")
		return
	

def Scientific():
	try:
		num1 = float(input("Insert first number: "))
		num2 = float(input("Insert second number: "))
	except:
		print("Incorrect Input! Exiting ")
		return
	sign = input("Insert Operation: ")
	if sign == "+":
		addition = num1 + num2
		print(str(addition))

	elif sign == "*":
		print(str(num1 * num2))

	elif sign == "-":
		print(str(num1 - num2))	

	elif sign == "**":
		print(str(num1 ** num2))	

	elif sign == "/":
		print(str(num1 / num2))
	else:
		print("Incorrect Input! Exiting!")
		return

	q = input("Continue Scientific Mode? Y/N ")
	if q == "Y":
		Scientific()
	elif q == "N":
		print("Exiting mode ")
	else:
		print("Incorrect Input! Exiting. ")

	return	

def Quest():
	question = input("Programmer or Scientfic ")

	if question == "Programmer":
		Programmer()

	elif question == "Scientific":
		Scientific()
	else:
		print("Incorrect Input! ")


	ask = input("Continue Program: Y/N ")
	if ask == "Y":
		Quest()
	elif ask == "N":
		print("Exiting ")
	else:
		print("Incorrect Input! Exiting ")

	return	



Quest()







