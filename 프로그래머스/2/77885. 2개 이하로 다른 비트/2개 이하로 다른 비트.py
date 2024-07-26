# 10진법 -> 2진법
def bina(n):
    return bin(n)[2:]

# 2진법 -> 10진법
def deci(b):
    return int(b, 2)

def solution(numbers):
    answers = []

    for number in numbers:
        # 각 숫자를 2진법 문자열로 변환
        bin_str = bina(number)

        # "1"일 경우
        if bin_str == "1":
            answers.append(2)
            continue

        # 맨 마지막 인덱스가 0일 경우, 그냥 그걸 1로 바꾸기
        if bin_str[-1] == "0":
            answer = bin_str[:-1] + "1"
            answers.append(deci(answer))
            continue

        # 아닌 케이스일 경우?
        """
        ex) 전부 1로 구성
        0001 : 0010
        0011 : 0101
        0111 : 1011
        01111 : 10111
        => 맨 앞의 1을 0으로 바꾸고, 그 앞에 1 붙이면 됨

        ex) 기타 등등
        101 : 110
        1001 : 1010
        10001 : 10010
        => 역순에서 처음 등장하는 1과 그 앞의 0을 바꾸기

        1011 : 1101
        1010111 : 1011011

        => 결국 역순으로 훑었을 때 처음 등장하는 01을 10으로 바꾸는 거 아닌가?
        """

        # 아닌 케이스일 경우
        index = len(bin_str) - 1

        # 11111 같은 케이스 제외하고 중간에 0 있는 경우
        while index > 0:
            if bin_str[index] == "1":
                if bin_str[index - 1] == "1":
                    index -= 1
                    continue

                bin_list = list(bin_str)
                bin_list[index] = "0"
                bin_list[index - 1] = "1"

                answer = "".join(bin_list)
                answers.append(deci(answer))
                break
            index -= 1

        # 루프가 끝나도 처리되지 않은 경우,
        # 예를 들면 111 같은 경우 맨 앞의 1을 0으로 바꾸고 앞에 1 덧붙이기
        if index == 0:
            bin_list = list(bin_str)
            bin_list[0] = "0"
            temp = "".join(bin_list)

            answer = "1" + temp
            answers.append(deci(answer))

    return answers