# 재귀 활용해보기
# 조합의 형성 과정을 트리로 나타내면 레벨 당 한 개의 숫자가 등장
# 그 숫자가 등장한 시점에서 하위 레벨에 해당 숫자가 등장해서는 안된다
# 등장할 경우, 백트랙킹

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         result = []
        
#         # cur: 현재 숫자, visit: 방문한 숫자 리스트
#         def dfs(cur, visit):
#             # 백트랙킹
#             if len(visit) == k:
#                 # visit에 영향 안 가게 복사 객체
#                 result.append(visit[:])
#                 return
            
#             # cur부터 n까지 순회 탐색
#             for i in range(cur, n + 1):
#                 new_visit = visit + [i]
                
#                 # cur이 추가된 시점의 동일 레벨의 재귀 작업
#                 # 조합이므로 cur이 이미 방문 처리된 new_visit을 할당
#                 dfs(i + 1, new_visit)
        
#         dfs(1, [])
        
#         return result
            
        
        


# # 꼼수 1 : 순열을 전부 구하고 중복 값을 전부 배제하면 그게 곧 조합

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        
        if n == k:
            return [nums]
        
        stack = [[nums, []]] # remaining, path
        answer = []
        combination = set()
        
        while stack:
            remaining, path = stack.pop()
            
            if len(path) is k:
                path.sort()
                tuple_path = tuple(path)
                combination.add(tuple_path)
                continue

            for i in range(len(remaining)):
                # 이미 앞전의 애들은 전단계에서 훑었을 테니까 굳이 조회 필요 x 
                new_remaining = remaining[i+1:]
                new_path = path + [remaining[i]]
                
                stack.append([new_remaining, new_path])

        # 조합 산출 과정
        for item in combination:
            list_item = list(item)
            answer.append(list_item)
        
        return answer
        
        
        