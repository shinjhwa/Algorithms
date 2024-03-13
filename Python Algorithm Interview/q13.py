#펠린드롬 연결 리스트
#1->2 false, 1->2->2->1 true
from typing import List
from typing import ListNode

def isPalindrome(self, head: ListNode)->bool:
    q: List = []
    
    if not head:
        return True
    
    node = head
    
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q)>1:
        if q.pop(0) != q.pop():
            return False
        
    return True
        