#Design Circular Deque
'''
(생각할 점)
-_add, _del 함수에서 사용된 '_'의 의미는 내부에서만 사용한다는 의미
-원형 deque를 이중 연결리스트로 구현할 이유x -> 원형의 이점을 전혀 살리지 못함
'''

#이중 연결리스트를 이용해 deque를 직접 구현
class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k,0
        self.head.right, self.tail.left = self.tail, self.head

    #새로운 노드(new)를 기존 노드(node)와 그 다음 노드 사이에 삽입
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
    
    #지정된 노드(node)의 다음 노드를 리스트에서 제거
    def _del(self, node:ListNode):
        n = node.right.right
        node.right = n
        n.left = node
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k