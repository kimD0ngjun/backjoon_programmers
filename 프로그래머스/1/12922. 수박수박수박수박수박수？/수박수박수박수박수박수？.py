def solution(n):
    count = n // 2
    # print(count)

    if n % 2 == 0:
        answer = '수박' * count
        # print("짝수: " + answer)
    else:
        answer = '수박' * count + '수'
        # print("홀수: " + answer)

    return answer