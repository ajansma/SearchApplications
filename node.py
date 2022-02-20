# Node objects store data used when exploring nodes
class Node:
    def __init__(self, vertex, parent=None, cost = 0, heuristic=0):
        self._vertex = vertex
        self._parent = parent
        self._cost = cost
        self._heuristic = heuristic


    @property
    def vertex(self):
        return self._vertex
    
    @property
    def parent(self):
        return self._parent
    
    @property
    def cost(self):
        return self._cost
    
    @property
    def heuristic(self):
        return self._heuristic
    

    def __str__(self):
        return "'" + self._vertex + "'" if self._parent == None else "'" + self._vertex + "','" + self._parent + "',cost=" + str(self._cost) + ",heuristic=" + str(self._heuristic)