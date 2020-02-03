def param(x,y):
	print("in function our variables: " + str(x)+ " " + str(y))
	z = x + y
	#return z


def main():
	a = 1
	b = 2
	c = 4
	hello = 57
	x = 5
	y = 20
	world = 1000000
	print(param(x,y))
	print(param(x,a))
	print(param(hello, world))
	print(param(c, b))
main()
