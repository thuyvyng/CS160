def userinput():
	numlist = []
	no = str("over")
	length = int(input("How many numbers are you putting in? "))
	for x in range(length):
		number = int(input("Enter a number: "))
		if number <= 100:
			numlist.append(number)

		elif number > 100:
			numlist.append("over")
		else:
			print("incorrect input u suck ")
	print(numlist)
	return

def main():
	userinput()

main()
