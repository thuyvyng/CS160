def userinput():
	numlist = []
	length = int(input("How many numbers are you inserting? "))
	for x in range(length):
		number = int(input("Enter number:"))
		if number >= 1 and number <= 1000:
			numlist.append(number)
	print(numlist)
	
	return

def main():
	userinput()
main()
