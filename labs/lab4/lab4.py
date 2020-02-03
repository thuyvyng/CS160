stars = int(input("How many stars do you want? "))
while (stars % 2 == 0):
	stars = int(input(" Enter an odd number "))
 
for x in range(stars +1):
	if x % 2 == 0:
		continue
	space = (stars-x)//2
	print(" " * space + "*" * x + " " * space)

