import art
import random
import os

def easy(): # 쉬운버전 함수
  i = 0
  while i < 10: # 기회가 5번이라 5번 반복하는 반복문 1
    user_choice = int(input("숫자를 입력하세요 - "))
    if user_choice == computer_choice:
      print("맞췄습니다!!! 당신의 승리\n\n")
      print(art.win)
      break
    elif user_choice < computer_choice:
      print("땡!! 숫자가 작아요 Up!!Up!!")
      i += 1
    else:
      print("땡!! 숫자가 커요. Down>>Down>>")
      i += 1
  if i == 10:
    print("횟수를 다썼습니다. 당신의 패배 ㅠㅠ\n\n")
    print(art.lose)

def hard(): # 어려운버전 함수
  i = 0
  while i < 5: # 기회가 5번이라 5번 반복하는 반복문 2
    user_choice = int(input("숫자를 입력하세요 - "))
    if user_choice == computer_choice:
      print("맞췄습니다!!! 당신의 승리\n\n")
      print(art.win)
      break
    elif user_choice < computer_choice:
      print("땡!! 숫자가 작아요 Up!!Up!!")
      i += 1
    else:
      print("땡!! 숫자가 커요. Down>>Down>>")
      i += 1
  if i == 5:
    print("횟수를 다썼습니다. 당신의 패배 ㅠㅠ\n\n")
    print(art.lose)

numbers=[] # 1 부터 100까지 숫자를 넣기위한 리스트 & 반복문
for i in range(1,101):
  numbers.append(i)

game_choice = True # 게임을 계속 할지 정해놓은 변수

while game_choice:
  computer_choice = int(random.choice(numbers)) # 랜덤하게 1~100까지 한가지 숫자를 골라줌
  print(art.log)
  print("\n\n\n1~100까지 숫자를 맞춰주세요!!")

  # 난이도 선택으로 미리 만들어 놓은 함수를 끌고옴
  version = input("쉬운 버전(기회 10번)은 'easy'를 어려운 버전(기회 5번)은 'hard'를 입력해주세요.(easy/hard) - ").lower()
  if version == 'easy':
    easy()
  else:
    hard()
  
  # 게임을 계속 플레이하거나 종료하기 위해 만든 조건문
  user_game_choice = input("게임을 더 하시겠습니까?(y/n) - ").lower()
  if user_game_choice == 'y':
    os.system('cls')
    game_choice = True
  else:
    game_choice = False