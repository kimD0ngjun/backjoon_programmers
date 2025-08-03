T = int(input())
result = []

"""
역순정렬은 너무 리소스가 크다...
그냥 방향을 추적하는 식으로? 인덱스 0이거나 인덱스 -1이거나

1. R울 카운팅한다
2. R이 입력될 때마다 pop()과 popleft()를 번갈아 처리한다.
3. 1번에 따른 R의 갯수가 홀수면 그때는 reverse 호

문자열을 배열로 처리하지 않고, 문자열 내에서 처리를 하는 게 핵심일듯
left = 0, right = 길이 입력값 - 1
count % 2 == 0 and "D" -> popleft += 1
count % 2 == 1 and "D" -> pop += 1
"""

for _ in range(T):
    par = input()
    n = int(input())
    arr = input() # "[]". "[1]", "[1, 2, 3]"

    R_count = 0
    D_count = 0

    # arr == "[1, 2]" 용도
    left = 0
    right = n - 1

    for f in par:
        if f == "R":
            R_count += 1
        elif f == "D":
            D_count += 1

            if R_count % 2 == 0:
                left += 1
            else:
                right -= 1

    # arr == "[]"
    if n == 0:
        if D_count > 0:
            result.append("error")
            continue
        else:
            result.append("[]")
            continue

    # arr == "[1]"
    if n == 1:
        if D_count > 1:
            result.append("error")
            continue
        elif D_count == 1:
            result.append("[]")
            continue
        elif D_count == 0:
            result.append(arr)
            continue

    # arr = "[1, 2 ...]"
    # 여기서의 left와 right는 몇 번째 인덱스까지
    if left > right + 1:
        result.append("error")
        continue

    sub_list = arr[1:-1].split(",")
    sub_list = sub_list[left:right + 1]

    if R_count % 2 == 1:
        sub_list.reverse()

    result.append("[" + ",".join(sub_list) + "]")

print(*result, sep="\n")