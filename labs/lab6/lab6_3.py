def userinput():
	ask = input("Insert a word yo ")
	list1 = list(ask)
	print(list1)
	a = []
	for i in range(len(list1)):
		for j in range(len(list1)):
			if list1[j] > list1[i]:
				temp = list1[j]
				list1[j] = list1[i]
				list1[i] = temp
	print(list1)
	return

def main():
	userinput()

main()
