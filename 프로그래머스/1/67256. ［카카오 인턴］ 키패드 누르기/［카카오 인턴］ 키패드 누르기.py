import math

# 키패드 좌표 정의
vertexs = {
    1: [0, 0], 2: [0, 1], 3: [0, 2],
    4: [1, 0], 5: [1, 1], 6: [1, 2],
    7: [2, 0], 8: [2, 1], 9: [2, 2],
    "*": [3, 0], 0: [3, 1], "#": [3, 2]
}

def distance(one_position, another_position):
    y1, x1 = one_position
    y2, x2 = another_position
    return abs(y2 - y1) + abs(x2 - x1)

def solution(numbers, hand):
    answer = ''
    left_position = vertexs["*"]
    right_position = vertexs["#"]

    for number in numbers:
        if number in [1, 4, 7]:
            left_position = vertexs[number]
            answer += 'L'
        elif number in [3, 6, 9]:
            right_position = vertexs[number]
            answer += 'R'
        else:
            position = vertexs[number]
            left_dist = distance(left_position, position)
            right_dist = distance(right_position, position)

            if left_dist < right_dist:
                left_position = position
                answer += 'L'
            elif right_dist < left_dist:
                right_position = position
                answer += 'R'
            else:
                if hand == 'left':
                    left_position = position
                    answer += 'L'
                else:
                    right_position = position
                    answer += 'R'

    return answer