def userinput():
	flist = []
	blank = ""

	askf = int(input("How many fruits?  "))

	for x in range(askf):
		fruits = input("Enter fruit: ")
		pounds = input("Enter number of pounds of " + fruits+ " : " )
		flist.append([fruits,pounds])
#	print(flist)

	for i in range(len(flist)):
		for j in range(len(flist)):
			if flist[j] > flist[i]:
				temp = flist[j]
				flist[j] = flist[i]
				flist[i] = temp

	for i in range(len(flist)):
		print(flist[i][0] + "," + str(flist[i][1]))


#	print(flist)
	

	return 


def main():	
	userinput()
      
main()
