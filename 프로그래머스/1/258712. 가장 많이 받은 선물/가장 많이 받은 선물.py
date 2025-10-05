# https://school.programmers.co.kr/learn/courses/30/lessons/258712
"""
1. 두 사람( A,B ) 서로 선물을 주고받은 수의 차( abs(gift(A, B) - gift(B, A)) )가 0이 아님
더 많이 선물 준 사람( max(gift(A, B), gift(B, A)) )이 다음달 상대에게서 선물 get

2. 두 사람( A,B ) 서로 선물을 주고받은 수의 차( abs(gift(A, B) - gift(B, A)) )가 0
선물지수( gift(A, all) - gift(all, A) )를 비교해서 더 큰 사람이 다음달 상대에게서 선물 get
2-1. 만약 선물지수도 같다면 다음달 선물 주고받는 거 없음

Q. 그래서 누가 다음달에 선물 제일 많이 받을까요??
"""
from collections import defaultdict

class User:
    def __init__(self, name):
        self.name = name
        self.give = defaultdict(int) # 그 사람에게 선물 줌
        self.receive = defaultdict(int) # 그 사람에게 선물 받음
        self.gift_idx = 0 # 선물 지수

    def give_gift(self, friend):
        self.give[friend] += 1
        friend.receive[self] += 1

        self.gift_idx += 1
        friend.gift_idx -= 1

def solution(friends, gifts):
    users = defaultdict(User)
    for name in friends:
        users[name] = User(name)

    for gift in gifts:
        a, b = gift.split()
        users[a].give_gift(users[b])

    # print(users)
    results = defaultdict(int)

    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            a = users[friends[i]]
            b = users[friends[j]]

            a_to_b = a.give.get(b, 0)
            b_to_a = b.give.get(a, 0)

            if a_to_b != b_to_a:
                if a_to_b > b_to_a:
                    results[a] += 1
                else:
                    results[b] += 1
            else:
                if a.gift_idx > b.gift_idx:
                    results[a] += 1
                elif a.gift_idx < b.gift_idx:
                    results[b] += 1
    
    answer = 0
    if results:
        answer = max(results.values())

    return answer

# print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
# print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
