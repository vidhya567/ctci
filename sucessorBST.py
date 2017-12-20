
class Node:
 	def __init__(self, value):
	  	self.left   = None
	  	self.right  = None
	  	self.parent = None
	  	self.value  = value

# sucessor of node A is a node with lowest value higher than value of A
def sucessor(node):
	if (node.right):
		return minBST(node.right)
	else:
		# percolate up till a parent has the node as the left node
		parentNode = node.parent
		childNode  = node
		while (parentNode and childNode == parentNode.right):
			childNode = parentNode
			parentNode = parentNode.parent
		return parentNode.value

def minBST(node):
	while(node.left):
		node = node.left
	return node.value

root = Node(15)
node1 = Node(6)
node2 = Node(18)
node3 = Node(3)
node4 = Node(7)
node5 = Node(17)
node6 = Node(20)
node7 = Node(2)
node8 = Node(4)
node9 = Node(13)
node10 = Node(9)
root.left  = node1
root.right = node2
node1.parent = node2.parent = root
node1.left  = node3
node1.right = node4
node3.parent = node4.parent = node1
node2.left  = node5
node2.right = node6
node5.parent = node6.parent = node2
node3.left  = node7
node3.right = node8
node7.parent = node8.parent = node3
node4.right = node9
node9.parent = node4
node9.left  = node10
node10.parent = node9
print sucessor(node2)
print sucessor(root)
print sucessor(node9)












