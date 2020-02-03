import turtle
my_turtle = turtle.Turtle()
window = turtle.Screen()

def star(a,b):
	my_turtle.color("yellow")
	my_turtle.clear()
	for x in range(5):
		my_turtle.forward(300)
		my_turtle.right(144)

	return


def name(a,b):
	

	my_turtle.clear()
	my_turtle.reset()

	my_turtle.color("purple")
		
	my_turtle.forward(90) #T
	my_turtle.right(90)
	my_turtle.forward(120)
	my_turtle.right(180)
	my_turtle.forward(120)
	my_turtle.right(90)
	my_turtle.forward(100)

	my_turtle.right(90) #h
	my_turtle.forward(120)
	my_turtle.right(180)
	my_turtle.forward(50)
	my_turtle.right(90)
	my_turtle.forward(50)
	my_turtle.right(90)
	my_turtle.forward(50)


	my_turtle.left(90) #u
	my_turtle.forward(15)
	my_turtle.left(90)
	my_turtle.forward(50)
	my_turtle.left(180)
	my_turtle.forward(50)
	my_turtle.left(90)
	my_turtle.forward(45)
	my_turtle.left(90)
	my_turtle.forward(50)
	my_turtle.right(90)
	my_turtle.forward(10)
	
	my_turtle.right(90) #y
	my_turtle.forward(50)
	my_turtle.left(90)
	my_turtle.forward(40)
	my_turtle.left(90)
	my_turtle.forward(50)
	my_turtle.right(180)
	my_turtle.forward(120)
	my_turtle.right(90)
	my_turtle.forward(40)
	my_turtle.right(125)
	my_turtle.forward(120)
	my_turtle.right(55)
	my_turtle.forward(35)


	my_turtle.left(105) #V
	my_turtle.forward(95)
	my_turtle.left(180)
	my_turtle.forward(125)
	my_turtle.left(150)
	my_turtle.forward(125)

	my_turtle.left(180)
	my_turtle.forward(65)
	my_turtle.left(105)
	my_turtle.forward(5)

	my_turtle.right(90)
	my_turtle.forward(50)
	my_turtle.left(90)
	my_turtle.forward(40)
	my_turtle.left(90)
	my_turtle.forward(50)
	my_turtle.right(180)
	my_turtle.forward(120)
	my_turtle.right(90)
	my_turtle.forward(40)
	my_turtle.right(125)
	my_turtle.forward(120)
	
	return 
	
def main():
	my_turtle.speed(10)
	my_turtle.pos()
	(0.00,0.00)
	question = input("Do you want turtle to draw you a star or spell out my name?:Input Star or Name ")
		
	print("Click on the turtle or arrow thing! Click on the x in the corner to exit!  ")


	if question == "Star":
		my_turtle.onclick(star)
		#my_turtle.onclick(clearscreen)
	elif question == "Name":
		my_turtle.onclick(name)
	else:
		print("Incorrect Input")	
		main()

	window.mainloop()
	return 

main()

