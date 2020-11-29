import sys, os

def main():

    n = len(sys.argv)

    if sys.argv[1] == "-i":
    	inputFileLocation = sys.argv[2]

    f = open(inputFileLocation, "r")

    if sys.argv[3] == "-o":
    	outputFileDestination = sys.argv[4]

    numberOfThreads = 1

    if n > 5 and sys.argv[5] == "-t":
    	numberOfThreads = sys.argv[6]

    Lines = f.readlines()

    board = []

    for line in Lines:
    	board.append(list(line.strip()))

    rows = len(board)
    columns = len(board[0])
    aliveCells = 0

    print("Project :: R11545508\n")
    
    def checkNeighbours(board, row, column):
        cells = 0
        
        if board[row][ (column-1) % len(board[0]) ] == 'O':
            cells += 1
        
        if board[row][ (column+1) % len(board[0]) ] == 'O':
            cells += 1
            
        if board[ (row-1) % len(board) ][column] == 'O':
            cells += 1
        
        if board[ (row+1) % len(board) ][column] == 'O':
            cells += 1
        
        if board[ (row+1) % len(board) ][ (column+1) % len(board[0]) ] == 'O':
            cells += 1
            
        if board[ (row+1) % len(board) ][ (column-1) % len(board[0]) ] == 'O':
            cells += 1
            
        if board[ (row-1) % len(board) ][ (column+1) % len(board[0]) ] == 'O':
            cells += 1
            
        if board[ (row-1) % len(board) ][ (column-1) % len(board[0]) ] == 'O':
            cells += 1
            
        return cells

    nextBoard = [ [0 for col in range(columns)] for row in range(rows) ]

    for i in range(100):
    	if i > 0:
    		board = nextBoard
    		nextBoard = [ [0 for col in range(columns)] for row in range(rows) ]

    	for row in range(rows):
	        for column in range(columns):
	            aliveCells = checkNeighbours(board, row, column)
	                            
	            if board[row][column] == 'O':
	                if aliveCells == 2 or aliveCells == 3 or aliveCells == 4:
	                    nextBoard[row][column] = 'O'
	                else:
	                    nextBoard[row][column] = '.'

	            else:
	                if aliveCells > 0 and aliveCells % 2 == 0:
	                    nextBoard[row][column] = 'O'
	                else:
	                    nextBoard[row][column] = '.'

    with open(outputFileDestination, "w") as fp:
    	for row in range(rows):
    		string = ""
    		for column in range(columns):
	        	string += nextBoard[row][column]

    		fp.write(string + os.linesep)

if __name__ == '__main__':
    main()

