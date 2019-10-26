import queue as Q

import heapq

import sys

import math

import time

from Puzzle import *

from Heuristics import calculate_total_manhattan_cost, calculate_total_euclidean_cost

# Function that Writes to output.txt
def writeOutput(state, numNodes):
    """Output"""

    #a list that will hold the nodes on the path to goal
    pathToGoal = []

    #fill the list by iterating over the parents of the reached goal state
    while state != None:
        pathToGoal.append(state)
        state = state.parent
    
    #reverse to start by ptinting the root
    pathToGoal.reverse()
    for state in pathToGoal:        
        print(state.action)
        state.display()

    print("Cost of path is " + str(state.cost))
    print("Number of nodes expanded is " + str(numNodes))

#function to check wether a state alread exists in the queue
def InQ(Q, state):
    
    size = Q.qsize()

    flag = False

    #get out all the items in the queue and compare them to the new state, then put back all items in same order
    while(size > 0):
        item = Q.get()
        
        if item == state:
            flag = True
        Q.put(item)
        size -= 1
    return flag



def bfs_search(initial_state):
    """BFS search"""

    frontier = Q.Queue()

    frontier.put(initial_state)

    explored = set()

    while not frontier.empty():
        state = frontier.get()
        explored.add(state.config)

        if test_goal(state):
            return state, len(explored)

        state.expand()
        for child in state.expand():
            if child.config not in explored:
                if not InQ(frontier, child):
                    frontier.put(child)

    return None

#function to check if a state is already in the stack
def InStack(S, state):
    
    flag = False

    #notice here that since we implmented the stack using a heap, we can iterate over all its items as a list
    for item in S:
        if item[1].config == state.config:
            flag = True
            break

    return flag



def dfs_search(initial_state, pushOrder):
    """DFS search"""

    frontier = []
    #implementing the stack using a heap with its pushOrder as cost
    #the intuition here is that the heap always retyrn item with least cost which will always be the last item added to the stack
    #the beenfit we get here is to simplify checking whether an item exists ina  stack or not later on
    heapq.heappush(frontier, (pushOrder, initial_state))
    pushOrder -= 1

    explored = set()

    while frontier:
        state = heapq.heappop(frontier)[1]
        explored.add(state.config)
        
        if test_goal(state):
            return state, len(explored)

        children = state.expand()
        children.reverse()
        for child in children :
            if child.config not in explored:
                if not InStack(frontier, child):
                    heapq.heappush(frontier, (pushOrder, child))
                    pushOrder -= 1

    return None

#function to check whether an item exists in a heap
def InHeap(H, state):
    flag = False

    for item in H:
        if item[1].config == state.config:
            flag = True
            break

    return flag

def A_star_search(initial_state, heuristicMode):
    """A * search"""

    frontier = []
    if heuristicMode == 1:
        heapq.heappush(frontier, (calculate_total_manhattan_cost(initial_state), initial_state))
    elif heuristicMode == 2:
        heapq.heappush(frontier, (calculate_total_euclidean_cost(initial_state), initial_state))
    explored = set()

    while frontier:
        state = heapq.heappop(frontier)[1]
        explored.add(state.config)

        if test_goal(state):
            return state, len(explored)

        for child in state.expand():
            if child.config not in explored:
                if not InHeap(frontier, child):
                    if heuristicMode == 1:
                        heapq.heappush(frontier, (calculate_total_manhattan_cost(child), child))
                    elif heuristicMode == 2:
                        heapq.heappush(frontier, (calculate_total_euclidean_cost(child), child))


    return None


def test_goal(puzzle_state):
    """test the state is the goal state or not"""

    for i, item in enumerate(puzzle_state.config):
        if not item == i:
            return False

    return True


# Main Function that reads in Input and Runs corresponding Algorithm
def main():

    sm = sys.argv[1].lower() # selected method is the 1st argument

    begin_state = sys.argv[2].split(",") # the begin state is the 2nd argument and must be split over the ,

    begin_state = tuple(map(int, begin_state)) # cast the inout into integers and then put them in a tuple

    size = int(math.sqrt(len(begin_state))) #get the size of the state

    hard_state = PuzzleState(begin_state, size) # create the PuzzleState object using the input

    startTime = time.time() #used to caclulate running time after execution

    if sm == "bfs":

        solution, nodes = bfs_search(hard_state)
        writeOutput(solution, nodes)


    elif sm == "dfs":

        solution, nodes = dfs_search(hard_state, 362880)
        writeOutput(solution, nodes)

    elif sm == "astman":

        solution, nodes = A_star_search(hard_state, 1)
        writeOutput(solution, nodes)

    elif sm =="asteuc":

        solution, nodes = A_star_search(hard_state, 2)
        writeOutput(solution, nodes)

    else:

        print("Enter valid command arguments !")
    
    print("Running time is %s seconds"% (time.time() - startTime))


if __name__ == '__main__':

    main()
