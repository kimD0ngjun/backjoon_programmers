# - 뒤의 숫자들이 전부 +일 때, 걔네를 전부 괄호 씌워서 -로 바꾸기

# 입력 단계
expression = str(input())

# 정답 산출
# -식 기준으로 구별해서 전부 분리하기
no_minus = expression.split('-')
answer = 0

# 문자열의 인덱스 0이 -라면 첫 번째 수 혹은 수식은 전부 감산해야 함
if expression[0] == '-':
    answer -= sum(map(int, (no_minus[0].split('+'))))
else:
    answer += sum(map(int, (no_minus[0].split('+'))))


# 첫 번째 작업 이후의 작업(객체 복사)
for x in no_minus[1:]:
    answer -= sum(map(int, (x.split('+'))))


print(answer)