from graph import * 
# pyamaze class to help with visualization of the maze
# license/source in pyamaze
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
        
# main program
if __name__ == '__main__':

    # creat the maze graph (T is start point in lower right corner)
    # A is the goal in the upper left corner
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
    m1.set_vertex('I', [['E', 6]], [1])
    m1.set_vertex('E', [['F', 7]], [1])
    m1.set_vertex('F', [['B', 6]], [2])
    m1.set_vertex('G', [['F', 5]], [3])
    m1.set_vertex('H', [['D', 6]], [4])
    m1.set_vertex('D', [['C', 7]], [3])
    m1.set_vertex('C', [['B', 8]], [2])
    m1.set_vertex('B', [['A', 8]], [1])
    m1.set_vertex('A', [], [0])

    print(m1)

    # print solution
    print('******MAZE********')
    print_solution ("A* search f(n)=h(n)      ", m1.astar('T', 'A', greedy_search))
    print_solution ("A* search f(n)=g(n)+h(n) ", m1.astar('T', 'A', astar_search))

    # draw solution
    m=maze(4,5)
    m.CreateMaze(loadMaze='maze--2022-02-20--17-14-51.csv')
    a = agent(m,filled=True,footprints=True)
    m.tracePath({a:m.path})
    m.run() 