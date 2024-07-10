# 이진 탐색
def binary_search(trees, need, minimum, maximum):
    if minimum > maximum:
        return maximum

    cut = (maximum + minimum) // 2  # 필요 나무 최대 한정 높이 계산
    total_sum = 0

    for tree in trees:
        if tree >= cut: # 나무가 커트라인 아래면 계산 x
            total_sum += tree - cut

    if total_sum >= need:
        return binary_search(trees, need, cut + 1, maximum)
    else:
        return binary_search(trees, need, minimum, cut - 1)


count, need = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
maximum = max(trees)
minimum = 0

# 뭔가 가장 짧은 나무를 min, 가장 긴 나무를 max로 두고
# 필요한 나무 길이가 이진 탐색의 대상이 될 것 같다



print(binary_search(trees, need, minimum, maximum))