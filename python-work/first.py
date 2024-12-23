# 1. 준비(변수 준비)
number1 = 0 # 첫번째 숫자 저장 변수
number2 = 0 # 두번째 숫자 저장 변수
op = '' # 연산자 저장 변수
result = 0 # 결과값 저장 변수

# 프로그램 타이틀 출력
print('간단한 계산기')

# 2. 입력
#   첫번째 숫자를 입력받아서 저장
number1 = input('첫번째 숫자 입력 : ')
#   연산자를 입력받아서 저장
op = input('연산자를 입력하세요 (+, -, *, /) : ')
#   두번째 숫자를 입력받아서 저장
number2 = input('두번째 숫자 입력 : ')

# 3. 연산 처리
#   정수로 입력값을 변경
number1 = int(number1)
number2 = int(number2)
#   입력한 산술연산자에 따라 분기
if op == '+':
    result = number1 + number2
elif op == '-':
    result = number1 - number2
elif op == '*':
    result = number1 * number2
elif op == '/':
    if number2 == 0:
        result = '0으로 나눌 수 없습니다.'
    else:        
        result = number1 / number2
else:
    result = '잘못된 연산자입니다.'

# 3. 결과 값을 출력
print('결과 : ', result)
