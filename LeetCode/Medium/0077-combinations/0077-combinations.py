# 꼼수 1 : 순열을 전부 구하고 중복 값을 전부 배제하면 그게 곧 조합

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
        
        
        