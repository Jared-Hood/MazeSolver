import math

class Node():
    def __init__(self, value):
        self.value = value
        self.next = []
        self.visited = False
        self.distance = math.inf
        self.coord = (0,0)

    def setNext(self, neighbors):
        for n in neighbors:
            if n.value != 1:
                self.next.append(n)

    def neighbors(self):
        return self.next