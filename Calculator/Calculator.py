import os # 계산하던 식이 끝나면 지우기 위해 불러온 os
import art # 로고 그림 불러오기

#Add - 더하기 함수
def add(n1, n2):
  return n1 + n2

#Subratct - 빼기 함수
def Subratct(n1, n2):
  return n1 - n2

#Multiply - 곱하기 함수
def Multiply(n1, n2):
  return n1 * n2

#Divide - 나누기 함수
def Divide(n1, n2):
  return n1 / n2

operations = { # dictionary로 key:value 값을 만들어 사칙연산을 선택하면 바로 함수를 불러올 수 있음
  "+":add,
  "-":Subratct,
  "*":Multiply,
  "/":Divide
}

def calcuratior(): # 함수를 계속 돌리기 위해 전체를 묶어줄 함수
  print(art.logo)
  num1 = float(input("계산하고 싶은 숫자를 입력하세요 : "))
  for symbol in operations: # 사칙연산을 보여주기 위한 for 반복문
    print(symbol)
  should_continue = True # while문을 계속 돌리기 위한 변수 설정
  while should_continue:
    operations_symbol = input("구하고 싶은 연산자를 선택하세요 - ")
    num2 = float(input("계산하고 싶은 다음 숫자를 입력하세요 : ")) # 소수까지 계산하기 위해 int대신 float로 설정
    calculator_function = operations[operations_symbol] # 선택한 사칙연산을 통해 dictionary에서 함수를 실행
    answer = calculator_function(num1,num2)
    print(f"{num1} {operations_symbol} {num2} = {answer}")
    if input(f"{answer}을 더 계산하고 싶으시면 'y'를 그만하고 싶으시면 'n'을 입력해주세요 - ").lower() == 'y':
      num1 = answer # 구한 수를 더 계산하고 싶을때 계산한 수를 저장하기 위해 설정
    else:
      should_continue = False
      os.system('cls') # 여태 계산했던 식을 다 지우고 처음부터 시작하기 위해 설정
      calcuratior() # 함수의 재귀를 위해 설정

calcuratior()