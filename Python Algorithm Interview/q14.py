#두 정렬 리스트의 병합
# 1->2->4, 1->3->4  ==>  1->1->2->3->4->4

from typing import List
import collections

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
#재귀 풀이
class solution:      
    def mergeTwoLists(self, l1:ListNode, l2:ListNode)->ListNode:
        #l1이 None 이거나 l2가 존재하고 l1.val > l2.val인 경우
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        
        return l1


#iterative 풀이
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        #result의 현재 위치 추적하는 포인터
        current = result

        while list1 and list2:
            if list1.val<list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            #current 포인터 이동
            current = current.next

        if list1:
            current.next = list1

        elif list2:
            current.next = list2

        return result.next