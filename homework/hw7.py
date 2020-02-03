
def isNumber(input_str):
	for char in input_str:
		if char in ('0123456789'):
			return True
		else:
			return False
	return 
   
def str2int(input_str):
	Decimal = {9:100000000, 8:10000000, 7:1000000, 6:100000, 5:10000, 4:1000, 3:100, 2:10, 1:1}
	Digit = {'0': 0,'1':1, '2':2, '3':3, '4':4 , '5':5, '6':6, '7':7, '8':8, '9':9}
	input_length = 0
	for char in input_str:
		input_length += 1
	number = 0
	for char in input_str:
		number += (Digit[char] * Decimal[input_length])
		input_length -= 1
	return number

################################################################################



def isPositive(): #works!!!!
	x  = input("Enter a string to determine it is a positive integer: ")
     
	if isNumber(x):
		print("Number", x, "is Positive" )
	else:
		print("Number", x, "is Not Positive" )
    
def isDecimal():
	x = input("Enter a string to determine it is a Decimal: ")

	for char in x:
		if char not in ('0123456789-+.'):
			print("Number", x, "is Not a Decimal")
			return 0
	print("Number", x, "is a Decimal")
    
def inBound(): #works
	x  = input("Enter X or Y position value: ")
	x1 = input("Enter X or Y maximum value: ")
	if isNumber(x) and isNumber(x1):
		if str2int(x)  <= str2int(x1) :
			print("Number", x, "is in Bound of ", x1)
		else:
			print("Number", x, "is not in Bound of ", x1)
	else:
		print("Number", x, x1, "is not Decimal ")
    
def capitalsPresent(): #works
	x = input("Enter a string to determine Capital Present: ")
	for char in x:
		if char in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
			print("String", x,  "has Capital letter Present")
			return 0
	print("String", x,  "has No Capital letter Present")
    
def numbersPresent(): #works
	x =input("Enter a string to determine numbers Present: ")
	for char in x:
		if char in ('0123456789'):
			print("String", x, "has Numbers Present")
			return 0
	print("String", x, "has No Numbers Present")
          
def isEven(): #work
	x = input("Enter a string to determine it is Even integer: ")
	if isNumber(x) == True :
		if str2int(x)%2 == 0:
			print("Number", x,"Number is Even")
		else:
			print("Number", x,"Number is Not Even")
	else:
		print("Not Positive")
    
def isOdd(): #work
	x = input("Enter a string to determine it is Odd integer: ")
	if isNumber(x):
		if str2int(x)%2 == 1:
			print("Number", x,"Number is Odd")
		else:
			print("Number", x, "Number is Not Odd")
	else:
		print("Number", x,"Not Positive")
    
def isCorrectLength(): #work
	x = input("Enter a string: ")
	it1 =input("Enter a length of string: ")
	it_length = 0
	for char in x:
		it_length += 1
	if isNumber(it1):
		if it_length == str2int(it1):   
			print("String", x, "Correct Length is", it_length)
		else:
			print("Incorrect length entered")

def main():
	ans = True
	
	#These are the instructions
	print( "1 - isPositive")
	print( "2 - isDecimal")
	print( "3 - inBound")
	print( "4 - capitalsPresent")
	print( "5 - numbersPresent")
	print( "6 - isEven")
	print( "7 - isOdd")
	print( "8 - isCorrectLength")
	while ans:
		print( "")
		answers = input("Enter 1..8 or other to quit: ")
		if answers == "1": #works
			isPositive()
		elif answers == "2": #work
			isDecimal()   
		elif answers == "3": #work
			inBound()   
		elif answers == "4": #works
			capitalsPresent()   
		elif answers == "5": #works
			numbersPresent()
		elif answers == "6": #work
			isEven()    
		elif answers == "7": #work
			isOdd()   
		elif answers == "8": #work
			isCorrectLength()
		else:
			return
main()
