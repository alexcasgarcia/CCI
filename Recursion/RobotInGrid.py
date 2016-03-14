#Imagine a robot sitting on the upper left corner of grid with r rows and c columns.  The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them.  Design an algorithm to find a path for the robot from the top left to the bottom right.


def FindPathToBottomRight(grid,x,y):
	if IsCellAvailableForMove(grid,x+1,y):
		return ">" + FindPathToBottomRight(grid,x+1,y)
	elif IsCellAvailableForMove(grid,x,y+1):
		return "v" + FindPathToBottomRight(grid,x,y+1)
	if IsBottomRightCell(grid,x,y):
		return "."

def IsCellAvailableForMove(grid,x,y):
	if IsInsideGrid(grid,x,y) and IsCellEmpty(grid,x,y):
		return True
	else:
		return False

def IsCellEmpty(grid,x,y):
	print "(" + str(x) + "," + str(y) + ") = " + str(grid[x][y])
	if grid[x][y] == 0:
		return True
	else:
		return False

def IsInsideGrid(grid,x,y):
	gridWidth = len(grid)
	gridHeight = len(grid[0])

	if x < gridWidth and y < gridHeight:
		return True
	else:
		return False 

def IsBottomRightCell(grid,x,y):
	gridWidth = len(grid)
	gridHeight = len(grid[0])

	if x == gridWidth - 1 and y == gridHeight - 1:
		return True
	else:
		return False


myGrid1 = [[0,0,0],[1,0,0],[0,0,0]]
myGrid2 = [[0,0,0,0,0,0],[1,1,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

print FindPathToBottomRight(myGrid2,0,0)
