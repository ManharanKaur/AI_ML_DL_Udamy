import sys

class Node():
    def __init__(self, state, parent = None, action = None):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier(): #Custom stack for DFS
    def __init__(self):
        self.frontier = [] #represented by a list

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
        # 'any' function returns true if the state is in the frontier

    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if not self.empty():
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        else:
            raise Exception('Stack is empty')
        

class QueueFrontier(StackFrontier): #Custom queue for BFS
    def remove(self):
        if not self.empty():
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        else:
            raise Exception('Queue is empty')

# # Maze problem
class Maze():
    def __init__(self,filename):
        # read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # validate start and goal
        if contents.count("A") != 1:
            raise Exception('Maze must have only one start point')
        if contents.count("B") != 1:
            raise Exception('Maze must have only one goal point')
        
        # determine height and width of maze
        contents  = contents.split() # split line wise into list of strings
        self.height = len(contents)
        self.width = max(len(row) for row in contents)

        # keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i,j) # start point
                        row.append(False) # start point is not a wall
                    elif contents[i][j] == "B":
                        self.goal = (i,j) # goal point
                        row.append(False) # goal point is not a wall
                    elif  contents[i][j] == " ":
                        row.append(False) # space is not a wall
                    else:
                        row.append(True) # wall is encountered
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        self.solution = None  

    def print(self):
        solution = self.solution[1] if self.solution else None
        print()
        for i, row in enumerate(self.walls):
            for j,col in enumerate(row):
                if col:
                    print("█", end="") # wall
                elif (i,j) == self.start:
                    print("A", end="") # start point
                elif (i,j) == self.goal:
                    print("B", end="") # goal point
                elif solution and (i,j) in solution:
                    print("*", end="") # solution path
                else:
                    print(" ", end="") # space
            print()
        print()
                
    def neighbours(self,state):
        row, col = state
        # all possible acdtions
        possible = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        # Ensure acitons are valid
        result = []
        for action, (r, c) in possible:
            try:
                if not self.walls[r][c]:
                    result.append((action, (r, c))) # valid action
            except IndexError:
                continue
        return result
    

    def solve(self):
        # find solution to maze if one exist

        # keep track of no of states explored
        self.num_explored = 0
        # initialize frontier frontier to just starting position
        start = Node(self.start)
        frontier = StackFrontier()  
        frontier.add(start)

        # initialize an empty explored set
        self.explored = set()

        # repeat till solution is found
        while True:
            # if frontier is empty, no solution
            if frontier.empty():
                raise Exception("no solution")
            # get next node from frontier
            node = frontier.remove()
            self.num_explored += 1

            # if node is goal, we have a solution
            if node.state == self.goal:
                actions = []
                cells = []

                # follow parent nodes to find solution
                while node.parent:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            
            # Mark this node as explored
            self.explored.add(node.state)

            # addget neighbors to frontier
            for action, state in self.neighbours(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state, node, action)
                    frontier.add(child)


maze = Maze("/Users/manharankaur/Desktop/Coding/Repository_AI_ML_DL/Artificial Intelligence/maze.txt")
maze.solve()
maze.print()