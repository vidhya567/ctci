
class Node:
 	def __init__(self, value):
	  	self.left  = None
	  	self.right = None
	  	self.value = value

def valiadteBST(root):
	return checkTree(root, None, None)

def checkTree(node, minValue, maxValue):
	
	if (not node):
		return True
	if (minValue and node.value <= minValue) or (maxValue and  node.value > maxValue):
		return False
	if (not checkTree(node.left, minValue, node.value)):
		return False
	if (not checkTree(node.right, node.value, maxValue)):
		return False
	return True	

treeRoot1 = Node(20)
treeRoot1.left = Node(10)
treeRoot1.right = Node(30)
treeRoot1.left.right = Node(25)
if (not valiadteBST(treeRoot1)):
	print "Test Case 1 with Violation Passed"

treeRoot2 = Node(20)
treeRoot2.left = Node(10)
treeRoot2.right = Node(30)
treeRoot2.left.right = Node(15)
if (valiadteBST(treeRoot2)):
	print "Test Case 2 without Violation Passed"

treeRoot3 = Node(20)
treeRoot3.left = Node(10)
treeRoot3.right = Node(30)
treeRoot3.right.left = Node(15)
if (not valiadteBST(treeRoot3)):
	print "Test Case 3 with Violation Passed"






