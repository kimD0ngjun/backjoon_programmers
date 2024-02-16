# 자력 x
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        # 그래프 구성
        for key, value in prerequisites:
            graph[key].append(value)

        trace = set() # 현재 분기에서의 추적 기록
        visit = set() # 전체 분기에서의 방문 기록 남기기

        def dfs(node):
            # 순환 구조이면 False
            if node in trace:
                return False

            # 이미 이전 분기에 방문해서 탐색의 필요성이 없는
						# 즉, 사이클이 아니라는 확신을 얻은 노드이면
            if node in visit:
                return True
    
            trace.add(node)
            
            for y in graph[node]:
                if not dfs(y):
                    return False
            
            trace.remove(node)
            # 탐색 종료 후 방문 노드 추가
            visit.add(node)
            
            return True
    
        # 각 시작점으로부터 순환 구조 여부 서치
        for i in list(graph):
            if not dfs(i):
                return False

        return True
    
    # 반복문 풀이는 불가능한 것인가???