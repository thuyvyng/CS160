def board_su(n):
	board = [""]*n
	for i in range(n):
		board[i] = ["   "]*n
		print(i, end = "\t")
	return board

def show_board(board):
	print("\n")
	for i in range(len(board)):
		print(i+1, end = "\t")
		for j in range(len(board[i])):
			print("|" + board[i][j] + "|", end = "")
		
		print("\n")

	return






def main():
	n = int(input("How many rows/columns do you want? "))
	board = board_su(n)
	show_board(board)

main()


"""def board(n):
	for i in range(1,n):
		print(i, end = "\t")
	print()
	print("____________________________________________________\n")

	for j in range(1,n):
		for w in range(1,n):
			print(i, end = "\t")
		print("\n")
	return

def main():
	n = int(input("How many rows/columns do you want? "))
	board(n)
	print("\n")


main()



"""
















