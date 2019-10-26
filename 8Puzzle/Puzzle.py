## The Class that Represents the Puzzle

class PuzzleState(object):

    """PuzzleState class contains its initializer and children creation and all helper functions"""

    def __init__(self, config, n, parent=None, action="Initial", cost=0):

        if n*n != len(config) or n < 2: #check that user input is correct

            raise Exception("the length of config is not correct!")

        self.n = n 

        self.cost = cost 

        self.parent = parent

        self.action = action #action that resulted in state's creation

        self.dimension = n

        self.config = config #tuple that holds the arrangement of the tiles inside the puzzle

        for i, item in enumerate(self.config):

            if item == 0:

                self.blank_row = i // self.n #row index of 0

                self.blank_col = i % self.n #col index of 0

                break

    def __lt__(self, other): #function to compare the puzzle states , it is as if our class implments the interface Comparable 

        return self.cost < other.cost

    def display(self): #function that displays the puzzle tuple

        for i in range(self.n):

            line = [] # a list for each row of the puzzle

            offset = i * self.n # row index

            for j in range(self.n): # col index

                line.append(self.config[offset + j])

            print(line)

    def move_left(self): #get the left child 

        if self.blank_col == 0: #impossible to move left

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col #get the tuple index of the blank tile 

            target = blank_index - 1 #calculate target index of the blank tile

            new_config = list(self.config) #get a copy of the parent state tuple

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index] #swap blank tile with its neighbor 

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self): #get the right child 

        if self.blank_col == self.n - 1: #impossible to move right

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col #get the tuple index of the blank tile

            target = blank_index + 1 #calculate target index of the blank tile

            new_config = list(self.config) #get a copy of the parent state tuple

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index] #swap blank tile with its neighbor

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self): #get the above child 

        if self.blank_row == 0: #impossible to move up

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col #get the tuple index of the blank tile

            target = blank_index - self.n #calculate target index of the blank tile

            new_config = list(self.config) #get a copy of the parent state tuple

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index] #swap blank tile with its neighbor

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self): #get the below child

        if self.blank_row == self.n - 1: #impossible to move down

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col #get the tuple index of the blank tile

            target = blank_index + self.n #calculate target index of the blank tile

            new_config = list(self.config) #get a copy of the parent state tuple

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index] #swap blank tile with its neighbor

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):
        """expand the node"""

        # add child nodes in order of UDLR

        children = []
        
        up_child = self.move_up()

        if up_child is not None:

            children.append(up_child)

        down_child = self.move_down()
        
        if down_child is not None:

            children.append(down_child)

        left_child = self.move_left()

        if left_child is not None:

            children.append(left_child)

        right_child = self.move_right()

        if right_child is not None:

            children.append(right_child)

        return children