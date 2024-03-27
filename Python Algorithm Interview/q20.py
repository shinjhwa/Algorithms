#유효한 괄호
#()[]{} true
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        table = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for char in s:
            #여는 괄호일때
            if char not in table:
                stack.append(char)
            #stack이 비어있거나 딕셔너리와 일치하지 않을때
            elif not stack or table[char] != stack.pop():
                return False
        
        return len(stack) == 0