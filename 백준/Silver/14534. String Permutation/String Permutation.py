import sys
from collections import defaultdict


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 순열 재귀함수
def permute(strs):
    if len(strs) == 1:
        return [strs]

    result = []

    def dfs(remaining, path):
        # 백트랙킹
        if not remaining:
            result.append(path)
            return

        for i in range(len(remaining)):
            new_remaining = remaining[:i] + remaining[i + 1:]
            new_path = path + [remaining[i]]

            dfs(new_remaining, new_path)

    dfs(strs, [])

    return result


# 입력 처리
cases = int(sys_input())
cases_map = defaultdict(dict)

for i in range(cases):
    strs = [char for char in sys_input()]
    str_cases = permute(strs)

    cases_map[i] = str_cases

for i in range(cases):
    introduce = f"Case # {i + 1}:"

    print(introduce)
    for item in cases_map[i]:
        result_str = "".join(map(str, item))
        print(result_str)



