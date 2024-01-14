#내 풀이
'''def reverse(s:str):
    s2 = []
    for char in s:
        s2.insert(0, char)
    print(s2)


reverse(["h","e","l","l","o"])
reverse(["H","a","n","n","a","h"])'''

#투 포인터
'''from typing import List

def reverseString(s: List[str])->None:
    left,right=0, len(s)-1
    while left<right:
        s[left], s[right] = s[right], s[left]
        left+=1
        right-=1
    
    print(s)

reverseString(["h","e","l","l","o"])'''

#파이썬다운 방식
from typing import List
def reverseString(s:List[str])->None:
    s.reverse()
    print(s)

reverseString(["h","e","l","l","o"])





