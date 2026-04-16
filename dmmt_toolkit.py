class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_res(self.root, key)

    def _insert_res(self, node, key):
        if not node: return BSTNode(key)
        if key < node.key:
            node.left = self._insert_res(node.left, key)
        else:
            node.right = self._insert_res(node.right, key)
        return node

    def search(self, key):
        curr = self.root
        while curr:
            if curr.key == key: return True
            curr = curr.left if key < curr.key else curr.right
        return False

    def inorder_traversal(self):
        res = []
        def _travel(node):
            if node:
                _travel(node.left)
                res.append(node.key)
                _travel(node.right)
        _travel(self.root)
        return res

    def delete(self, key):
        self.root = self._del_res(self.root, key)

    def _del_res(self, node, key):
        if not node: return None
        if key < node.key:
            node.left = self._del_res(node.left, key)
        elif key > node.key:
            node.right = self._del_res(node.right, key)
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            temp = self._min_node(node.right)
            node.key = temp.key
            node.right = self._del_res(node.right, temp.key)
        return node

    def _min_node(self, node):
        while node.left: node = node.left
        return node

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, w):
        if u not in self.adj: self.adj[u] = []
        self.adj[u].append((v, w))

    def bfs(self, start):
        visited, queue, order = {start}, [start], []
        while queue:
            u = queue.pop(0)
            order.append(u)
            for v, w in self.adj.get(u, []):
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        return order

    def dfs(self, start):
        visited, order = set(), []
        def _visit(u):
            visited.add(u)
            order.append(u)
            for v, w in self.adj.get(u, []):
                if v not in visited: _visit(v)
        _visit(start)
        return order

class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        idx = key % self.size
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def get(self, key):
        idx = key % self.size
        for k, v in self.table[idx]:
            if k == key: return v
        return None

    def delete(self, key):
        idx = key % self.size
        self.table[idx] = [pair for pair in self.table[idx] if pair[0] != key]

def main():
    # BST Test
    bst = BST()
    for x in [50, 30, 70, 20, 40, 60, 80]: bst.insert(x)
    print("BST Inorder:", bst.inorder_traversal())
    print("Search 20:", bst.search(20))
    bst.delete(20) # Leaf
    bst.insert(65)
    bst.delete(60) # One child
    bst.delete(50) # Two children
    print("BST After Deletions:", bst.inorder_traversal())

    # Graph Test
    g = Graph()
    for u, v, w in [('A','B',2), ('A','C',4), ('B','D',7), ('B','E',3), ('C','E',1), ('D','F',5), ('E','D',2), ('E','F',6), ('C','F',8)]:
        g.add_edge(u, v, w)
    print("\nAdjacency List:", g.adj)
    print("BFS:", g.bfs('A'))
    print("DFS:", g.dfs('A'))

    # Hash Table Test
    ht = HashTable(5)
    for k in [10, 15, 20, 7, 12]: ht.insert(k, f"Data{k}")
    print("\nHash Table:", ht.table)
    ht.delete(15)
    print("Bucket 0 after deleting 15:", ht.table[0])

if __name__ == "__main__":
    main()