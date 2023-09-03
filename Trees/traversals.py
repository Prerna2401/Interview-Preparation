class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end = ' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end = ' ')
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end = ' ')
        
root = None

while True:
    try:
        key = input('Enter value to be inserted(Enter q to quit): ')
        if key.lower() == 'q':
            break
        root = insert(root, key)
    except ValueError:
        print('Invalid input!')
        
print('Preorder Traversal ')
preorder(root)
print('\nInorder Traversal ')
inorder(root)
print('\nPostorder Traversal ')
postorder(root)