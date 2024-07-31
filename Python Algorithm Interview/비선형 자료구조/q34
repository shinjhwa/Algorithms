#q34 순열의 모든 경우의 수 나열하기
'''
(생각할 점): 예시
-[1,2,3]이 results에 들어간 후, 다시 dfs(3)호출.. prev_elements에서 2가 pop, 다시 dfs([2,3]) 호출.. 
-dfs([2,3])일 때, for으로 다시 돌아감.. 이제 e는 3 다시 dfs로 들어가면 [1,3,2]가 results에 들어감
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements)==0:
                results.append(prev_elements[:])

            for e in elements:
                #다음 dfs 파라미터
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results

#다른 풀이(itertools.permutations)
'''
def permute(self, nums: List[int]) -> List[List[int]]:
    return list(map(list, itertools.permutations(nums)))
'''
