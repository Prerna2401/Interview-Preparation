class TreeNode:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def insert(root, key):
    if not root:
        return TreeNode(key)
    
    queue = [root]

    while queue:
        current = queue.pop(0)
        if not current.left:
            current.left = TreeNode(key)
            break
        else:
            queue.append(current.left)
        
        if not current.right:
            current.right = TreeNode(key)
            break
        else:
            queue.append(current.right)

    return root

root = None

while True:
    try:
        key = input('Enter value to be inserted (Enter q to quit): ')
        if key.lower() == 'q':
            break
        root = insert(root, int(key))
    except ValueError:
        print('Invalid input. Please enter a valid integer or "q" to quit.')

print('Inorder Traversal of the Binary Tree:')
inorder(root)
