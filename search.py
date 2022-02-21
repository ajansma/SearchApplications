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

    # print Maze
    print('Goal: A  Start: T\n')
    print('A  | E    I    M     Q\n')
    print('B    F  | J  | N     R')
    print('              --')
    print('C  | G    K    O     S\n')
    print('D    H    L    P  |  T')

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

    # Create a graph that mimics a map of metro stops
    g1 = Graph()

    # Starting point is Gran Via, Goal is Nuevos Ministerios
    g1.set_vertex('Gran Via', [['Tribunal',2], ['Chueca',2], ['Sol',2]], [10])
    g1.set_vertex('Tribunal', [['Alonso Martinez',3], ['Bilbao', 2]], [11])
    g1.set_vertex('Alonso Martinez', [['Gregorio Maranon',3], ['Ruben Dario',2]], [8])
    g1.set_vertex('Gregorio Maranon', [['Nuevos Ministerios',3], ['Alonso Cano',2]], [3])
    g1.set_vertex('Bilbao', [['Iglesia',3]], [8])
    g1.set_vertex('Iglesia', [['Rios Rosas',2]], [6])
    g1.set_vertex('Rios Rosas', [['Metro Cuatro Caminos',2]], [4])
    g1.set_vertex('Metro Cuatro Caminos', [['Nuevos Ministerios',2], ['Canal',3]], [3])
    g1.set_vertex('Chueca', [['Alonso Martinez',2]], [14])
    g1.set_vertex('Ruben Dario', [['Nunez De Balboa',2]], [10])
    g1.set_vertex('Nunez De Balboa', [['Diego De Leon',2]], [8])
    g1.set_vertex('Diego De Leon', [['Avenida de America',3]], [6])
    g1.set_vertex('Avenida de America', [['Republica Argentina',2]], [3])
    g1.set_vertex('Republica Argentina', [['Nuevos Ministerios',2]], [3])
    g1.set_vertex('Sol', [['Sevilla',3], ['Callao',2]], [10])
    g1.set_vertex('Sevilla', [], [999])
    g1.set_vertex('Callao', [], [999])
    g1.set_vertex('Alonso Cano', [], [999])
    g1.set_vertex('Canal', [], [999])
    g1.set_vertex('Nuevos Ministerios', [], [0])

    print (g1)
    
    print('******Map******')
    print_solution ("A* search f(n)=h(n)      ", g1.astar('Gran Via', 'Nuevos Ministerios', greedy_search))
    print_solution ("A* search f(n)=g(n)+h(n) ", g1.astar('Gran Via', 'Nuevos Ministerios', astar_search))