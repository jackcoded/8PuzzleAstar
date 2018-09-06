import heapq
from random import shuffle
import time
import random


class state:
    boardState = []
    parent = []

    # initiate the board with given numbers
    def __init__(self, numbers, prev_state = None):
        self.boardState = numbers
        self.parent = prev_state

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

class astar:
    h = 0
    g = 0
    f = 0

    def __init__(self, board, totalMove, state):
        # initialise total move
        self.g = totalMove
        # gets heuristic value
        self.h = state.calculateHeuristic(board)
        # f = g + h
        self.f = self.g + self.h

\
class solver:
    totalMove = 0
    queue = []
    previousState = set()
    goalState = [1,2,3,8,0,4,7,6,5]


    def start(self):
        initialState = state([1,5,7,4,2,6,3,8,0])
        initialState.print_state(initialState.boardState)
        searcher = astar(initialState.boardState, self.totalMove, initialState)
        heapq.heappush(self.queue, (searcher.f, self.totalMove , initialState))
        print()

        while self.queue.__len__() > 0:
            tuple = heapq.heappop(self.queue)
            current = tuple[2]
            self.previousState.add(current)
            if(current.boardState == self.goalState):
                break;

            if self.totalMove > tuple[1]:
                self.totalMove = tuple[1]+1
                continue

            #print("state:", self.totalMove, "f:", stuff2.f, "h:", stuff2.h)

            for i in current.possibleMoves(current.boardState):
                nextMove = state(i, current)
                searcher = astar(nextMove.boardState, self.totalMove, nextMove)
                if nextMove in self.previousState:
                    continue
                else:
                    heapq.heappush(self.queue, (searcher.f, self.totalMove ,nextMove))

        print("Solved in", self.totalMove, "Moves")

game = solver()
game.start()
