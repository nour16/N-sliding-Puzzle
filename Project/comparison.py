import matplotlib.pyplot as plt  
import algorithms 

time_list_bfs=[]
time_list_ucs=[]
time_list_astar_h1=[]
time_list_astar_h2=[]
space_list_bfs=[]
space_list_ucs=[]
space_list_astar_h1=[]
space_list_astar_h2=[]
time_list_bi=[]
space_list_bi=[]
liste_n=[3,8,15]
liste=[i for i in range(1,10)]

def compar(g):      
    nb_expanded,nb_explored=algorithms.breadth_first_search(g)
    time_list_bfs.append(nb_explored)
    space_list_bfs.append(nb_expanded)
    
    
    nb_expanded,nb_explored=algorithms.uniform_cost_search(g)
    time_list_ucs.append(nb_explored)
    space_list_ucs.append(nb_expanded)
    
    nb_expanded,nb_explored= algorithms.a_star(g,'h1')
    time_list_astar_h1.append(nb_explored)
    space_list_astar_h1.append(nb_expanded)
   
    nb_expanded,nb_explored= algorithms.a_star(g,'h2')
    time_list_astar_h2.append(nb_explored)
    space_list_astar_h2.append(nb_expanded)
    nb_expanded,nb_explored= algorithms.bidirectional_BFS(g)
    time_list_bi.append(nb_explored)
    space_list_bi.append(nb_expanded)


def graph_1():
    
    plt.xlabel('different problems(n=8)')
    plt.ylabel('Computation time (explored_nodes)')
    plt.plot( liste, time_list_bfs, label = "BFS")
    plt.plot(liste, time_list_ucs, label = "UCS")

    plt.title('Computation Time graph')
    plt.legend()
    plt.show()

    plt.xlabel('different problems(n=8)')
    plt.ylabel('Computation time (explored_nodes)')
    plt.plot(liste, time_list_astar_h1, label = "A*_h1",color="red")
    plt.plot(liste, time_list_astar_h2, label = "A*_h2",color="green" )

    plt.title('Computation Time graph')
    plt.legend()
    plt.show()

    plt.xlabel('different problems(n=8)')
    plt.ylabel('Computation time (explored_nodes)')
    plt.plot( liste, time_list_bfs, label = "BFS")
    plt.plot(liste, time_list_bi, label = "Bi_BFS",color="purple" )
    plt.title('Computation Time graph')
    plt.legend()
    plt.show()
    
    plt.xlabel('different problems(n=8)')
    plt.ylabel('Computation time (explored_nodes)')
    plt.plot(liste, time_list_astar_h2, label = "A*_h2",color="green" )
    plt.plot(liste, time_list_bi, label = "Bi_BFS",color="purple" )
    plt.title('Computation Time graph')
    plt.legend()
    plt.show()

    plt.xlabel('different problems(n=8)')
    plt.ylabel('Frontier size(expanded nodes)')
    plt.plot(liste, space_list_bfs, label = "BFS")
    plt.plot(liste, space_list_ucs, label = "UCS")
    plt.title('space complexity graph')
    plt.legend()
    plt.show()

    plt.xlabel('different problems(n=8)')
    plt.ylabel('Frontier size(expanded nodes)')
    plt.plot(liste, space_list_astar_h1, label = "A*_h1",color="red")
    plt.plot(liste, space_list_astar_h2, label = "A*_h2",color="green")
    plt.title('space complexity graph')
    plt.legend()
    plt.show()
    
    plt.xlabel('different problems(n=8)')
    plt.ylabel('Frontier size(expanded nodes)')
    plt.plot(liste, space_list_bfs, label = "BFS")
    plt.plot(liste, space_list_bi, label = "Bi_BFS",color="purple")
    plt.title('space complexity graph')
    plt.legend()
    plt.show()

    plt.xlabel('different problems(n=8)')
    plt.ylabel('Frontier size(expanded nodes)')
    plt.plot(liste, space_list_astar_h2, label = "A*_h2",color="green")
    plt.plot(liste, space_list_bi, label = "Bi_BFS",color="purple")

    plt.title('space complexity graph')
    plt.legend()
    plt.show()
def graph_2():
    
    plt.xlabel('n')
    plt.ylabel('Computation time (explored_nodes)')
    plt.plot( liste_n, time_list_bfs, label = "BFS")
    plt.plot(liste_n, time_list_ucs, label = "UCS")
    plt.plot(liste_n, time_list_astar_h1, label = "A*_h1",color="red")
    plt.plot(liste_n, time_list_astar_h2, label = "A*_h2",color="green" )

    plt.title('Computation Time graph')
    plt.legend()
    plt.show()

    plt.xlabel('n')
    plt.ylabel('Computation time (explored_nodes)')
    plt.plot(liste_n, time_list_astar_h1, label = "A*_h1",color="red")
    plt.plot(liste_n, time_list_astar_h2, label = "A*_h2",color="green" )
    plt.title('Computation Time graph')
    plt.legend()
    plt.show()

    plt.xlabel('n')
    plt.ylabel('Computation time (explored_nodes)')
    plt.plot( liste_n, time_list_bfs, label = "BFS")
    plt.plot(liste_n, time_list_bi, label = "Bi_BFS",color="purple" )
    plt.title('Computation Time graph')
    plt.legend()
    plt.show()
    

    plt.xlabel('n')
    plt.ylabel('Frontier size(expanded nodes)')
    plt.plot(liste_n, space_list_bfs, label = "BFS")
    plt.plot(liste_n, space_list_ucs, label = "UCS")
    plt.plot(liste_n, space_list_astar_h1, label = "A*_h1",color="red")
    plt.plot(liste_n, space_list_astar_h2, label = "A*_h2",color="green")
    plt.title('space complexity graph')
    plt.legend()
    plt.show()

    plt.xlabel('n')
    plt.ylabel('Frontier size(expanded nodes)')
    plt.plot(liste_n, space_list_astar_h1, label = "A*_h1",color="red")
    plt.plot(liste_n, space_list_astar_h2, label = "A*_h2",color="green")
    plt.title('space complexity graph')
    plt.legend()
    plt.show()
    
    plt.xlabel('n')
    plt.ylabel('Frontier size(expanded nodes)')
    plt.plot(liste_n, space_list_bfs, label = "BFS")
    plt.plot(liste_n, space_list_bi, label = "Bi_BFS",color="purple")
    plt.title('space complexity graph')
    plt.legend()
    plt.show()
    
    


    