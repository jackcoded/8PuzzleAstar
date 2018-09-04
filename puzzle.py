from heapq import heappush, heappop
from random import shuffle
import time
import random



class state:
    goalState = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    boardState = []
    previousState = []
    heuristic = 0
    distance = 0

    #initiate the board with given numbers
    def __init__(self, numbers):
        self.boardState = numbers

    #prints the board
    def print_state(self, state):
        for count, i in enumerate(state, start=1):
            print(i, end=" ")
            if count % 3 == 0:
                print()

    #moves block by switching array element
    def state_move_block(self, boardState, source, dest, move):
        newState = list(boardState)
        newState[source], newState[dest] = newState[dest], newState[source]
        self.print_state(newState)
        print(newState[source], "-", move)

        return newState
    def calculateHeuristic(self, state):
        wrongtile = 0
        for count, i in enumerate(state, start =0):
            if i == 0:
                continue
            elif i != self.goalState[count]:
                wrongtile += 1;
        print(wrongtile)
        return wrongtile

    #finds the possible moves at given location on the board
    def possibleMoves(self, boardState):
        index = boardState.index(0)
        possibleStates = list([])
        #checks if 0 is on the top, up move is available
        if not index >= 6:
            possibleStates.append(self.state_move_block(boardState, index, index + 3, "up"))

        #checks if 0 is on the bottom,down move is available
        if not index <= 6:
            possibleStates.append(self.state_move_block(boardState, index, index - 3, "down"))

        #checks if 0 is on the left side, right move is available
        if not index % 3 == 0:
            possibleStates.append(self.state_move_block(boardState, index, index - 1, "right"))

        #checks if 0 is on the right side, left move is available
        if not index % 3 == 2:
            possibleStates.append(self.state_move_block(boardState, index, index + 1, "left"))

        #delete duplicate states from previousStates
        for count, i in enumerate(possibleStates, start = 0):
                for x in self.previousState:
                    if i == x:
                        del possibleStates[count]

        return possibleStates


numbers = list(range(0, 9))
shuffle(numbers)
stuff = state(numbers)
stuff.print_state(stuff.boardState)
print()
stuff.possibleMoves(stuff.boardState)


