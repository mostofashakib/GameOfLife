import sys, os
from utils import *
from multiprocessing import Pool

def main():

    n = len(sys.argv)

    if sys.argv[1] == "-i":
    	inputFileLocation = sys.argv[2]

    f = open(inputFileLocation, "r")

    if sys.argv[3] == "-o":
    	outputFileDestination = sys.argv[4]

    numberOfThreads = 1

    if n > 5 and sys.argv[5] == "-t":
    	numberOfThreads = int(sys.argv[6])

    Lines = f.readlines()

    board = []

    for line in Lines:
    	board.append(list(line.strip()))

    rows = len(board)
    columns = len(board[0])
    aliveCells = 0

    print("Project :: R11545508\n")

    for i in range(100):
    	if i > 0:
    		board = result

    	processPool = Pool(processes=numberOfThreads)
    	poolData = list()

    	dividend = rows//numberOfThreads
    	count = numberOfThreads
    	startRow = 0
    	endRow = startRow + dividend

    	while(count > 1):
    		poolData.append([board, startRow, endRow])
    		startRow = endRow
    		endRow = startRow + dividend
    		count -= 1

    	poolData.append([board, startRow, rows])

    	finalData = processPool.map(processMatrix, poolData)

    	del (poolData)

    	result = finalData[0]

    	for i in range(1, len(finalData)):
    		result += finalData[i]

    with open(outputFileDestination, "w") as fp:
    	for row in range(rows):
    		string = ""
    		for column in range(columns):
	        	string += result[row][column]

    		fp.write(string + "\n")

if __name__ == '__main__':
    main()