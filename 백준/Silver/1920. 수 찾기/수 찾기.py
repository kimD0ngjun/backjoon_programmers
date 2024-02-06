import sys

question_len = int(input())
question_serial = sys.stdin.readline()
question = list(question_serial.split())

answer_len = int(input())
answer_serial = sys.stdin.readline()
answer = list(answer_serial.split())

# set 구조로 교집합 계산
set_question = set(question)
set_answer = set(answer)

intersection = set_question & set_answer

for i in answer:
    if i in intersection:
        print(1)
    else:
        print(0)
