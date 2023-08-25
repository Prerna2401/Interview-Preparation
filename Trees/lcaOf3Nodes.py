import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def lca(r,d1,d2,d3):
    if r == None:
        return None
    if r.data == d1 or r.data == d2 or r.data == d3:
        return r
    left = lca(r.left,d1,d2,d3)
    right = lca(r.right,d1,d2,d3)
    if left and right:
        return r
    if left == None:
        return right
    return left

def lcaOf3Nodes(root, node1, node2, node3):
    res = lca(root, node1, node2, node3)
    return res.data

def buildLevelTree(li):
    #Given format of nodes is in level order traversal, so we have to build the tree that way
    index = 0
    length = len(li)
    if length <= 0 or li[0] == -1:
        return None
    root = BinaryTreeNode(li[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currNode = q.get()
        leftChild = li[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currNode.left = leftNode
            q.put(leftNode)
        rightChild = li[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currNode.right = rightNode
            q.put(rightNode)
    return root

t = int(input())
while t > 0:
    nodes = [int(i) for i in input().split()]
    treeNodes = [int(i) for i in input().split()]
    root = buildLevelTree(treeNodes)
    print(lcaOf3Nodes(root,nodes[0],nodes[1],nodes[2]))
    t -= 1