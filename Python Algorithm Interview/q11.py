#자신을 제외한 배열의 곱

#[1, 2, 3, 4] -> [24, 12, 8, 6]
#투 포인터로 풀어보자..!
from typing import List


def mul(nums:List[int])->List[int]:
    ans = []
    
    for i in range(len(nums)):
        left, right = 0, len(nums)-1
        mul_left = 1
        mul_right = 1
        
        while(left < i):
            mul_left *= nums[left]
            left+=1
        while(right > i):
            mul_right *= nums[right]
            right-=1
        ans.append(mul_left*mul_right)
    
    return ans
            
print(mul([1, 2, 3, 4]))