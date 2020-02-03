#password generator
import random, sys
from random import choice
from string import ascii_uppercase
from string import ascii_lowercase
from string import digits

def gen_password(length, sym, capital):
	password = ""
	capLoc = []

	#random location for caps
	count = 1
	while count <= capital:
		x = random.randint(1, length)
		if x not in capLoc:
			capLoc.append(x)
			count = count + 1

	count = 1

	while count <= length:
		if count in capLoc:
			password += ''.join(choice(ascii_uppercase))
		else: 
			password += ''.join(choice(ascii_lowercase + digits + sym))
		count = count +1

	print("Password = ", password)

	return

def main():
	
# user input here---------------------------------------------------
	length = int(input("Enter length of password: "))
	capital = int(input(" Enter how many capital letters can be used"))
	symbols = input("Enter which special characters can be used: ")

	gen_password(length, symbols, capital)


main()


