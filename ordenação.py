# ============================================================
# Trabalho 4 - Algoritmos de Ordenação
# Estrutura de Dados
# Autor: Fábio Stahl Azevedo
# ============================================================

from copy import deepcopy

# Estrutura para contar testes (comparações) e trocas
class Counter:
    def __init__(self):
        self.tests = 0
        self.swaps = 0

# ---------------- INSERTION SORT ----------------
def insertion_sort(arr):
    c = Counter()
    a = arr
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            c.tests += 1
            if a[j] > key:
                a[j + 1] = a[j]
                c.swaps += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return c

# ---------------- SELECTION SORT ----------------
def selection_sort(arr):
    c = Counter()
    a = arr
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            c.tests += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            c.swaps += 1
    return c

# ---------------- BUBBLE SORT ----------------
def bubble_sort(arr):
    c = Counter()
    a = arr
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            c.tests += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                c.swaps += 1
    return c

# ---------------- SHELL SORT ----------------
def shell_sort(arr):
    c = Counter()
    a = arr
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap:
                c.tests += 1
                if a[j - gap] > temp:
                    a[j] = a[j - gap]
                    c.swaps += 1
                    j -= gap
                else:
                    break
            a[j] = temp
        gap //= 2
    return c

# ---------------- MERGE SORT ----------------
def merge_sort(arr):
    c = Counter()

    def merge_sort_rec(a):
        if len(a) > 1:
            mid = len(a) // 2
            L = a[:mid]
            R = a[mid:]
            merge_sort_rec(L)
            merge_sort_rec(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                c.tests += 1
                if L[i] < R[j]:
                    a[k] = L[i]
                    i += 1
                else:
                    a[k] = R[j]
                    j += 1
                c.swaps += 1
                k += 1
            while i < len(L):
                a[k] = L[i]
                c.swaps += 1
                i += 1
                k += 1
            while j < len(R):
                a[k] = R[j]
                c.swaps += 1
                j += 1
                k += 1

    merge_sort_rec(arr)
    return c

# ---------------- QUICK SORT ----------------
def quick_sort(arr):
    c = Counter()

    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            c.tests += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                c.swaps += 1
        a[i + 1], a[high] = a[high], a[i + 1]
        c.swaps += 1
        return i + 1

    def quick_sort_rec(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quick_sort_rec(a, low, pi - 1)
            quick_sort_rec(a, pi + 1, high)

    quick_sort_rec(arr, 0, len(arr) - 1)
    return c

# ---------------- HEAP SORT ----------------
def heap_sort(arr):
    c = Counter()
    a = arr
    n = len(a)

    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n:
            c.tests += 1
            if a[l] > a[largest]:
                largest = l
        if r < n:
            c.tests += 1
            if a[r] > a[largest]:
                largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            c.swaps += 1
            heapify(n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        c.swaps += 1
        heapify(i, 0)
    return c

# ---------------- COUNTING SORT ----------------
def counting_sort(arr):
    c = Counter()
    a = arr
    max_val = max(a)
    count = [0] * (max_val + 1)
    for num in a:
        count[num] += 1
    i = 0
    for val in range(len(count)):
        while count[val] > 0:
            a[i] = val
            i += 1
            count[val] -= 1
            c.swaps += 1
    return c

# ---------------- TESTES ----------------
listas = [
    [12, 42, 83, 25, 67, 71, 3, 4, 94, 53],
    [100, 48, 19, 61, 86, 33, 13, 43, 84, 28],
    [81, 60, 6, 49, 40, 41, 38, 64, 44, 36],
    [45, 27, 11, 89, 63, 39, 9, 58, 52, 17],
    [88, 77, 26, 62, 30, 96, 56, 65, 98, 99],
    [76, 73, 16, 95, 35, 87, 68, 69, 51, 92],
    [37, 75, 90, 82, 8, 18, 23, 93, 57, 10],
    [15, 97, 14, 29, 7, 24, 31, 59, 78, 85],
    [5, 70, 55, 91, 47, 72, 2, 20, 34, 74],
    [50, 66, 32, 22, 54, 79, 21, 1, 80, 46]
]

algoritmos = [
    ("Insertion Sort", insertion_sort),
    ("Selection Sort", selection_sort),
    ("Bubble Sort", bubble_sort),
    ("Shell Sort", shell_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort),
    ("Heap Sort", heap_sort),
    ("Counting Sort", counting_sort)
]

for nome, alg in algoritmos:
    print("\n", nome)
    for lista in listas:
        copia = deepcopy(lista)
        c = alg(copia)
        print(f"Ordenado: {copia} | Testes: {c.tests} | Trocas: {c.swaps}")
