import sys
import numpy as np 
from Node import *
from queue import Queue
from Nsliding_puzzle import *

def heuristic(game,state,chosen_h):
    if chosen_h=='h1':
        'number of displaced tiles'
        nbPieces=0
        for i in range(game.grid_size):
            for j in range(game.grid_size):
                if state[i][j]!=0 and state[i][j]!=game.goal.state[i][j]: #We don't take in consideration the empty space(0)
                    nbPieces+=1
        return nbPieces

    else:   ##h2
        'sum of manhattan distances'
        sumMunh=0
        for i in range(game.grid_size):
            for j in range(game.grid_size):
                tile=state[i][j]
                if tile!=0:   #We don't take in consideration the empty space(0)
                    ([x],[y]) = np.where(game.goal.state==tile)
                    sumMunh+= abs(i-x)+abs(j-y)
        return sumMunh
    
def breadth_first_search(game):
    current=game.initial
    nb_expanded=0
    nb_explored=0
    if (game.goal_test(current.state)==True):  
        print("**************************************************")
        print("Solution with Breadth First Search (BFS):")
        Node.print_board(current)
        print("SUCCESS! Goal_state Found!")
        return nb_expanded,nb_explored
    frontier= Queue() 
    frontier.put(current) 
    nb_expanded+=1
    explored=[]
    while(not frontier.empty()):
        print("size of the frontier: "+str(frontier.qsize()))
        print("size of the explered set: "+str(len(explored)))
        current=frontier.get()
        explored.append(current.state)  ##add current to explored
        nb_explored+=1
        successers=game.results(current)
        for suc in successers:
            if not game.contains(suc.state,explored):
                suc.parent=current
                if (game.goal_test(suc.state)==True):  
                    print("size of the frontier: "+str(frontier.qsize()))
                    print("size of the explered set: "+str(len(explored)))  
                    print("**************************************************")
                    print("Solution with Breadth First Search (BFS):")
                    print()
                    print_path(suc)
                    Node.print_board(suc)
                    print("SUCCESS! Goal_state Found!")
                    return (nb_expanded,nb_explored)
                frontier.put(suc)  ##add suc to frontier
                nb_expanded+=1     
    if frontier.empty():
        print("**************************************************")
        print("Nosolution with BFS")
        return
                
def uniform_cost_search(game):
    frontier= PriorityQueue()  
    nb_expanded=0
    nb_explored=0
    current=game.initial
    frontier.put(current)
    nb_expanded+=1 
    explored=[]
    while(not frontier.empty()):
        print("size of the frontier: "+str(len(frontier.heap)))
        print("size of the explered set: "+str(len(explored)))  
        current=frontier.get()
        path_cost=current.path_cost  ##keeps track of the path_cost 
        if (game.goal_test(current.state)==True):  
            print("size of the frontier: "+str(len(frontier.heap)))
            print("size of the explered set: "+str(len(explored)))  
            print("**************************************************")
            print("Solution with Uniform Cost Search:")
            print()
            print_path(current)
            Node.print_board(current)
            print("SUCCESS! Goal_state Found!")
            return (nb_expanded, nb_explored)
        explored.append(current.state)
        nb_explored+=1
        successers=game.results(current)
        for suc in successers:
            if not game.contains(suc.state,explored):
                suc.parent=current
                suc.path_cost=path_cost+game.step_cost() 
                suc.total_cost=suc.path_cost
                frontier.put(suc)
                nb_expanded+=1
    if frontier.empty():
        print("**************************************************")
        print("Nosolution with UCS")
        return


def a_star(game,h):
    frontier= PriorityQueue()  ##initialize a priorityQueue
    nb_expanded=0
    nb_explored=0
    current=game.initial
    current.total_cost = current.path_cost+heuristic(game,current.state,h)
    frontier.put(current) 
    nb_expanded+=1
    explored=[]
    while(not frontier.empty()):
        print("size of the frontier: "+str(len(frontier.heap)))
        print("size of the explered set: "+str(len(explored)))
        current=frontier.get()
        path_cost=current.path_cost
        if (game.goal_test(current.state)==True): 
            print("size of the frontier: "+str(len(frontier.heap)))
            print("size of the explered set: "+str(len(explored)))
            print("**************************************************")
            print('Solution with Algo A* '+h+' :') 
            print()
            print_path(current)
            Node.print_board(current)
            print("SUCCESS! Goal_state Found!")
            return (nb_expanded, nb_explored ) ##we return the nb of expanded nodes so we can use it to compare space complexity
        explored.append(current.state)
        nb_explored+=1
        successers=game.results(current)
        for suc in successers:
            if not game.contains(suc.state,explored):
                suc.parent=current
                suc.path_cost=path_cost+game.step_cost()
                suc.total_cost= suc.path_cost+heuristic(game,suc.state,h) #keep track of the cost
                frontier.put(suc)
                nb_expanded+=1
    if frontier.empty():
        print("**************************************************")
        print("Nosolution with A*") 
        return

def bidirectional_BFS(game):
    frontier_start= Queue()
    frontier_end= Queue()
    nb_expanded=0
    nb_explored=0
    frontier_start.put(game.initial) 
    frontier_end.put(game.goal) 
    nb_expanded+=2
    if (game.goal_test(game.initial.state)==True):  
        print("**************************************************")
        print("Solution with Bidirectiona_BFS:")
        Node.print_board(game.initial)
        print("SUCCESS! Goal_state Found!")
        return (nb_expanded,nb_explored)
    explored_start=[]
    explored_end=[]
    while(not frontier_start.empty() or not frontier_end.empty()):
        print("size of the frontier_start: "+str(frontier_start.qsize()))
        print("size of the explered set start: "+str(len(explored_start)))  
        print("size of the frontier_end: "+str(frontier_end.qsize()))
        print("size of the explered set end: "+str(len(explored_end)))  
        current_start=frontier_start.get()
        current_end=frontier_end.get()
        same_val_s,same_val_e=lists_have_same_value(frontier_start,frontier_end)
        if (same_val_s): 
            print("**************************************************")
            print('Solution with Algo Bidirectional_BFS* :') 
            print()
            print("-----------------Intersection state:")
            Node.print_board(same_val_s)
            print("-----------------Path from start:")
            print_path(same_val_s)
            Node.print_board(same_val_s)
            print("------------------Path from end:")
            print_path(same_val_e)
            Node.print_board(same_val_e)
            return (nb_expanded, nb_explored ) ##we return the nb of expanded nodes so we can use it to compare space complexity
        explored_start.append(current_start.state)
        explored_end.append(current_end.state)
        nb_explored+=2
        successers_start=game.results(current_start)
        for suc in successers_start:
            if not game.contains(suc.state,explored_start):
                suc.parent=current_start
                frontier_start.put(suc)
                nb_expanded+=1
        successers_end=game.results(current_end)
        for suc in successers_end:
            if not game.contains(suc.state,explored_end):
                suc.parent=current_end
                frontier_end.put(suc)
                nb_expanded+=1
    print("**************************************************")
    print("Nosolution with Bi_BFS") 
    return (nb_expanded,nb_explored)

def lists_have_same_value(front1,front2):
    for node1 in front1.queue:
        for node2 in front2.queue:
            if np.array_equal(node1.state,node2.state):
                return node1,node2 ##which have the same state value but 
                                    ##one found from start and the other from goal
    return None,None

def print_path(node):
    """print the path solution found by an algorithm"""
    leaf=node
    path=[]
    while leaf:
        path.append(leaf)
        if leaf.parent:
            leaf=leaf.parent
        else:
            leaf=None   
    path= list(reversed(path))
    
    def find_direction(current_state, next_state):
        current_empty_row=np.where(current_state==0)[0][0]
        current__empty_col=np.where(current_state==0)[1][0]      
        next_empty_row=np.where(next_state==0)[0][0]
        next__empty_col=np.where(next_state==0)[1][0]
        if next__empty_col == current__empty_col and next_empty_row > current_empty_row:
            print('Moved Down  >>>>>')
        if next__empty_col == current__empty_col and next_empty_row  < current_empty_row:
            print('Moved Up >>>>>')
        if next__empty_col > current__empty_col and next_empty_row  == current_empty_row:
            print('Moved Right >>>>>')
        if next__empty_col < current__empty_col and next_empty_row  == current_empty_row:
            print('Moved Left >>>>')

    for current, next in  zip(path, path[1:]):   
        print("Current_state:")
        Node.print_board(current)
        print()
        find_direction(current.state, next.state)

    



   
      


