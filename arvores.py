# ============================================================
# ARVORES BINARIAS - IMPLEMENTAÇÃO COMPLETA
# Contém:
# - LinkedBinaryTree
# - ArrayBinaryTree
# - Pre/In/Post-order
# - Exercícios 5, 6, 7 e 8 com exemplos das imagens
# ============================================================

class LinkedBinaryTree:

    class Node:
        def __init__(self, element, left=None, right=None):
            self.element = element
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def add_root(self, element):
        if self.root is not None:
            raise ValueError("Root já existe.")
        self.root = self.Node(element)
        return self.root

    def add_left(self, node, element):
        if node.left is not None:
            raise ValueError("Esse nó já possui filho à esquerda.")
        node.left = self.Node(element)
        return node.left

    def add_right(self, node, element):
        if node.right is not None:
            raise ValueError("Esse nó já possui filho à direita.")
        node.right = self.Node(element)
        return node.right


# ============================================================
# ARRAY BINARY TREE
# ============================================================

class ArrayBinaryTree:
    def __init__(self, capacity=100):
        self.data = [None] * (capacity + 1)

    def add_root(self, element):
        self.data[1] = element

    def add_left(self, idx, element):
        self.data[idx*2] = element

    def add_right(self, idx, element):
        self.data[idx*2 + 1] = element

    def get(self, idx):
        return self.data[idx]


# ============================================================
# TRAVESSIAS
# ============================================================

def preorder(node):
    if node:
        print(node.element)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.element)
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.element)


# ============================================================
# EXERCICIO 5 — ÁRVORE SOMA
# ============================================================

def verificar_arvore_soma(node):
    if node is None:
        return 0, True

    if node.left is None and node.right is None:
        return node.element, True

    soma_esq, ok_esq = verificar_arvore_soma(node.left)
    soma_dir, ok_dir = verificar_arvore_soma(node.right)

    ok = ok_esq and ok_dir and node.element == soma_esq + soma_dir

    return node.element + soma_esq + soma_dir, ok


# ============================================================
# EXERCICIO 6 — Caminhos raiz->folhas
# ============================================================

def imprimir_caminhos(node, caminho=None):
    if caminho is None:
        caminho = []

    if node is None:
        return

    caminho.append(node.element)

    if node.left is None and node.right is None:
        print(" -> ".join(map(str, caminho)))

    imprimir_caminhos(node.left, caminho)
    imprimir_caminhos(node.right, caminho)

    caminho.pop()


# ============================================================
# EXERCICIO 7 — Ancestrais
# ============================================================

def encontrar_ancestrais(root, alvo, caminho=[]):
    if root is None:
        return False

    caminho.append(root.element)

    if root.element == alvo:
        print("Ancestrais de", alvo, ":", caminho[:-1])
        return True

    if encontrar_ancestrais(root.left, alvo, caminho) or encontrar_ancestrais(root.right, alvo, caminho):
        return True

    caminho.pop()
    return False


# ============================================================
# EXERCICIO 8 — Substituir por soma das subárvores
# ============================================================

def substituir_por_soma(node):
    if node is None:
        return 0

    soma_esq = substituir_por_soma(node.left)
    soma_dir = substituir_por_soma(node.right)

    antigo = node.element
    node.element = soma_esq + soma_dir

    return antigo + soma_esq + soma_dir


# ============================================================
# EXEMPLOS DOS EXERCÍCIOS (conforme as imagens)
# ============================================================

if __name__ == "__main__":

    print("\n====== EXERCICIO 5 — ÁRVORE SOMA ======")

    tree = LinkedBinaryTree()
    r = tree.add_root(44)
    n9 = tree.add_left(r, 9)
    n13 = tree.add_right(r, 13)
    tree.add_left(n9, 4)
    tree.add_right(n9, 5)
    tree.add_left(n13, 6)
    tree.add_right(n13, 7)

    _, ok = verificar_arvore_soma(tree.root)
    print("É árvore soma?", ok)


    print("\n====== EXERCICIO 6 — Caminhos raiz→folhas ======")

    t = LinkedBinaryTree()
    r = t.add_root(1)
    n2 = t.add_left(r, 2)
    n3 = t.add_right(r, 3)
    t.add_left(n2, 4)
    n5 = t.add_right(n2, 5)
    n6 = t.add_left(n3, 6)
    n7 = t.add_right(n3, 7)
    t.add_right(n6, 8)
    t.add_right(n7, 9)

    imprimir_caminhos(t.root)


    print("\n====== EXERCICIO 7 — Ancestrais ======")
    encontrar_ancestrais(t.root, 9)
    encontrar_ancestrais(t.root, 6)
    encontrar_ancestrais(t.root, 5)


    print("\n====== EXERCICIO 8 — Substituir por soma ======")

    t2 = LinkedBinaryTree()
    r = t2.add_root(1)
    n2 = t2.add_left(r, 2)
    n3 = t2.add_right(r, 3)
    t2.add_left(n2, 4)
    n5 = t2.add_right(n2, 5)
    n6 = t2.add_left(n3, 6)
    t2.add_left(n5, 7)
    t2.add_right(n5, 8)

    substituir_por_soma(t2.root)

    print("Valor final da raiz:", t2.root.element)
