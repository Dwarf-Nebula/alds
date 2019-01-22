class Vertex:
	def __init__(self, data):
		self.data = data

	def __repr__(self):         # voor afdrukken
		return str(self.data)

	def __lt__(self, other):    # voor sorteren
		return self.data < other.data

def vertices(G):
	return sorted(G)

def edges(G):
	return [(u,v) for u in vertices(G) for v in G[u]]

class myqueue(list):
	def __init__(self,a=[]):
		list.__init__(self,a)

	def dequeue(self):
		return self.pop(0)

	def enqueue(self,x):
		self.append(x)

	def empty(self):
		return a.empty()

import math
INFINITY = math.inf # float("inf")

def clear(G): 
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v,e)

def BFS(G,s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s) 
    while q:
        u = q.dequeue() 
        for v in G[u]:
            if v.distance == INFINITY: # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)

v = [Vertex(i) for i in range(8)]    

G = {v[0]:[v[4],v[5]], 
     v[1]:[v[4],v[5],v[6]], 
     v[2]:[v[4],v[5],v[6]], 
     v[3]:[v[7]],
     v[4]:[v[0],v[1],v[2],v[5]],
	 v[5]:[v[0],v[1],v[2],v[4]],
	 v[6]:[v[1],v[2]],
	 v[7]:[v[3]]}
				
				
#5.1
def is_connected(G):
	V = vertices (G)
	BFS(G, V[0])
	V = vertices (G)
	for v in V:
		if v.distance == INFINITY:
			return False
	return True

print(is_connected(G))

#5.2
def no_cycles(G):
	q = myqueue()
	V = vertices(G)
	q.enqueue(V[0])
	visited = []
	while q:
		n = q.dequeue()
		if n in visited:
			return False
		visited.append(n)
		for v in G[n]:
			q.enqueue(v)
	return True
	
print(no_cycles(G))

#5.3

v = [Vertex(i) for i in range(8)]    

G = {v[0]:[v[1],v[3]], 
     v[1]:[v[0],v[2]],
     v[2]:[v[1],v[3],v[4]], 
     v[3]:[v[0],v[2]],
     v[4]:[v[2],v[5],v[6]],
	 v[5]:[v[4],v[6]],
	 v[6]:[v[4],v[5],v[7]],
	 v[7]:[v[6]]}

def get_bridges(G):
	bridges = []
	for v in G:
		for e in G[v]:
			G[v].remove(e)
			G[e].remove(v)
			BFS(G, e)
			if v.distance == INFINITY:
				bridges.append((v, e))
			G[v].append(e)
			G[e].append(v)
	return bridges

print(get_bridges(G))

#5.4

v = [Vertex(i) for i in range(3)]

G = {v[0]:[v[1]], 
     v[1]:[v[2]],
     v[2]:[v[0]]}

falseV = [Vertex(i) for i in range(3)]

falseG = {v[0]:[v[2]], 
     v[1]:[v[2]],
     v[2]:[v[0]]}

def is_strongly_connected(G):
	if is_connected(G):
		newG = {}
		for v in G:
			for e in G[v]:
				if e in newG:
					newG[e].append(v)
				else:
					newG[e] = [v]
			return is_connected(newG)
	return False

print(is_strongly_connected(G))
print(is_strongly_connected(falseG))

#5.5

v = [Vertex(i) for i in range(8)]    

G = {v[0]:[v[1],v[2]], 
     v[1]:[v[0],v[3]],
     v[2]:[v[0],v[3]], 
     v[3]:[v[1],v[2],v[4],v[6]],
     v[4]:[v[3],v[5],v[6],v[7]],
	 v[5]:[v[4],v[6]],
	 v[6]:[v[3],v[4],v[5],v[7]],
	 v[7]:[v[4],v[6]]}

def is_Euler_graph(G):
	for v in G:
		if len(G[v]) % 2:
			return False
	return True

print (is_Euler_graph(G))

def get_Euler_circuit(G,s):
	path = [s]
	current = s
	while edges(G):
		for t in G[current]:
			if (current, t) not in get_bridges(G):
				break
			if G[current] == G[current][-1]:
				break
		path.append(t)
		G[current].remove(t)
		G[t].remove(current)
		current = t
	return path

V = vertices(G)
print (get_Euler_circuit(G, V[0]))




