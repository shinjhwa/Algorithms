#유효한 팰린드롬
import collections
import re

#리스트로 변환
"""def isPalindrome(s:str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True
"""

#Deque 자료형 이용
"""def isPalindrome(s:str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs)>1:
        if strs.popleft() != strs.pop():
            return False
    
    return True
"""

#슬라이싱 사용
def isPalindrome(s:str)->bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    
    return s == s[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))