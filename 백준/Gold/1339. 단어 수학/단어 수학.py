"""
https://www.acmicpc.net/problem/1339
"""

# 입력
N = int(input())

# 입력된 단어 및 그 길이를 튜플로 받아두기
# 강타입 언어에서는 어떻게 할 수 있으려나
words = []

for _ in range(N):
    word = input()
    words.append((word, len(word)))

"""
최선의 선택: 자릿수가 높은 곳에 위치한 알파벳에게 최대 수를 부여하기
자릿수가 큰 것의 기준 이전에 단어의 길이가 긴 것부터 앞에서 먼저 배치 시작
"""

# 길이 기준으로 내림차순 정렬 후, 길이 차이만큼의 절댓값으로 매핑
# 이 절댓값이 인덱스 기준 시작점 지표로 활용될 예정
words.sort(key=lambda x: x[1], reverse=True)

max_len = words[0][1]
words = [[word, abs(length - max_len)] for word, length in words]

# print(words)

# 알파벳 - 숫자 딕셔너리 초기화
num_dict = {}

# 연산
for i in range(max_len):
    # 자릿수 = max_len - i - 1
    digit = 10 ** (max_len - i - 1)

    # 전체 요소를 순회해서 abs(length - max_len) 보다 작거나 같은 애들부터 맨 앞자리에서 문자 배치 시작
    for element in words:
        # 단어, 인덱스 지표, 지속적으로 업데이트 되는 숫자 담을 변수
        word, standard = element

        # 인덱스 지표보다 현재 인덱스가 작다면 아직 수 할당 순서 x
        if standard > i:
            continue

        # 인덱스 지표를 기준으로 각 단어의 현재 인덱스 계산
        index = i - standard

        # 해당 인덱스에 위치한 단어의 알파벳 추출
        alphabet = word[index]

        if alphabet in num_dict:
            num_dict[alphabet] += digit
        else:
            num_dict[alphabet] = digit

# print(words)

# 정답 연산
# print(num_dict)
sorted_num_dict = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)

integer = 9  # 숫자는 9부터 시작(가장 큰 값 기준)
answer = 0  # 정답 변수

for _, value in sorted_num_dict:
    # print(str(key) + ": " + str(value))
    answer += value * integer
    integer -= 1

print(answer)

"""
틀렸네... 반례

10
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB
output: 1780(A=9, B=8)
answer: 1790(A=8, B=9)

자릿수의 영향력?
알파벳이 구성하고 있는 자릿수의 총 합을 구하고 그것들 중 가장 큰 값부터 차례대로 9, 8, 7... 할당?
"""

