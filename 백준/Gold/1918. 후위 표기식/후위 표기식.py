"""
뭔가 스택 느낌인데...
A+B -> AB+
약간 뭐 때문에 +를 스택에 넣었다가 다시 +를 스택에서 꺼내 덧붙인 그런 느낌..?

A+B*C
ABC*+ -> 얘도 + 넣고 * 넣고, 결과는 *가 먼저 나오고 그다음에 + 나오고...
A*B+C
AB*C+ -> 얘 too

식에 전부 괄호가 있다고 가정할때, 가장 바깥 괄호 기준 연산 묶음부터 스택에 먼저 넣는다
하지만 괄호가 있다면

(A+B)*C
AB+C*
얘는 오히려 위의 결과와 반대된다. 괄호가 존재하기 때문

A*(B+C)
ABC+*
얘 too

문자열 순회를 시작한다
1. 괄호 (를 마주하면 괄호가 있었다는 플래그를 세팅한다
1-1. 연산자가 나오면 스택에 넣는다
1-1. 괄호 )가 나오면 플래그를 해제하고, 바로 pop해서 덧붙인다
"""

line = input()

result = ""
stack = []

OPERATOR = ["+", "-", "*", "/"]
PM_OPERATOR = ["+", "-"]
MD_OPERATOR = ["*", "/"]

"""
이 방법은 A+B*C나 A*B+C 같은 건 커버
하지만 괄호가 있다거나 좀 더 복합된 케이스(예제1, 예제4)는 커버 x

후위표현은 묶음에서 덧뺄셈(+,-)보다 곱나눗셈(*,/)가 더 먼저 나온다 
곱나눗셈 연산자를 마주해서 스택에 쌓이다가 최초로 덧뺼셈 연산자가 마주되면 스택에서 전부 빠져야 한다
단 닫는 괄호를 만나면 무조건 내뱉는다?
"""
# 일단 괄호없는 케이스는 커버가 된 것 같은데
for element in line:

    # 변수 마주할 경우
    if element not in OPERATOR:

        # 추가) 괄호도 고려해야 할 경우
        if element == "(":
            stack.append(element)
            continue
        elif element == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop() # ( 제거
            continue

        result += element
    # 연산자 마주할 경우
    # 일단 1개의 스택으로
    # md가 pm보다 뒤에 있는 경우는 절대 없음?
    else:
        if element in MD_OPERATOR:
            if stack and stack[-1] in PM_OPERATOR:
                stack.append(element)
            elif stack and stack[-1] in MD_OPERATOR:
                while stack and stack[-1] in MD_OPERATOR:
                    result += stack.pop()
                stack.append(element)
            else:
                stack.append(element)
            continue

        if element in PM_OPERATOR:
            while stack and stack[-1] != "(": # 왠지 여기도 ( 발견하기 전까지 스택 팝 조건 추가해야될듯
                result += stack.pop()

            stack.append(element)

while stack:
    result += stack.pop()

print(result)