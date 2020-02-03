print(4//3//2)
print(4/3/2)
print(1//2*8)
print(5*10//2+10/5.0)
print(3+2*4//5+8+2)
print((3+2)*4//(5+8)+2)
print((3+2)*4//5+(8+2))
print(20.0/4*2**3)
print(5.5*2+4//2)
print(False and True)
print(not False)
print(True or False)
print(not True or False and False or True)
print(not ((True or False) and (False or True)))
print(not True and False)
print(not (True and False))
print(False and not False or False)
a = 0.0
b = 1.0
c = True
d = False

print(b-a/10)
print((b-a)/10)
print(not c or not d)
print(chr(84)+chr(104)+chr(117)+chr(121)+chr(45)+chr(86)+chr(121)+chr(32)+chr(78)+chr(103)+chr(117)+chr(121)+chr(101)+chr(110))

#Design and Write a Program
for x in range(3):
	number = int(input("Insert radius here "))
	third = (number**3)
	#water = 62.4
	volume = 4/3*(22/7)
	buoyant = int(third*62.4*volume)
	weight = int(input("Insert weight here "))

	if buoyant >= weight:
		print("This sphere will float")
	else:
		print("This sphere will sink")



