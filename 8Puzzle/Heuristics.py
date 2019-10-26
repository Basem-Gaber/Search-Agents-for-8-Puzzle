import math 

def calculate_total_manhattan_cost(state):
    """calculate the total cost of a state using manhattan heuristic"""

    heuristic = state_manhattan(state)

    return state.cost + heuristic


def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a single tile"""

    goalRow = value // n #row index at goal

    goalCol = value % n #col index at goal

    currentRow = idx // n #current row index

    currentCol = idx % n #current col index

    dist = abs(goalRow - currentRow) + abs(goalCol - currentCol) #manhattan
    
    return dist


def state_manhattan(state):
    """calculate the manhattan distance of a state"""

    total = 0

    for i, item in enumerate(state.config): # loop over all the tiles and calculate their costs
        if item == 0:
            continue
        total += calculate_manhattan_dist(i, item, state.n)

    return total


def calculate_total_euclidean_cost(state):
    """calculate the total cost of a state using euclidean heuristic"""
    
    heuristic = state_euclidean(state)

    return state.cost + heuristic


def calculate_euclidean_dist(idx, value, n):
    """calculate the euclidean distance of a single tile"""

    goalRow = value // n #row index at goal

    goalCol = value % n #col index at goal

    currentRow = idx // n #current row index

    currentCol = idx % n #current col index

    dist = math.sqrt((goalRow - currentRow)**2 + (goalCol - currentCol)**2) #euclidean
    
    return dist


def state_euclidean(state):
    """calculate the euclidean distance of a state"""

    total = 0

    for i, item in enumerate(state.config): #loop over all the tiles and caclulate their costs
        if item == 0:
            continue
        total += calculate_euclidean_dist(i, item, state.n)

    return total
