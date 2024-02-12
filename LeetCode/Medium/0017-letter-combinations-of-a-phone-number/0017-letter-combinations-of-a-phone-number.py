# 재귀 리팩토링
class Solution:    
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        result = []
        
        if not digits:
            return result
        
        def dfs(index, path):
            # 백트랙킹
            if len(path) == len(digits):
                result.append(path)
                return
            
            # index부터 마지막까지 숫자들 전부 순회
            for idx in range(index, len(digits)):
                # 딕셔너리에 있는 해당 인덱스의 숫자가 지닌 문자들 전부 순회
                for el in dictionary[digits[idx]]:
                    # 다음 인덱스, 문자열 이어붙이고 재귀
                    dfs(idx + 1, path + el)
            
        dfs(0, '')
        
        return result


# class Solution:    
#     def letterCombinations(self, digits: str) -> List[str]:
#         dictionary = {
#             '2': ['a', 'b', 'c'],
#             '3': ['d', 'e', 'f'],
#             '4': ['g', 'h', 'i'],
#             '5': ['j', 'k', 'l'],
#             '6': ['m', 'n', 'o'],
#             '7': ['p', 'q', 'r', 's'],
#             '8': ['t', 'u', 'v'],
#             '9': ['w', 'x', 'y', 'z']
#         }
        
#         result = []
        
#         if not digits:
#             return result
        
#         stack = [''] # 스택 초기화
        
#         while stack:
#             curr = stack.pop()  # 스택에서 현재 문자열들 팝
            
#             # 현재 조합의 길이가 숫자의 길이와 같으면 result에 추가
#             if len(curr) == len(digits):  
#                 result.append(curr)
#                 continue 
#                 # 현재 반복 중지, 곧바로 다음 순회로 가도록
#                 # 다음 단계는 다른 첫 번째 문자에 대해 이어붙이기 작업
            
#             # 다음 인덱스 업데이트
#             idx = len(curr) 
            
#             # 다음 인덱스의 숫자에 해당하는 문자들 전부 순회
#             for char in dictionary[digits[idx]]:  
#                 combination = curr + char
#                 stack.append(combination)  # 스택에 추가
        
#         return result
