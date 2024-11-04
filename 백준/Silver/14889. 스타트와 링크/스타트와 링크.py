import sys

N = int(input())

ability = [[0] * (N + 1)]
members = []

for i in range(1, N + 1):
    members.append(i)
    line = list(map(int, input().split()))
    ability.append([0] + line)

# print(members)
# print(ability)

gap = sys.maxsize


def backtrack(team_A, team_B, start, ability_a, ability_b):
    global gap

    if len(team_A) == N // 2 and len(team_B) == N // 2:
        # print("------")
        # print("팀A:", team_A)
        # print("팀B:", team_B)
        # print("해당 팀 차이:", abs(ability_a - ability_b))
        # print("------")

        gap = min(gap, abs(ability_a - ability_b))
        return

    # 팀 A에 멤버 추가
    if len(team_A) < N // 2:
        next_member = start
        new_ability_a = ability_a

        for member in team_A:
            new_ability_a += ability[member][next_member] + ability[next_member][member]

        team_A.append(next_member)
        backtrack(team_A, team_B, start + 1, new_ability_a, ability_b)
        team_A.pop()

    # 팀 B에 멤버 추가
    if len(team_B) < N // 2:
        next_member = start
        new_ability_b = ability_b

        for member in team_B:
            new_ability_b += ability[member][next_member] + ability[next_member][member]

        team_B.append(next_member)
        backtrack(team_A, team_B, start + 1, ability_a, new_ability_b)
        team_B.pop()


backtrack([], [], 1, 0, 0)
print(gap)
