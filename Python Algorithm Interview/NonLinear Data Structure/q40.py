#q40 네트워크 딜레이 타임
'''
(생각할 점)
-최단경로는 bfs사용, 다익스트라 알고리즘
-'모든 노드가 신호를 받는 데 걸리는 시간', '모든 노드에 도달할 수 있는지 여부' 2가지를 판단해야 한다. 
-가장 오래 걸리는 노드까지의 최단 시간 -> 다익스트라 알고리즘
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        #u는 출발 노드, v는 도착 노드, w는 소요 시간
        for u, v, w in times:
            graph[u].append((v, w))

        #(소요시간, 정점)
        Q = [(0,k)]
        dist = collections.defaultdict(int)

        while Q:
            #현재 가장 소요 시간이 적은 노드를 꺼낸다.
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    #현재 노드까지의 소요 시간과 다음 노드로의 소요 시간을 더한다.
                    alt = time+w
                    heapq.heappush(Q, (alt, v))
        
        if len(dist) == n:
            return max(dist.values())
        return -1




             
        
