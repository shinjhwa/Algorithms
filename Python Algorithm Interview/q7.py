#두수의 합

from typing import List

#나의 풀이 -> O(n^2) 비효율적
nums = [2, 7, 11, 15]
target = 9
answer = []

for i in range(len(nums)):
    if nums[i]<target:
        for j in range(i+1 , len(nums)):
            if nums[i]+nums[j]==target:
                answer.append(i)
                answer.append(j)
                break
            
print(answer)
        
#첫 번째 수를 뺀 결과 키 조회 -> O(n)
def twoSum(nums: List[int], target: int)->List[int]:
    nums_map = {}
    #키와 값을 바꿔서 딕셔너리로 저장
    for i,num in enumerate(nums):
        nums_map[num] = i
        
    #타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]:
            return nums.index(num), nums_map[target-num]
        
print(twoSum([2, 7, 11, 15], 9))