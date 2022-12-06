NODES=6
MATRIX=[(0,1,3),(0,2,2),(1,3,1),(1,4,4),(3,2,2),(3,4,3),(2,5,1),(4,5,2),
(1,0,3),(2,0,2),(3,1,1),(4,1,4),(2,3,2),(4,3,3),(5,2,1),(5,4,2)]
#[(Source,Destination,Weight)]
VISITED=[0]
UNVISITED=[1,2,3,4,5]
MX=9999
Distance=[0,MX,MX,MX,MX,MX]
i=0
while(len(VISITED)!=NODES):

    queue=[]
    for each in MATRIX:
        source=each[0]
        dest= each[1]
        dist=each[2]
        if(source==i and dest not in VISITED):
            if(Distance[source]+dist<Distance[dest]):
                Distance[dest]=Distance[source]+dist
    i=min(UNVISITED,key=lambda x:Distance[x])
    VISITED.append(i)
    UNVISITED.pop(UNVISITED.index(i))
for each in range(len(Distance)):
    print("0->",each,"=",Distance[each])

