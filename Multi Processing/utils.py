__name__ = 'utils'

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

def processMatrix(matrixData):
    board = matrixData[0]
    startRow = matrixData[1]
    endRow = matrixData[2]
    columnLength = len(board[0])

    difference = endRow - startRow
    nextBoard = [ [0 for col in range(columnLength)] for row in range(difference) ]

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

