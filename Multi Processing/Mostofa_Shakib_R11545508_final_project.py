"""
  Author: Mostofa Adib Shakib
  Date: 12/01/2020
  Language: Python
  Description:
   A multithreaded program capable of executing the first 100 steps of a modified cellular life simulator.
   This simulator receives the path to the input file as an argument containing the starting cellular matrix.
   The program then simulates the next 100 time-steps based on the algorithm defined.
"""

# Importing the necessary libraries

import sys, os
from utils import *
from multiprocessing import Pool

def main():

	# Reads all the commend line arguments that are passed

    n = len(sys.argv)

    if sys.argv[1] == "-i":
    	inputFileLocation = sys.argv[2]

    f = open(inputFileLocation, "r")

    if sys.argv[3] == "-o":
    	outputFileDestination = sys.argv[4]

    # If -t is not passed then the default value for the number of thread is 1

    numberOfThreads = 1

    # If -t is passed we parse the thread count from the command line argument

    if n > 5 and sys.argv[5] == "-t":
    	numberOfThreads = int(sys.argv[6])

    Lines = f.readlines()

    board = []

    # Reads the input file line by line and initializes them to a 2D matrix as the starting cellular matrix

    for line in Lines:
    	board.append(list(line.strip()))

    rows = len(board)					# Calculates the number of rows in the matrix
    columns = len(board[0])				# Calculates the number of columns in the matrix
    aliveCells = 0

    print("Project :: R11545508\n")

    # Initializing the multiprocessing object

    processPool = Pool(processes=numberOfThreads)

    for i in range(100):
    	# Make the processed matrix the initial matrix for the ith iteration
    	if i > 0:
    		board = result

    	poolData = []

    	dividend = rows//numberOfThreads
    	extraThreads = rows % numberOfThreads
    	count = numberOfThreads
    	startRow = 0
    	endRow = startRow + dividend

    	# Break down the original matrix into submatrices where each worker takes 'dividend' number of rows
    	# If there are extra threads then we give each workers one more row to process in an attempt to divide the work as equally as possible

    	while(count > 1):
    		if extraThreads > 0:
    			poolData.append([board, startRow, endRow+1])
    			startRow = endRow+1
    			endRow = startRow + dividend
    			count -= 1
    			extraThreads -= 1
    		else:
    			poolData.append([board, startRow, endRow])
    			startRow = endRow
    			endRow = startRow + dividend
    			count -= 1

    	poolData.append([board, startRow, rows])

    	# This processes individual submatrices using the multiprocessing library

    	finalData = processPool.map(processMatrix, poolData)

    	del (poolData)	# Delete the poolData in order to save space

    	# We need to convert the 3D matrix to a 2D matrix which will be used as the starting matrix for the next iteration

    	result = finalData[0]

    	for i in range(1, len(finalData)):
    		result += finalData[i]

    # This writes the 100th iteration to an output file

    with open(outputFileDestination, "w") as fp:
    	for row in range(rows):
    		string = ""
    		for column in range(columns):
	        	string += result[row][column]

    		fp.write(string + "\n")

if __name__ == '__main__':
    main()