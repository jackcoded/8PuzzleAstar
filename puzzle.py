import heapq
from random import shuffle
import time
import random


class state:
    goalState = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    boardState = []
    previousState = []

    # initiate the board with given numbers
    def __init__(self, numbers):
        self.boardState = numbers

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

    def calculateHeuristic(self, state):
        wrongtile = 0
        for count, i in enumerate(state, start=0):
            if i == 0:
                continue
            elif i != self.goalState[count]:
                wrongtile += 1;
        print(wrongtile)
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

        # delete duplicate states from previousStates
        for count, i in enumerate(possibleStates, start=0):
            for x in self.previousState:
                if i == x:
                    print(count, "hello")
                    del possibleStates[count]
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


class solver:
    totalMove = 1
    queue = []

    def start(self):
        stuff = state([2, 8, 3, 1, 6, 4, 7, 0, 5])
        stuff.print_state(stuff.boardState)
        print()
        while stuff.boardState != stuff.goalState:
            for i in stuff.possibleMoves(stuff.boardState):
                stuff2 = astar(i, self.totalMove, stuff)
                heapq.heappush(self.queue, (stuff2.f, i))
                stuff.previousState.append(i)
            # while queue:
            #   next_item = heapq.heappop(queue)
            #  stuff.print_state(next_item)
            tuple = heapq.heappop(self.queue)
            stuff.boardState = tuple[1]
            print()
            stuff.print_state(stuff.boardState)
            self.totalMove += 1
        print("Solved in", self.totalMove)

game = solver()
game.start()
