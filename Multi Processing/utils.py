__name__ = 'utils'

# A helper function that checks how many neighbouring alive cells does a particular cell have
def checkNeighbours(board, row, column):
    cells = 0
    
    # Check the left cell
    if board[row][ (column-1) % len(board[0]) ] == 'O':
        cells += 1
    
    # Check the right cell
    if board[row][ (column+1) % len(board[0]) ] == 'O':
        cells += 1
    
    # Check the top cell
    if board[ (row-1) % len(board) ][column] == 'O':
        cells += 1

    # Check the bottom cell
    if board[ (row+1) % len(board) ][column] == 'O':
        cells += 1
    
    # Check the bottom-right cell
    if board[ (row+1) % len(board) ][ (column+1) % len(board[0]) ] == 'O':
        cells += 1
    
    # Check the bottom-left cell
    if board[ (row+1) % len(board) ][ (column-1) % len(board[0]) ] == 'O':
        cells += 1
    
    #  Check the top-right cell
    if board[ (row-1) % len(board) ][ (column+1) % len(board[0]) ] == 'O':
        cells += 1

    # Check the top-left cell
    if board[ (row-1) % len(board) ][ (column-1) % len(board[0]) ] == 'O':
        cells += 1
        
    return cells

# A helper function that takes a submatrix and processes it based on the predefined algorithm
def processMatrix(matrixData):
    board = matrixData[0]
    startRow = matrixData[1]
    endRow = matrixData[2]
    columnLength = len(board[0])

    # Initializing the submatrix for the next board

    difference = endRow - startRow
    nextBoard = [ [0 for col in range(columnLength)] for row in range(difference) ]

    # We iterate over each cell in the submatrix and decide if a given cell will be alive/dead based on the predefinded algorithm

    for row in range(difference):
        for column in range(columnLength):
            aliveCells = checkNeighbours(board, startRow+row, column)
                            
            if board[startRow+row][column] == 'O':
                if aliveCells == 2 or aliveCells == 3 or aliveCells == 4:
                    nextBoard[row][column] = 'O'
                else:
                    nextBoard[row][column] = '.'
            else:
                if aliveCells > 0 and aliveCells % 2 == 0:
                    nextBoard[row][column] = 'O'
                else:
                    nextBoard[row][column] = '.'

    return nextBoard

