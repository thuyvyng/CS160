from ast import literal_eval as eval
import sys, getopt

BOARD_SIZE = 6
O = 'O'
X = 'X'
DEFAULT = '_'
OFFSETS = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
INDEX = ((0,-1))
STOP = ((99,99))

#       -1      0      1
# -1  (-1,1)  (0,1)  (1,1)
#  0  (-1,0)  (0,0)  (1,0)
#  1  (-1,-1) (0,-1) (1,-1)

def instructions():
#Othello is a strategy game played by two players: Black and White.
#It is played on an 8x8 board (usually Green in colour), called the Othello board.
#The two players place 64 discs, each of which is black on one side and white on
#the other. For convenience, each player begins with 32 discs but these do not
#belong to him and if his opponent runs out of discs, he is obliged to give him some.
#A disc is black if the black side is visible and white if the white face is on top.

#The Goal

#The winner is the player who has more discs of his colour than his opponent at the
#end of the game. This will happen when neither of the two players has a legal move.
#Generally at this stage all 64 squares are occupied.

    input('\nPress Enter to continue...')

# Create Board with default pre-assign value '_', 'B', or 'W'
def default_board():
    # Assign default '_' for all X,Y
    # Use first 2 rows and last column to display number indexing
    GameBoard = [[DEFAULT for x in range(1,BOARD_SIZE+2)] for x in range(1, BOARD_SIZE+1)]
    #print ('default_board Board Size', BOARD_SIZE)
    # Assign X,Y index number
    for x in range(1,BOARD_SIZE-1):
        if x<10:
            GameBoard[0][x] = x             # Row 0 index 1-9
            GameBoard[1][x] = ' '           # Row 1 index spacing
        else:
            GameBoard[0][x] = 1             # Row 0 index 10-19     
            GameBoard[1][x] = x-10          # Row 1 index 10-19        
    for x in range(2,BOARD_SIZE):
        GameBoard[x][0] = ' '
        GameBoard[x][BOARD_SIZE-1] = ' '    # Column index spacing
        GameBoard[x][BOARD_SIZE] = x-1      # Last column index 1-19
    # Assign ' ' at different location 
    GameBoard[0][0] = ' '
    GameBoard[1][0] = ' '
    GameBoard[0][BOARD_SIZE] = ' '
    GameBoard[0][BOARD_SIZE-1] = ' '
    GameBoard[1][BOARD_SIZE] = ' '
    GameBoard[1][BOARD_SIZE-1] = ' '
    # Assign Default 'X' and 'O' in middle
    middle = (BOARD_SIZE+1)//2
    GameBoard[middle+1][middle-1] = X
    GameBoard[middle][middle] = X
    GameBoard[middle+1][middle] = O
    GameBoard[middle][middle-1] = O
    return GameBoard

# Update Board with latest patterns in "GameBoard" variable
def update_board(GameBoard):
    print()
    for x in range(len(GameBoard)):
        print(*GameBoard[x], sep='')
    print()
    return

# Invert location 'X'->'O' or 'O'->'X'
def inverse(XO):
    return O if XO is X else X

# inverse data at this location
def flip(GameBoard, XO, XY_enter, Surround_XY):
    check = [XY_enter[0]+Surround_XY[0], XY_enter[1]+Surround_XY[1]]
    while(GameBoard[check[0]][check[1]] is inverse(XO)):
        GameBoard[check[0]][check[1]] = XO
        check[0] += Surround_XY[0]
        check[1] += Surround_XY[1]
    return

# Game move location to be enter by player
def enter_location(GameBoard, XO):
    while(True):
        # Enter X,Y location
        try:
            enter_XY = eval(input('Enter X,Y value: 0,0 to quit: %s-turn >>> ' % XO))            
            #print ('enter_location', enter_XY[0], enter_XY[1]) 
            # Swap X,Y -> Y,X Location for easier processing
            tmp = [enter_XY[0], enter_XY[1]-INDEX[1]]
            YX_enter = tuple(reversed(tmp))
            # Exit due to player quitting 
            if GameBoard[YX_enter[0]][YX_enter[1]] is ' ':
                print()
                print('Quitting... Good Bye!!!')
                exit()
            # Check if location is valid before placement
            if find_xo_pair(GameBoard, XO, YX_enter):
                placement(GameBoard, XO, YX_enter)
                return
            else:
                raise AssertionError        
        # Check invalid X,Y input
        except (TypeError, ValueError, IndexError, SyntaxError, AssertionError):
            print('Invalid move. Try again.')

# Place selected move on Board and check to invert all location in between
def placement(GameBoard, XO, YX_enter):
    # Assign 'B' or 'W' to "GameBoard" variable at enter location
    GameBoard[YX_enter[0]][YX_enter[1]] = XO
    # Check each of all location surrounding the enter location to invert
    for Surround_YX in OFFSETS:
        check = [YX_enter[0]+Surround_YX[0], YX_enter[1]+Surround_YX[1]]
        # Check data for all location on Board
        while 1<=check[0]<BOARD_SIZE and 1<=check[1]<BOARD_SIZE:
            # If location data is default, exit while loop
            if GameBoard[check[0]][check[1]] is DEFAULT:
                break
            # If location data is the same, invert & exit while loop
            if GameBoard[check[0]][check[1]] is XO:
                #print ('placement invert location found at', tuple(reversed(check)))
                flip(GameBoard, XO, YX_enter, Surround_YX)
                break
            check[0] += Surround_YX[0]
            check[1] += Surround_YX[1]
    return

# Check location if its valid by checking surrounding location
def find_xo_pair(GameBoard, XO, YX_location):
    # Exit function False and invalid because location had 'B' or 'W'
    if GameBoard[YX_location[0]][YX_location[1]] is not DEFAULT:
        return False
    # Check each of all surrounding location
    #print ('find_xo_pair: ', XO, tuple(reversed(YX_location)))                
    for Surround_YX in OFFSETS:
        check = [YX_location[0]+Surround_YX[0], YX_location[1]+Surround_YX[1]]
        # Find first location of XO
        #print ('find_xo_pair: ', XO, tuple(reversed(check)))                
        while 1<=check[0]<BOARD_SIZE-1 and 1<=check[1]<BOARD_SIZE and \
              GameBoard[check[0]][check[1]] is inverse(XO):
            #print ('find_xo_pair: ', XO, tuple(reversed(check)), *GameBoard[check[0]][check[1]])                
            check[0] += Surround_YX[0]
            check[1] += Surround_YX[1]
            if GameBoard[check[0]][check[1]] is XO:
                #print ('find_xo_pair: ', XO, 'start', \
                #       tuple(reversed(YX_location)), 'end', tuple(reversed(check)))                
                return True
    return False

# Check all location to make sure there is a valid location
def has_valid_location(GameBoard, XO):
    for y in range(1,BOARD_SIZE):
        for x in range(1,BOARD_SIZE):
            #print ('has_valid_location', XO, (y,x))
            # Exit function True when encounter valid location on Board 
            if find_xo_pair(GameBoard, XO, (y,x)):
                #print ('has_valid_location True', XO, (y,x))
                return True
    # Exit function False when there is no valid location on Board
    #print ('has_valid_location False', XO, (y,x))
    return False

# Main Program
def main(argv):

    global BOARD_SIZE
    # Check command line and get Board size
    if len(sys.argv) == 3:
        if str.isdigit(sys.argv[2]):
            BOARD_SIZE = int(sys.argv[2]) + 2
        else:
            BOARD_SIZE = 10
    else:
        print ('python assignment8.py <option> <value>')
        print ('python assignment8.py -h 8')
        print ('<option>: -h for Instruction')
        print ('<value>:   N for Board Size NxN')
        exit()
    # Check command line and get instruction
    if sys.argv[1] == '-h':
        instructions()

    while True:
        # Start with default Board with command board size
        GameBoard = default_board()
        update_board(GameBoard)
        # Default 'O' go first
        XO = O
        # Start and continue games if the is valid location to select
        while has_valid_location(GameBoard, XO):
            # Ask player to enter location
            enter_location(GameBoard, XO)
            # Alternate between 'X' or 'O' if there is still valid location
            XO = inverse(XO)
            # display Board result  
            update_board(GameBoard)
        # Count Black & White on Board to determine winner, losser, or tie
        o_cnt, x_cnt = 0,0
        # Count each row
        for x in GameBoard:
            for count in x:
                if count is X:
                    x_cnt += 1
                if count is O:
                    o_cnt += 1
        # Printout result
        print()
        if o_cnt == x_cnt:
            print("It's a tie!")
        elif o_cnt>x_cnt:
            print('The winner is', O, '=', o_cnt, X, '=', x_cnt)
        else:
            print('The winner is', X, '=', x_cnt, O, '=', o_cnt)
        print('')
        answers = input('Enter anything to continue or return to quit: ')
        if answers == '':
            exit()
        new_N = input('Default NxN board is 8.  Enter new N or return to continue: ')
        if new_N == '':
            BOARD_SIZE = 9
        else:
            BOARD_SIZE = int(new_N) + 2
        
    return

if __name__ == '__main__':
    main(sys.argv[1:])
