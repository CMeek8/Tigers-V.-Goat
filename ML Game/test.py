#Test code


class Position:

    def __init__(self,coordx,coordy,state, neighbor):
        self.coordx = coordx
        self.coordy = coordy
        self.state = state
        self.neighbor = neighbor

p = []
play = 1

p.append(Position(2,3,'goat', [1, 2, 3]))


for x in range(len(p[0].neighbor)):
    if p[0].neighbor[x] == play:
        print("FUCKYFUICK")
    else:
            print("NOPE")



'''
if any(p[0].neighbor[i] == play for i in p[0].neighbor):
    print(p[0].neighbor)
else: 
    print("NOPE")
    print(p[0].neighbor[2])

     [3,4],[(3,3),(2,4),(3,5),(4,4)]
              [3,5],[(3,4),(2,5),(3,6),(4,5)]
              [3,6],[(3,5),(2,6)]
              [2,1],[(1,1),(3,1),(2,2)]
              [2,2],[(2,1),(1,2),(2,3),(3,2)]
              [2,3],[(2,2),(1,3),(2,4),(3,3)]
              [2,4],[(2,3),(1,4),(2,5),(3,4)]
              [2,5],[(2,4),(1,5),(2,6),(3,5)]
              [2,6],[(2,5),(1,6),(3,6)]
              [1,1],[(2,1),(1,2)]
              [1,2],[(1,1),(0,0),(1,3),(2,2)]
              [1,3],[(1,2),(0,0),(1,4),(2,3)]
              [1,4],[(1,3),(0,0),(1,5),(2,4)]
              [1,5],[(1,4),(0,0),(1,6),(2,5)]
              [1,6],[(1,5),(2,6)]
              [0,0],[(1,2),(1,3),(1,4),(1,5)]


for x in p[0].neighbor:
    print(x)
''' 