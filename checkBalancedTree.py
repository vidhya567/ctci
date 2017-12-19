
from collections import defaultdict
from sys import maxint
minimum_int = -maxint - 2

class Node:
	def __init__(self,value):
		self.value = value
		self.left  = None
		self.right = None

def checkBalanced(root):
	if checkHeights(root) == minimum_int:
		return False
	else:
		return True

def checkHeights(node):
	# Leaf Node
	if not node:
		return 0

	# passing up violation
	leftHeight = checkHeights(node.left)
	if leftHeight == minimum_int:
		return minimum_int

	rightHeight = checkHeights(node.right)
	if rightHeight == minimum_int:
		return minimum_int

	#checking violation
	if abs(leftHeight - rightHeight) > 1:
		return minimum_int
	else:
		return max(leftHeight,rightHeight) + 1

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

array = [1,2,3,4,5,6,13,14]
treeRoot = minimalBST(array)
print checkBalanced(treeRoot)
root = Node(5)
root.left = Node(6)
root.left.left = Node(8)
root.left.left.left = Node(9)
print checkBalanced(root)






