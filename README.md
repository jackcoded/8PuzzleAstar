# 8puzzleAstar
How to compile and run
python ./puzzle.py


Goal state 
[1,2,3,8,0,4,7,6,5]


Heuristic Function - Manhattan

Description: Manhattan Heuristic counts the total distance for all blocks from source to destination.
How it works:
My board is a just a single list of numbers, for example [1,2,3,4,5,6,7,8,0]
Because it’s just a list of numbers, it is difficult to count rows and columns when there isn’t any. 
By using the mod 3 technique for columns and divide 3 and round down for rows, we can check if they’re in the same row and columns and the distance between them.
First get the number board, discard 0 for admissible heuristic
for i in board:
    if i is not 0:
Getting displacement
displacement = abs(goalState.index(i) - board.index(i))
Check if same row 
if abs(int(math.floor(goalState.index(i) / 3)) - int(math.floor(board.index(i) / 3))) == 0
	distance += displacement 
Check if same col
	if abs(goalState.index(i) % 3 - board.index(i) % 3) == 0
	distance += int(math.floor(displacement / 3))
if not same col or row
	  col = displacement % 3
row = int(math.floor(displacement / 3))
distance += row + col
if not same col or row and both src and goal are both edges added to the previous distance as well
if abs(goalState.index(i) % 3 - board.index(i) % 3) == 2 and displacement % 3 == 1:
distance += 2 
This is all looped through each number on the board till return the total distance
