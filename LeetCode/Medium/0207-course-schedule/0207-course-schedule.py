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
                
            # 백트랙킹 조건 : 사이클 판정이 난 노드라면 바로 False
            # 백트랙킹 조건 : 이미 유망(사이클 염려가 없는) 나들목 루트라면 방문 안 해도 됨 바로 True
            
            ### 중요! 재귀는 말단을 만나 재귀 과정이 종료되고 리턴문이 소환되면서
            ### 바로 위에 덮여진 상위 재귀함수의 리턴문 하부 코드를 실행시키게 된다.
            ### 이 과정이 곧 현재 탐색 과정의 기록을 초기화시킴과 동시에
            ### 전체 분기에서는 탐색의 필요성을 기록하는 과정이 된다
            
            ### 만일 visit이란 기록기가 존재하지 않으면 사이클의 판별 과정은
            ### 단순히 이미 방문된 노드를 다시 만날 경우로 판별하게 된다.
            ### DFS의 탐색 특성상 우회도로와 직선도로의 개념이 없어서 직선도로 탐색을 먼저 만나서
            ### 직선도로가 거쳐간 노드를 우회도로가 늦게 마주할 때 그곳이 이미 최종 방문 처리가 됐다면
            ### 해당 탐색은 사이클로 판명하고 오류 판정을 내리게 될 것이다
            ### 그러므로 전체 탐색 기록을 통한 백트랙킹 조건과 
            ### 현재 분기에서의 탐색 기록을 별도로 관리해야 한다
            
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
            
            
