#.......Implementation of AVL Tree.....
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
      # insertion
    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
#   Inorder Traversal
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.key, end=" ")
            self.inorderTraversal(root.right)

# output 
avlTree = AVLTree()
root = None
keys = [10, 20, 30, 40, 50, 25]

for key in keys:
    root = avlTree.insert(root, key)

print("Inorder Traversal of AVL tree:")
avlTree.inorderTraversal(root)


# #include <iostream>
# #include <algorithm>

# class AvlTree {
#     struct Node {
#         int data;
#         Node* left;
#         Node* right;
#         int height;
#         Node(int val) : data(val), left(nullptr), right(nullptr), height(1) {}
#     };

#     Node* root;

# public:
#     AvlTree() : root(nullptr) {}
    
#     AvlTree(int arr[], int size) : root(nullptr) {
#         for (int i = 0; i < size; ++i) {
#             root = Insert(root, arr[i]);
#         }
#     }

#     ~AvlTree() {
#         // Implement destructor to delete nodes
#         DestroyTree(root);
#     }

#     // Override Functions
#     void visualizeTree() {
#         visualizeTree(root, 0);
#     }

#     Node* Insert(int x) {
#         return Insert(root, x);
#     }

#     Node* Delete(int x) {
#         return Delete(root, x);
#     }

# private:
#     // Helper functions
#     int height(Node* node) {
#         if (node == nullptr) return 0;
#         return node->height;
#     }

#     int balanceFactor(Node* node) {
#         if (node == nullptr) return 0;
#         return height(node->left) - height(node->right);
#     }

#     void updateHeight(Node* node) {
#         if (node == nullptr) return;
#         node->height = 1 + std::max(height(node->left), height(node->right));
#     }

#     Node* rightRotate(Node* y) {
#         Node* x = y->left;
#         Node* T2 = x->right;

#         x->right = y;
#         y->left = T2;

#         updateHeight(y);
#         updateHeight(x);

#         return x;
#     }

#     Node* leftRotate(Node* x) {
#         Node* y = x->right;
#         Node* T2 = y->left;

#         y->left = x;
#         x->right = T2;

#         updateHeight(x);
#         updateHeight(y);

#         return y;
#     }

#     Node* Insert(Node* node, int x) {
#         if (node == nullptr) {
#             return new Node(x);
#         }

#         if (x < node->data) {
#             node->left = Insert(node->left, x);
#         } else if (x > node->data) {
#             node->right = Insert(node->right, x);
#         } else {
#             // No duplicate values allowed
#             return node;
#         }

#         updateHeight(node);

#         int balance = balanceFactor(node);

#         // Left Left Case
#         if (balance > 1 && x < node->left->data) {
#             return rightRotate(node);
#         }
#         // Right Right Case
#         if (balance < -1 && x > node->right->data) {
#             return leftRotate(node);
#         }
#         // Left Right Case
#         if (balance > 1 && x > node->left->data) {
#             node->left = leftRotate(node->left);
#             return rightRotate(node);
#         }
#         // Right Left Case
#         if (balance < -1 && x < node->right->data) {
#             node->right = rightRotate(node->right);
#             return leftRotate(node);
#         }

#         return node;
#     }

#     Node* minValueNode(Node* node) {
#         Node* current = node;

#         while (current->left != nullptr) {
#             current = current->left;
#         }

#         return current;
#     }

#     Node* Delete(Node* node, int x) {
#         if (node == nullptr) {
#             return node;
#         }

#         if (x < node->data) {
#             node->left = Delete(node->left, x);
#         } else if (x > node->data) {
#             node->right = Delete(node->right, x);
#         } else {
#             if (node->left == nullptr || node->right == nullptr) {
#                 Node* temp = node->left ? node->left : node->right;

#                 if (temp == nullptr) {
#                     temp = node;
#                     node = nullptr;
#                 } else {
#                     *node = *temp;
#                 }

#                 delete temp;
#             } else {
#                 Node* temp = minValueNode(node->right);
#                 node->data = temp->data;
#                 node->right = Delete(node->right, temp->data);
#             }
#         }

#         if (node == nullptr) {
#             return node;
#         }

#         updateHeight(node);

#         int balance = balanceFactor(node);

#         // Left Left Case
#         if (balance > 1 && balanceFactor(node->left) >= 0) {
#             return rightRotate(node);
#         }
#         // Right Right Case
#         if (balance < -1 && balanceFactor(node->right) <= 0) {
#             return leftRotate(node);
#         }
#         // Left Right Case
#         if (balance > 1 && balanceFactor(node->left) < 0) {
#             node->left = leftRotate(node->left);
#             return rightRotate(node);
#         }
#         // Right Left Case
#         if (balance < -1 && balanceFactor(node->right) > 0) {
#             node->right = rightRotate(node->right);
#             return leftRotate(node);
#         }

#         return node;
#     }

#     void DestroyTree(Node* node) {
#         if (node == nullptr) return;

#         DestroyTree(node->left);
#         DestroyTree(node->right);

#         delete node;
#     }

#     void visualizeTree(Node* node, int space) {
#         constexpr int spacing = 5;
#         if (node == nullptr) return;

#         space += spacing;

#         visualizeTree(node->right, space);

#         std::cout << std::endl;
#         for (int i = spacing; i < space; i++) {
#             std::cout << " ";
#         }
#         std::cout << node->data << "\n";

#         visualizeTree(node->left, space);
#     }
# };
