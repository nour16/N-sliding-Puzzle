import heapq

class Node:
    def __init__(self,state,path_cost=0,total_cost=0,parent=None):
        self.state= state
        self.path_cost=path_cost   ## g function
        self.total_cost=total_cost  ##f function = g+h
        self.parent=parent

    def __lt__(self,nxt):
        return self.total_cost <  nxt.total_cost

    def print_board(self):
        state=self.state
        for row in state:
            for col in row:
                print ('|',end=" ")
                print(col,end=" ")
            print('|')

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def empty(self):
        return len(self.heap) == 0

    def put(self, node):
        heapq.heappush(self.heap, node)

    def get(self):
        return heapq.heappop(self.heap)

