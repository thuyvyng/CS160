def part1():
	listone = []
	try:
		ask1 = int(input("How many integers?"))
	except:
		print("Incorrect input! Exiting")
		return
	try:	
		for x in range(ask1):
			list1 = int(input("Enter your integers "))
			listone.append(list1)
	except:
		print("Incorrect input! Exiting") 
		return


	a = sum(listone)
	print(listone)	


	listtwo =  []
	try:
		ask2 = int(input("How many integers? "))
	except:
		print("Incorrect input! Exiting")
		return
	try:
		for x in range(ask2):
			list2 = int(input("Enter set of integers "))
			listtwo.append(list2)	
	except:
		print("Incorrect input, goodbye")
		return
	b = sum(listtwo)
	print(listtwo)


	if ask1  > ask2 :
		print("Your first list is longer")
	elif ask2 > ask1:
		print("Your second list is longer")
	else:
		print("Neither line is longer than the other")

	if a > b :
		print("Your first line is greater")
	elif b > a :
		print("Your second line is greater")
	else:
		print("Neither line is greater than the other")



	new_list = []

	for stuff in listone:
		if stuff in listtwo:
			new_list.append(stuff)

	print(new_list)


	return


def main():
	part1()
main()

