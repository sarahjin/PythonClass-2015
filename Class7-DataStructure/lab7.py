"""Data Structures
Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# Ring Network
ring = {} # empty graph 

n = 5 # number of nodes 

# Add in edges
for i in range(n):
	print "making ring with ring: %s, %d, %d" %(ring, i, (i+1)%n)
	ring = makeLink(ring, i, (i+1)%n)
	print "now ring is: %s" %ring

# How many nodes?
print len(ring)

# How many edges?
ring.keys()
#[0,1,2,3,4]
print sum([len(ring[node]) for node in ring.keys()])/2 


# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 

new_ring ={}
for i in range(16):
	for j in range(15):
		new_ring = makeLink(new_ring, (i,j), (i,j+1))
		
for j in range(16):
	for i in range(15):		
		new_ring = makeLink(new_ring, (i,j), (i+1,j))
		
#the number of nodes:
print len(new_ring)

#the number of edges:
edge_note =[]
for node in new_ring.keys():
	edge_note.append(len(new_ring[node]))

print sum(edge_note)/2
	

# TODO: define a function countEdges
def countedge(ring):
	return sum([len(ring[node]) for node in ring.keys()])/2
		

# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

# How many nodes in movies?
print len(movies)
#7

# How many edges in movies?
print countedge(movies)
#10

def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 

# TODO: find an Eulerian tour of the movie network and check it 
movie_tour = movies.keys()
print movie_tour
tour(movies, movie_tour)

mytour=[kb,dh,rd,ms,ah,jr,ss,dh,jr,kb,ms]

tour(movies,mytour)


def findPath(graph, start, end, path=[]):
        path = path + [start]
        print "Now path is %s" %path
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
            	print "now node is %s" %node
                newpath = findPath(graph, node, end, path)
                if newpath: return newpath
        return None

print findPath(movies, jr, ms)


# TODO: implement findShortestPath()
# print findShortestPath(movies, ms, ss)

# TODO: implement findAllPaths() to find all paths between two nodes
# allPaths = findAllPaths(movies, jr, ms)
# for path in allPaths:
#   print path

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.