import heapq
import math
from random import shuffle
import time
import random


class state:
    boardState = []
    parent = []
    step = 0
    h = 0
    g = 0
    f = 0


    def __lt__(self, other):
        return

    def __eq__(self, other):
        return self.boardState == other.boardState

    # initiate the board with given numbers
    def __init__(self, numbers, prev_state = None):
        self.boardState = numbers
        self.parent = prev_state
        self.step = 0
        if self.parent:
            self.step = self.parent.step + 1
        self.h = self.manhattan(self.boardState)
        self.f = self.step + self.h

    # prints the board
    def print_state(self, state):
        for count, i in enumerate(state, start=1):
            print(i, end=" ")
            if count % 3 == 0:
                print()

    # moves block by switching array element
    def state_move_block(self, boardState, source, dest, move):
        newState = list(boardState)
        newState[source], newState[dest] = newState[dest], newState[source]
        # self.print_state(newState)
        # print(newState[source], "-", move)
        return newState

    def manhattan(self, board):
        distance = 0
        col = 0
        row = 0
        #print(board)
        goalState = [1,2,3,8,0,4,7,6,5]
        for i in board:
            if i is not 0:
                #print(i)
                displacement = abs(goalState.index(i) - board.index(i))
                if abs(int(math.floor(goalState.index(i) / 3)) - int(math.floor(board.index(i) / 3))) == 0:
                    distance += displacement
                    #print("method 1,  distance",displacement)
                elif abs(goalState.index(i) % 3 - board.index(i) % 3) == 0:
                    #print ("method 2, distance",int(math.floor(displacement / 3)))
                    distance += int(math.floor(displacement / 3))
                else:
                    # found the amount of column between goal
                    col = displacement % 3
                    #print("col", col)
                    # found the amount of row between goal
                    # round down
                    row = int(math.floor(displacement / 3))
                    #print("row", row)
                    distance += row + col
                    #print("method 3, distance ", row + col+2)
                    if abs(goalState.index(i) % 3 - board.index(i) % 3) == 2 and displacement % 3 == 1:
                        distance += 2
                        #print("method 4 +2 ")
        #print("H value is", distance)
        return distance

    #hamming heuristic
    def calculateHeuristic(self, state):
        goalState = [1,2,3,8,0,4,7,6,5]
        wrongtile = 0
        for count, i in enumerate(state, start=0):
            if i == 0:
                continue
            elif i != goalState[count]:
                wrongtile += 1;
        #print(wrongtile)
        return wrongtile

    # finds the possible moves at given location on the board
    def possibleMoves(self, boardState):
        index = boardState.index(0)
        possibleStates = list([])
        # checks if 0 is on the top, up move is available
        if not index > 5:
            possibleStates.append(self.state_move_block(boardState, index, index + 3, "up"))

        # checks if 0 is on the bottom,down move is available
        if not index < 2:
            possibleStates.append(self.state_move_block(boardState, index, index - 3, "down"))

        # checks if 0 is on the left side, right move is available
        if not index % 3 == 0:
            possibleStates.append(self.state_move_block(boardState, index, index - 1, "right"))

        # checks if 0 is on the right side, left move is available
        if not index % 3 == 2:
            possibleStates.append(self.state_move_block(boardState, index, index + 1, "left"))

        return possibleStates



class PriorityQueue:

    def  __init__(self):
        self.heap = []

    def push(self,priority, item):
        # FIXME: restored old behaviour to check against old results better
        # FIXED: restored to stable behaviour
        entry = (priority,  item)
        # entry = (priority, item)
        heapq.heappush(self.heap, entry)

    def pop(self):
        (_, item) = heapq.heappop(self.heap)
        #  (_, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0



class solver:
    totalMove = 0
    priotity_queue = PriorityQueue()
    previousState = []
    goalState = [1,2,3,8,0,4,7,6,5]
    state = []

    def start(self):
        initialState = state([2,0,4,1,3,5,7,8,6])
        initialState.print_state(initialState.boardState)
        #searcher = astar(initialState.boardState, self.totalMove, initialState)
        self.priotity_queue.push(0, initialState)

        print()

        found = False
        while not self.priotity_queue.isEmpty() and found == False:

            current = self.priotity_queue.pop()

            for i in current.possibleMoves(current.boardState):
                nextMove = state(i, current)
                # nextMove.print_state(nextMove.boardState)
                #print("state:", nextMove.step, "f:", searcher.f, "h:", searcher.h)

                if nextMove.boardState == self.goalState:
                    path = []
                    # path.append(initialState.boardState)
                    while not nextMove.parent is None:
                        path.append(nextMove)
                        nextMove = nextMove.parent
                    path.reverse()
                    for count, i in enumerate(path, start = 1):
                        print("Step:", i.step, "F:", i.f,  "h:", i.h)
                        print(nextMove.print_state(i.boardState))
                    found = True
                    break;

                if nextMove in self.previousState:
                    index = self.previousState.index(nextMove)
                    #print(nextMove.step, "     1")
                    #print(self.previousState[index].step, "     2")
                    if self.previousState[index].step > nextMove.step:
                        del self.previousState[index]
                        self.previousState.append(nextMove)
                else:
                    self.priotity_queue.push(nextMove.f, nextMove)


            self.previousState.append(current)




if __name__ == '__main__':
    #something = state([6,5,7,3,0,2,8,4,1])
    #something.manhattan([6,5,7,3,0,2,8,4,1])
    #something.manhattan([6,5,7,3,4,2,8,1,0])
    game = solver()
    game.start()