def userinput():
	namelist = []
	try:
		length = int(input("How many names? "))
	except:
		print("Bad input!!! exiting")
		return
	try:	
		for x in range(length):
			name = input("Enter name: ")
			namelist.append(name)
	except:
		print(" no" )
		return

	for i in range(0, length):
		namelist[i] = namelist[i].lower()

	histogram = []

	for word in namelist:
		for letter in word: #????????????? make uppercase
			newletter = True;
			for entry in histogram:
				if entry[0] == letter:
					entry[1] += 1
					newletter = False;

			if newletter == True:
				histogram.append([letter,1])

	for i in range(len(histogram)):
		for j in range(len(histogram)):
			if histogram[j] > histogram[i]:
				temp = histogram[j]
				histogram[j] = histogram[i]
				histogram[i] = temp
	

	print(histogram)

	return

def main():
	userinput()
main()
