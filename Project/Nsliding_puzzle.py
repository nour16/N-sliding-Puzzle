import numpy as np
import random
from copy import deepcopy
import algorithms 
from Node import *
from comparison import *

class Game:
    def __init__(self,n,init_tiles=[]):
        """Initialze the n-puzzle problem, with n tiles.
            We either get the start configuration from a text file or we generate it randomly 
        """
        self.n=n
        self.grid_size = int(np.sqrt(self.n+1))
        self.tiles=list(range(1,self.n+1))+[0]   ##we add 0 to the tiles , that represent the empty space
        self.goal=Node(np.array(self.tiles).reshape(self.grid_size,self.grid_size))
        if len(init_tiles)!=0:  ##if it is not generated randomly
            self.initial=Node(np.array(init_tiles).reshape(self.grid_size,self.grid_size))

    def random_init_state(self,difficulty=20):
        """Generate the initial state randomly """
        #Takes a random series of moves backwards from the goal state 
        # so that the initial state of the puzzle is guaranteed to be solvable
        current=deepcopy(self.goal)
        for i in range (difficulty): 
            legal_successors=self.results(current)
            current=random.choice(legal_successors) 
        self.initial =current

    def goal_test(self,state):
        """Check if the state in the paramater is the goal state"""
        return np.array_equal(state, self.goal.state)

    def Actions(self,state):
        """generates the list of possible moves in the state"""
        actions=[]
        ## we get the position of 0 (which is the empty tile) in the state
        empty_row=np.where(state==0)[0][0]
        empty_col=np.where(state==0)[1][0]
        if empty_col>0:   
            actions.append('L')  # we can move left
        if empty_col<self.grid_size-1:   
            actions.append('R')  #we can move right
        if empty_row>0:
            actions.append('U')   #we can move up
        if empty_row<self.grid_size-1:
            actions.append('D')    #we can move down 
        return actions

   
    def results(self,node):
        """expand the given node by applying state transitions(actions) and returns its children"""
        results = []     
        empty_row=np.where(node.state==0)[0][0]  ## we get the position of 0 (which is the empty tile) in the state
        empty_col=np.where(node.state==0)[1][0]
        actions=self.Actions(node.state)
        for action in actions: #we generate the result for each action 
            temp_state = deepcopy(node.state)
            if action=='U':
                temp_state[empty_row][empty_col] = temp_state[empty_row-1][empty_col]
                temp_state[empty_row-1][empty_col] = 0
            elif action=='D':
                temp_state[empty_row][empty_col] = temp_state[empty_row+1][empty_col]
                temp_state[empty_row+1][empty_col] = 0
            elif action=='L':
                temp_state[empty_row][empty_col] = temp_state[empty_row][empty_col-1]
                temp_state[empty_row][empty_col-1] = 0
            elif action=='R':
                temp_state[empty_row][empty_col] = temp_state[empty_row][empty_col+1]
                temp_state[empty_row][empty_col+1] = 0
            results.append(Node(temp_state))
        return results

    def step_cost(self):
        """all steps cost are 1 """
        return 1

    def contains(self,state,list):
        """Check if a list contains a state or not """
        for s in list:
            if np.array_equal(state, s):
                return True
        return False
    

def read_from_text_file():
    f_name="start_config.txt"
    file = open(f_name, "r")
    n =int(file.readline())
    init_tiles=[]
    for line in file:
        for t in line.split(" "):
            init_tiles.append(int(t))
    file.close()
    g=Game(n,init_tiles)
    print("**************************************************")
    print("Start configuration read from the file 'text_file': ")
    print("n= "+str(n))
    print("Initial State of the game:")
    Node.print_board(g.initial)
    return g

def random_game(n=8,difficulty=20):
    g=Game(n)
    g.random_init_state(difficulty)
    print("**************************************************")
    print("Start configuration read from the file 'text_file':")
    print("n= "+str(n))
    print("Initial State of the game:")
    Node.print_board(g.initial)
    return g

def main():  
    start_choice = input("Enter the way to generate the start_configuration: 'text_file' or 'random'\n")
    if start_choice=='text_file': ##Reading a start configuration from a file
       g= read_from_text_file()    
    else:   ## Otherwise it is generated randomly
        g= random_game()
        
    algo=''
    while algo!="UCS" and algo!="BFS" and algo!="A*_h1" and algo!="A*_h2" and algo!="Bi_BFS":
        algo= input("With which search algorithm you want to solve the problem?\nWrite 'BFS' or 'UCS' or 'A*_h1' or 'A*_h2' or 'Bi_BFS'\n")
    if algo=="UCS":  
        algorithms.uniform_cost_search(g)
    elif algo=="BFS":
        algorithms.breadth_first_search(g)
    elif algo=="A*_h1":
        algorithms.a_star(g,'h1')
    elif algo=="A*_h2":
        algorithms.a_star(g,'h2') 
    elif algo=="Bi_BFS":
        algorithms.bidirectional_BFS(g)


    ##used for comparison   
    """ 
    for i in range(1,10):
        g=random_game()
        compar(g)
    graph_1()
    for i in [3,8,15]:
        g=random_game(i)
        compar(g)
    graph_2()
    """

if __name__ == "__main__":
    main()