#배열 파이션1

#내 풀이
from typing import List

def pairSum(nums: List[int])->int:
    sum = 0
    nums.sort(reverse=True)
    
    for i in range(0, len(nums), 2):
        if i+1 < len(nums):
            sum += min(nums[i], nums[i+1])
    
    return sum

print(pairSum([1,4,3,2]))
            
#정렬(reverse=True)한 후 홀수번째 인덱스의 값을 더하는 방법도 있음

#파이썬다운 방식
def arrayPairSum(nums:List[int])->int:
    return sum(sorted(nums)[::2])

print(arrayPairSum([1,4,3,2]))