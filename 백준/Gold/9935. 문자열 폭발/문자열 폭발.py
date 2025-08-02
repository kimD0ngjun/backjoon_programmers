s = input()
ex = input()

"""
연결리스트? -> 삭제는 빠르지만, 일련의 삭제는 너무 복잡하고 느릴듯
스택? -> 폭발 문자열의 역순 pop?
"""

stack = []

for ch in s:
    # temp = [] # 복구용 배열
    stack.append(ch)

    # 문자 잘 쌓다가 폭발 문자열의 마지막 문자를 발견했다
    # 그냥 바로 여기서 스택이 더 빠르게 비워진 상황을 조건분기시킨다면 밑의 추가 검증 불필요할듯
    if ch == ex[-1] and len(stack) >= len(ex):

        # 인덱스로 접근하는 것과 직접 pop하면서 접근하는 것의 시간차?
        # 직접 팝하나, 결국 팝카운트가 누적되면서 O(n)으로 똑같
        if ''.join(stack[-len(ex):]) == ex:
            for _ in range(len(ex)):
                stack.pop()

print(''.join(stack) if stack else "FRULA")