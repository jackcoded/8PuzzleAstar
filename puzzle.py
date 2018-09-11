import heapq
from random import shuffle
import time
import random


class state:
    boardState = []
    parent = []
    step = 0
    def __lt__(self, other):
        return state

    def __eq__(self, other):
        return self.boardState == other.boardState

    # initiate the board with given numbers
    def __init__(self, numbers, prev_state = None):
        self.boardState = numbers
        self.parent = prev_state
        self.step = 0
        if self.parent:
            self.step = self.parent.step + 1

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
        initialState = state([0,6,5,4,1,7,3,2,8])
        initialState.print_state(initialState.boardState)
        #searcher = astar(initialState.boardState, self.totalMove, initialState)
        self.priotity_queue.push(0, initialState)

        print()

        while not self.priotity_queue.isEmpty():

            current = self.priotity_queue.pop()
            if current.boardState == self.goalState:
                path = []
               # path.append(initialState.boardState)
                while not current.parent is None:
                    path.append(current.boardState)
                    current = current.parent
                path.reverse()
                for count, i in enumerate(path, start = 1):
                    print("Step:",count)
                    print(current.print_state(i))

                break;

            self.previousState.append(current)

            for i in current.possibleMoves(current.boardState):
                    nextMove = state(i, current)
                    searcher = astar(nextMove.boardState, nextMove.step, nextMove)
                   # nextMove.print_state(nextMove.boardState)
                    #print("state:", nextMove.step, "f:", searcher.f, "h:", searcher.h)

                    if nextMove in self.previousState:
                        index = self.previousState.index(nextMove)
                        if nextMove.step < self.previousState[index].step:
                            print("shit")
                            del self.previousState[index]
                            self.previousState.append(nextMove)
                        continue
                    else:
                        self.priotity_queue.push(searcher.f, nextMove)








game = solver()
game.start()
