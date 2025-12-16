# ============================================================
# TRABALHO 3 - ESTRUTURA DE DADOS
# Árvores Binárias de Busca, AVL e Rubro-Negra
# Linguagem: Python
# ============================================================

# ------------------------------------------------------------
# 1. TREE MAP (ÁRVORE BINÁRIA DE BUSCA)
# ------------------------------------------------------------
class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key, value=None):
        if self.root is None:
            self.root = BSTNode(key, value)
            return
        self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left:
                self._insert(node.left, key, value)
            else:
                node.left = BSTNode(key, value)
                node.left.parent = node
        else:
            if node.right:
                self._insert(node.right, key, value)
            else:
                node.right = BSTNode(key, value)
                node.right.parent = node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (4 * level) + prefix + str(node.key))
            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")

# ------------------------------------------------------------
# 2. AVL TREE MAP
# ------------------------------------------------------------
class AVLNode(BSTNode):
    def __init__(self, key, value=None):
        super().__init__(key, value)
        self.height = 1

class AVLTreeMap(TreeMap):
    def height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if not node:
            return AVLNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        self.update_height(node)
        balance = self.balance_factor(node)

        # Left Left
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Right Right
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

# ------------------------------------------------------------
# 3. RED-BLACK TREE MAP
# ------------------------------------------------------------
class RBNode(BSTNode):
    RED = True
    BLACK = False

    def __init__(self, key, value=None, color=RED):
        super().__init__(key, value)
        self.color = color

class RedBlackTreeMap:
    def __init__(self):
        self.root = None

    def rotate_left(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        right.color = node.color
        node.color = RBNode.RED
        return right

    def rotate_right(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        left.color = node.color
        node.color = RBNode.RED
        return left

    def flip_colors(self, node):
        node.color = RBNode.RED
        node.left.color = RBNode.BLACK
        node.right.color = RBNode.BLACK

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)
        self.root.color = RBNode.BLACK

    def _insert(self, node, key, value):
        if not node:
            return RBNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        if node.right and node.right.color == RBNode.RED and not (node.left and node.left.color == RBNode.RED):
            node = self.rotate_left(node)
        if node.left and node.left.color == RBNode.RED and node.left.left and node.left.left.color == RBNode.RED:
            node = self.rotate_right(node)
        if node.left and node.right and node.left.color == RBNode.RED and node.right.color == RBNode.RED:
            self.flip_colors(node)

        return node

# ------------------------------------------------------------
# 4. EXERCÍCIO 4 - INSERÇÕES NA BST
# ------------------------------------------------------------
if __name__ == '__main__':
    print("\nEXERCÍCIO 4 - BST")
    bst = TreeMap()
    keys = [30, 40, 24, 58, 48, 26, 11, 13]
    for k in keys:
        print(f"\nInserindo {k}:")
        bst.insert(k)
        bst.print_tree()

    print("\nEXERCÍCIO 7 - RUBRO-NEGRA")
    rbt = RedBlackTreeMap()
    keys_rb = [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]
    for k in keys_rb:
        rbt.insert(k)
    print("Inserção concluída na árvore rubro-negra.")
