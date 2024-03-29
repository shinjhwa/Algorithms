# 일일 온도
'''
(생각할 점)
- stack에 73 등의 값 자체를 넣으려고 했지 index를 넣는다는 발상을 하지 못함
- enumerate 사용하기
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                ans[last] = i-last
            stack.append(i)
        
        return ans




        