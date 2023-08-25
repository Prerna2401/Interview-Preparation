class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    #Height using recursive DFS        
    def maxDepth(self, node):
        if self.node is None:
            return 0
        else:
            ldepth = Node.maxDepth(node.left)
            rdepth = Node.maxDepth(node.right)
            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1
        
    #Height using level order traversal
    def height(self, node):
        depth = 0
        q = []
        q.append(self.node)
        q.append(None)
        while len(q) > 0:
            temp = q[0]
            q = q[1:]
            if temp == None:
                depth += 1
            if temp != None:
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            elif len(q) > 0:
                q.append(None)
        return depth
    
tree = Node()
print('Enter value of node: ')
