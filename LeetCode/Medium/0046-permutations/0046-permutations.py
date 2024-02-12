# 재귀

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        result = []

        def dfs(remaining, path):
            # 백트랙킹
            if not remaining:
                result.append(path)
                return
            
            for i in range(len(remaining)):
                new_remaining = remaining[:i] + remaining[i+1:]
                new_path = path + [remaining[i]]
                
                dfs(new_remaining, new_path)
        
        dfs(nums, [])
        
        return result

# :는 파이썬에서 리스트의 슬라이싱(slice)을 사용하는 문법

# # 모든 요소들이 서로의 이웃이 되는 완벽한 그래프 구조
# # 즉 모든 요소들을 순회탐색하면 그게 곧 순열

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) is 1:
#             return [nums]
        
#         stack = [[nums, []]] # remaining, path
#         result = []

#         while stack:
#             # 스택에서 팝한 걸 두 변수에 할당
#             # remaining : 아직 순회 안 된 요소
#             # path : 현재까지 탐색한 요소
#             remaining, path = stack.pop()
            
#             # 백트랙킹(한 바퀴 완료한 순회가 헛돌지 않게)
#             if not remaining:
#                 result.append(path)
#                 continue

#             # 남아있는 요소들 있으면 그것들 순회
#             for i in range(len(remaining)):
#                 # `0부터 i-1까지` + `i+1번째 요소부터 마지막 요소까지`
#                 # 즉, i번째 요소를 뺀 나머지 요소들을 포함시킨 remaining 반환
#                 # remaining을 변환시키지 않는 문법이니 꼭 익혀둘 것
#                 new_remaining = remaining[:i] + remaining[i+1:]
                
#                 # 기존 루트에 새로운 요소 할당
#                 # 이것 역시 기존의 path 변화시키지 않음
#                 new_path = path + [remaining[i]]
                
#                 # 이렇게 변환시키지 않으려는 이유는 반복문 순회 때문
#                 stack.append([new_remaining, new_path])

#         return result

# # :는 파이썬에서 리스트의 슬라이싱(slice)을 사용하는 문법

