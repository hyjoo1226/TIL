'''
7
3 5 1 2 7 4 -5
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self): #관리할 데이터는 최상위 root
        self.root = None

    def insert(self, key):  #없으면 그냥 삽입
        if self.root is None:
            self.root = Node(key)
        else:   #있으면 자리를 찾아서 삽입
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:  #작으면 왼쪽을 고려
            if node.left is None:   #왼쪽에 삽입 가능하면 삽입
                node.left = Node(key)
            else:   #왼쪽에 데이터가 있어 삽입 못하면 재귀로 한번 더 탐색
                self._insert(node.left, key)
        else:   #크면 오른쪽을 고려
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):  #탐색
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)
    
    def delete(self, key):  #삭제
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # 기본 경우: 트리가 비어있거나 키를 찾지 못한 경우
        if node is None:
            return node

        # 키를 찾아 왼쪽 또는 오른쪽 서브트리로 이동
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # 키를 찾은 경우: 이 노드를 삭제해야 함

            # 경우 1: 리프 노드 또는 하나의 자식만 있는 노드
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 경우 2: 두 개의 자식이 있는 노드
            # 오른쪽 서브트리에서 가장 작은 노드를 찾음
            temp = self._min_value_node(node.right)
            # 현재 노드의 키를 후계자의 키로 대체
            node.key = temp.key
            # 후계자 노드를 삭제
            node.right = self._delete(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        current = node
        # 가장 왼쪽 리프를 찾아 내려감
        while current.left is not None:
            current = current.left
        return current

# 테스트 코드
N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("초기 중위 순회 결과:", end=' ')
bst.inorder_traversal()

# 삭제 연산 테스트
key_to_delete = 5
bst.delete(key_to_delete)

print(f'\n{key_to_delete} 삭제 후 중위 순회 결과:', end=' ')
bst.inorder_traversal()

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")

bst.insert(-8)
print("\n-8 삽입 후 중위 순회 결과:", end=' ')
bst.inorder_traversal()

# N = int(input())
# arr = list(map(int, input().split()))

# bst = BinarySearchTree()

# for num in arr:
#     bst.insert(num)

# print("중위 순회 결과:", end=' ')
# bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# # 탐색 예제
# key = 5
# result = bst.search(key)
# if result:
#     print(f"\n키 {key} 찾음.")
# else:
#     print(f"\n키 {key} 못 찾음.")
