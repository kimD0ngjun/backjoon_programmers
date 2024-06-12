"""
https://www.acmicpc.net/problem/16637
"""

# 입력 처리
N = int(input())
question = input()


# 1. 괄호는 두 숫자만 묶을 수 있다
# ex) (1+2) --> ok || (1+2+3) --> no

# 2. 괄호를 사용하지 않아도 된다

# 3. 중첩 괄호는 쓸 수 없다
# ex) ((8×7)-9)×2 --> no

"""
문자열 인덱스 순서대로 괄호를 넣을지, 안 넣을지 탐색
-> 케이스별로 분기를 추가하면서 그 당시의 결과를 계속 기억해야 함
-> DFS 사용하기?
"""



def operation(num_a, op, num_b):

    if op == "+":
        return num_a + num_b

    if op == "-":
        return num_a - num_b

    if op == "*":
        return num_a * num_b


# 인덱스가 0, 2, 4, 6... 2n의 위치에는 숫자가 존재
# (1) 두 개만을 계산하면 결국 괄호 계산과 같고
# (2) 세 개를 계산하는 방법은 () ? ? || ? ? ()
# 내가 고려할 부분은 ? ? () 이거 즉, i + 2부터 계산하고 i 계산

# 변수 전역화만이 방법뿐인가... 흠
answer = -2**31

def dfs(i, result):
    global answer

    if i >= N - 1:
        answer = max(answer, result)
        return

    # 케이스 (1)
    num_a = result
    op = question[i + 1]
    num_b = int(question[i + 2])

    next_result = operation(num_a, op, num_b)
    dfs(i + 2, next_result)

    # 케이스 (2)
    if i + 4 < N:
        num_b = int(question[i + 2])
        op2 = question[i + 3]
        num_c = int(question[i + 4])

        inner_result = operation(num_b, op2, num_c)
        next_result = operation(result, question[i + 1], inner_result)

        dfs(i + 4, next_result)


dfs(0, int(question[0]))

print(answer)


