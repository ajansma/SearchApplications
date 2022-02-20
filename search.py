from graph import * 
from pyamaze import *

# print the solution to the search problem
   
def print_solution(text, search):
    s = ""
    cost = 0

    while not search.path.empty():
        node = search.path.remove()
        s = s + node.vertex + "-"
        cost = cost + node.cost
    print(text + " " + s[:-1] + " with cost " + str(cost) + " after exploring " + str(search.explored_nodes) + " nodes")
    return
    # prints the search path and the cost
        
if __name__ == '__main__':

    m=maze(4,5)
    m.CreateMaze(loadMaze='maze--2022-02-20--17-14-51.csv')
    a = agent(m,filled=True,footprints=True)
    m.tracePath({a:m.path})
    m.run() 

    m1 = Graph()
    m1.set_vertex('T', [['S',1]], [7])
    m1.set_vertex('S', [['R', 2], ['O', 2]], [6])
    m1.set_vertex('R', [['N', 3]], [5])
    m1.set_vertex('Q', [], [4])
    m1.set_vertex('P', [['L', 4]], [6])
    m1.set_vertex('O', [['K', 3],['P', 3]], [5])
    m1.set_vertex('N', [['M', 4]], [4])
    m1.set_vertex('M', [['Q', 5], ['I', 5]], [3])
    m1.set_vertex('L', [['H', 5]], [5])
    m1.set_vertex('K', [['G', 4],['J',4]], [4])
    m1.set_vertex('J', [['K', 7], ['I', 5]], [3])
    m1.set_vertex('I', [['E', 6]], [2])
    m1.set_vertex('E', [['F', 7]], [1])
    m1.set_vertex('F', [['B', 6]], [2])
    m1.set_vertex('G', [['F', 5]], [3])
    m1.set_vertex('H', [['D', 6]], [4])
    m1.set_vertex('D', [['C', 7]], [3])
    m1.set_vertex('C', [['B', 8]], [2])
    m1.set_vertex('B', [['A', 8]], [1])
    m1.set_vertex('A', [], [0])

    print(m1)

    print('******MAZE********')
    print_solution ("A* search f(n)=h(n)      ", m1.astar('T', 'A', greedy_search))
    print_solution ("A* search f(n)=g(n)+h(n) ", m1.astar('T', 'A', astar_search))



    # Graph for uninformed search: BFS, DFS, UCS
    
    g1 = Graph()

    g1.set_vertex('S', [['A',5], ['B',2], ['C',4]])
    g1.set_vertex('A', [['D',9], ['E',4]])
    g1.set_vertex('B', [['G',6]])
    g1.set_vertex('C', [['F',2]])
    g1.set_vertex('D', [['H',5]])
    g1.set_vertex('E', [['G',6]])
    g1.set_vertex('F', [['G',1]])
    g1.set_vertex('G', [])
    g1.set_vertex('H', [])

    print (g1)

    print ("Uninformed search \n")
    print_solution ("Breadth-first search", g1.bfs('S', 'G'))
    print_solution ("Depth-first search  ", g1.dfs('S', 'G'))
    
    print_solution ("A* search f(n)=g(n) ", g1.astar('S', 'G', uniform_cost_search))
        
    # Graph for informed search: UCS, Greedy Best-first search, A* search
   
    g2 = Graph()

    g2.set_vertex('S', [['A',1], ['B',5], ['C',8]], [8])
    g2.set_vertex('A', [['D',3], ['E',7], ['G',9]], [8])
    g2.set_vertex('B', [['G',4]], [4])
    g2.set_vertex('C', [['G',5]], [3])
    g2.set_vertex('D', [], [999])
    g2.set_vertex('E', [], [999])
    g2.set_vertex('G', [], [0])

    print(g2)

    print ("Informed search \n")
    print_solution("A* search default f(n)   ", g2.astar('S', 'G'))
    print_solution("A* search f(n)=g(n)+h(n) ", g2.astar('S', 'G', astar_search))
    print_solution("A* search f(n)=g(n)      ", g2.astar('S', 'G', uniform_cost_search))
    print_solution("A* search f(n)=h(n)      ", g2.astar('S', 'G', greedy_search))

    # Graph in A* Applications
    
    g3 = Graph()

    g3.set_vertex('A', [['B',6], ['F',3], ['G',5]], [8])
    g3.set_vertex('B', [['A',6], ['C',3], ['D',2]], [8])
    g3.set_vertex('C', [['B',3], ['D',1], ['E',5]], [5])
    g3.set_vertex('D', [['B',2], ['C',1], ['E',8]], [7])
    g3.set_vertex('E', [['C',5], ['D',8], ['I',5], ['J',5]], [3])
    g3.set_vertex('F', [['A',3], ['G',1], ['H',7]], [6])
    g3.set_vertex('G', [['A',5], ['F',1], ['I',3]], [5])
    g3.set_vertex('H', [['F',7], ['I',2]], [3])
    g3.set_vertex('I', [['E',5], ['G',3], ['H',2], ['J',3]], [1])
    g3.set_vertex('J', [['E',5], ['I',3]], [0])

    print (g3) 

    print_solution ("A* search f(n)=g(n)      ", g3.astar('A', 'J', uniform_cost_search))
    print_solution ("A* search f(n)=h(n)      ", g3.astar('A', 'J', greedy_search))
    print_solution ("A* search f(n)=g(n)+h(n) ", g3.astar('A', 'J', astar_search))
    