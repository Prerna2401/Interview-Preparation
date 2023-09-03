class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end = ' ')
        inorder(root.right)

root = None

while True:
    try:
        val = int(input('Enter a value(Press q to quit): '))
        root = insert(root, val)
    except ValueError:
        exit = input('Type q to exit or press Enter to continue: ')
        if exit.lower() == 'q':
            break
        
print('Inorder Traversal: ', inorder(root))       