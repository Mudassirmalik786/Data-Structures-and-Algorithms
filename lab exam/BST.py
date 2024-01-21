#.........Implementation of BST...........
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root == None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root == None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def minValueNode(node):
    while node.left != None:
        node = node.left
    return node

def deleteNode(root, key):
    if root == None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left == None:
            temp = root.right
            root = None
            return temp
        elif root.right == None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root
    
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.key, end=" ")
        inorderTraversal(root.right)

#..........output.........
root = None
keys = [50, 30, 20, 40, 70, 60, 80]
# Insertion
for key in keys:
    root = insert(root, key)
# Inorder Traversal
print("Inorder Traversal before deletion:")
inorderTraversal(root)
print("")

# Searching
print("Search Result")
searchKey = 40
result = search(root, searchKey)
if result:
    print(searchKey,"Found in the tree")
else:
    print("Not found")

# Deletion
root = deleteNode(root, 30)
print("Inorder Traversal after deletion:")
inorderTraversal(root)

