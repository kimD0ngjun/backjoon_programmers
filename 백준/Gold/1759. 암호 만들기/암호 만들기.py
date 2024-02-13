import sys

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 백트랙킹 조건?
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음 + 길이

# dfs 함수(정렬된 문자 리스트 매개값)
def dfs(char_list, length):
    stack = [[char_list, '']] # remaining, current_string
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
        
    while stack:
        remaining, current_string = stack.pop()
        vowel_count = sum(1 for char in current_string if char in vowels)
            
        if len(current_string) == length and 1 <= vowel_count <= len(current_string) - 2:
            result.append(current_string)
            continue

        for i in range(len(remaining)):
            # 이미 앞전의 애들은 전단계에서 훑었을 테니까 굳이 조회 필요 x 
            new_remaining = remaining[i+1:]
            new_current_string = current_string + remaining[i]
                
            stack.append([new_remaining, new_current_string])

    return result

# 입력 처리
input_data = sys_input()
string_length, char_kind = map(int, input_data.split())

char_list = sys_input().replace(" ", "")
sorted_char_list = sorted(char_list)

result = dfs(sorted_char_list, string_length)

for string in sorted(result):
    print(string)