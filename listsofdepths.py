

from collections import defaultdict

def levelOrder(root):
	traverseLevel(root, 0)

class Node:
 def __init__(self, value):
  	self.left  = None
  	self.right = None
  	self.value = value

levelDict = defaultdict(list)

def traverseLevel(node, level):
	global levelDict
	levelDict[level].append(node.value)
	if (node.left):
		traverseLevel(node.left,level+1)
	if (node.right):
		traverseLevel(node.right,level+1)

def minimalBST(array):
	lenOfArray = len(array)
	if (lenOfArray == 1):
		return Node(array[0])
	else:
		mid  = len(array)/2
		root = Node(array[mid])
		if (array[mid-1]):
			root.left  = minimalBST(array[0:mid])  
		if ((mid+1)<lenOfArray):
			root.right = minimalBST(array[mid+1:len(array)])
		return root

def performBFS(root):
	depths = []
	initialList = [root]
	BFS(initialList, depths)
	return depths

def addValues(nodes):
	valueList = []
	for node in nodes:
		valueList.append(node.value)
	return valueList

def BFS(currList, depths):
	while (len(currList) > 0):
		depths.append(addValues(currList))
		parentList = currList
		currList = []
		for i in xrange(len(parentList)):
			parent = parentList[i]
			if (parent.left):
				currList.append(parent.left)
			if (parent.right):
				currList.append(parent.right)


array = [1,2,3,4,5,6,13,14]
treeRoot = minimalBST(array)
levelOrder(treeRoot)
print levelDict

depthTree = performBFS(treeRoot)
print "depth",depthTree
