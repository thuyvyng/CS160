
def board(n):
	for i in range(1,n):
		print(i, end = "\t")
	print()
	print("__________________________________________________________\n")

	for j in range(1,n):
		for w in range(1,n):
			print( j*w, end = "\t")
		print("\n")

	return

def main():
#	print("\t\t\t Multiplication Tables \n")
	print("\n")
	x = int(input("How many rows/columns do you want? "))
	n = x+1 
	print("\n")
	board(n)

main()




#how shannon did the tic tac toe board
"""def board_setup(n):
	board = [" "]*n
	for i in range(n):
		board[i] = [" "]*n
	return board


def show_board(board):
	print("\n")
	for i in range(len(board)):
		for j in range(len(board[i])):
			print("|" + board[i][j] + "|" , end = "")

		print("\n")

	return


def main():
	n = int(input("How many rows/columns do you want? "))
	board = board_setup(n)
	show_board(board)


main()"""




