def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])

    standard = 0
    for target in targets:
        if target[0] >= standard:
            answer += 1
            standard = target[1]

    return answer