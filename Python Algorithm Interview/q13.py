#펠린드롬 연결 리스트
#1->2 false, 1->2->2->1 true
from typing import List
import collections

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode)->bool:
        #q: List = []
        q:Deque = collections.deque()
    
        if not head:
            return True
    
        node = head
    
        while node is not None:
            q.append(node.val)
            node = node.next
    
        while len(q)>1:
            if q.popleft() != q.pop():
                return False
        
        return True
    
sol = Solution()
ln = ListNode([1,2,2,1])
print(sol.isPalindrome(ln))
        