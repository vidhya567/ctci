
from collections import defaultdict
adjList = defaultdict(list)
visited = defaultdict(bool)

def createGraph(edges):
	global adjList,visited
	for edge in edges:
		adjList[edge[0]].append(edge[1])
		visited[edge[0]] = False
		visited[edge[1]] = False


# Is route possible from node 1 to node 2 #
def isRoutePossible(node1, node2):
	global adjList,visited
	currAdjList = adjList[node1]
	visited[node1] = True
	for node in currAdjList:
		if not visited[node]:
			if node == node2:
				return True
			else:
				if (isRoutePossible(node, node2)):
					return True
	return False

def clearVisitedData(edges):
	global visited
	for edge in edges:
		visited[edge[0]] = False
		visited[edge[1]] = False

print "TEST-SET 1"
edges1 = [[1,2],[2,3],[3,1],[3,4],[1,5],[6,7],[6,8],[7,8],[8,9],[1,10],[10,11],[11,12],[10,13]]
createGraph(edges1)
print "GRAPH CREATED"
testEdges = [[1,2],[2,4],[3,5],[1,6],[1,8],[6,9],[3,12],[3,13]]
testResult = [True,True,True,False,False,True,True,True]

for index,edge in enumerate(testEdges):
	if (isRoutePossible(edge[0],edge[1]) == testResult[index]):
		print "test case "+str(index)+" Passed"
	else:
		print "test case "+str(index)+" Failed"	
	clearVisitedData(edges1);





