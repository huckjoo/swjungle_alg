# Node 클래스 정의, 초기화
class Node(object):                    # 여기서의 object는 뭐냐?
    def __init__(self, data):          # Node를 시작하면 매개변수로 data를 받아온다.
        self.data = data               # 노드값을 data에 받는다.
        self.left = self.right = None  # 초기에 좌우 노드는 비어있다.


class BinarySearchTree(object):      # 이진탐색트리 클래스
    # root속성 초기화
    def __init__(self):
        self.root = None
    # insert 부분

    def insert(self, data):    # insert method는 data를 매개변수로 받는다.
        self.root = self._insert_value(self.root, data)
        return self.root is not None   # 무슨 뜻인지 모르겠다.

    def _insert_value(self, node, data):  # 매개변수로 node, data를 받음
        if node is None:  # 노드가 없으면
            node = Node(data)  # node를 생성해서 node.data에 data를 넣는다.
        else:  # 노드가 있으면
            if data <= node.data:  # 현재 들어온 data가 현재 node의 값보다 작을때
                # 현재 노드의 왼쪽에 BinarySearchTree._insert_value(node.left,data)를 실행한다.
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)
bst.post_order_traversal()
