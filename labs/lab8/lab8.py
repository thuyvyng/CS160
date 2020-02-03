import sys
import os.path

def alpha(v):
	v = v.lower()
	histogram = []

	for char in v:
		newletter = True;
		for entry in histogram:
			if entry[0] == char:
				entry[1] += 1
				newletter = False;

		if newletter == True:
			histogram.append([char,1])

	return histogram

def main():
#	ans = ' '
	#print("Type in the file names")
	# names of files are alice.txt jungle.txt yellow.txt

	if len(sys.argv) < 4:
		print('too few command line arguments')
		exit()
	elif len(sys.argv) > 4:
		print('too many commannd line arguments')
		exit()
	else:
		if os.path.exists(sys.argv[1]):
			file1 = open(sys.argv[1], "r")
		else: 
			print('File', sys.argv[1], 'does not exist')
			exit()
		if os.path.exists(sys.argv[2]):
			file2 = open(sys.argv[2], "r")
		else: 
			print('this file doesnt exist')
			exit()
		if os.path.exists(sys.argv[3]):
			file3 = open(sys.argv[3], "r")
		else:
			print('this file doesnt exist')
			exit()

	new = open("freq.txt","r+")
		
	
	x = file1.read()
	y = file2.read()
	z = file3.read()
	
	new.write(x)
	new.write(y)
	new.write(z)

	file1.close()
	file2.close()
	file3.close()
	new.close()
	
	new = open("freq.txt", "r")
		
	weird = new.read()
	weird = alpha(weird)

	#print(weird)
	fileText = ""
	for i in range(len(weird)):
		fileText = fileText + ": ".join(str(x) for x in weird[i]) + "\n"

	#ok = ''.join(weird)
		
	new.close()
	cool = open("freq.txt", "w")

	cool.write(fileText)

	cool.close()
	print('output file: freq.txt')
	return

main()
