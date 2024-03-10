#세 수의 합

#[-1, 0, 1, 2, -1, -4]에서 답이 [-1, 0, 1], [-1,-1, 2]가 나와야 함

#브루트포스가 아닌 걸 생각해보자 -> 투 포인터?
from typing import List

def sum(nums:List[int]) -> List[List[int]]:
    ans = []
    nums.sort()
    
    for i in range(len(nums)- 2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        
        left = i+1
        right = len(nums)-1
        
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum<0:
                left += 1
            elif sum>0:
                right -= 1
            else:
                ans.append((nums[i], nums[left], nums[right]))

            while left<right and nums[left] == nums[left+1]:
                left += 1
            while left<right and nums[right] == nums[right-1]:
                right -= 1
                
            left += 1
            right -= 1
    
    return ans

print(sum([-1, 0, 1, 2, -1, -4]))    