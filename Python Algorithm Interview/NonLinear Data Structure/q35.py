#q35 조합의 모든 경우의 수 나열하기
'''
(생각할 점)
-ans의 참조를 추가하는 것이므로 ans를 변경하면 기존의 추가했던 ans도 변경됨. 따라서 ans[:]를 사용해야 함.
-ans.pop()으로 ans의 값을 제거해야 함.
-itertools.combinations(range(1, n + 1), k)로 사용가능
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        ans = []
        
        def dfs(index):
            if len(ans)==k:
                result.append(ans[:])
                return
            
            for i in range(index, n+1):
                ans.append(i)
                dfs(i+1)
                ans.pop()

        dfs(1)
        return result



        
