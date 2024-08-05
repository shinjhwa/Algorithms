#q38 여행 일정 구성
'''
(생각할 점)
-collections.defaultdict은 딕셔너리(dictionary)와 거의 비슷하지만 key값이 없을 경우 미리 지정해 놓은 초기(default)값을 반환하는 dictionary
-정렬 위해 for문 두 개 사용할 필요x, sorted(tickets)
-pop(0)은 O(n), pop()은 O(1) 따라서 애초에 sorted(tickets, reverse=True)로 구섣하는 게 좋음
'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route=[]
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        return route[::-1]
        
#다른 풀이(반복)
'''
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        return route[::-1]
'''
