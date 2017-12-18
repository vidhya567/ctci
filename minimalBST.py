

class Node:
 def __init__(self, value):
  	self.left  = None
  	self.right = None
  	self.value = value


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

def printTree(root):	
	if (root.left != None):
			printTree(root.left)
	print root.value,
	if (root.right != None):
			printTree(root.right)


array = [1,2,3,4,5,6,13,14]
treeRoot = minimalBST(array)
printTree(treeRoot)
print
array = [5,6,13,14]
treeRoot = minimalBST(array)
printTree(treeRoot)





