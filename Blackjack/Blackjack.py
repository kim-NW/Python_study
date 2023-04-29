import random # 랜덤하게 카드를 분배하기 위해 사용
import os # 새로운 게임을 하기위해 사용
import art

def deal_card(): # 카드를 랜덤하게 분배하기 위해 만든 함수
  """ 데크에서 임의 카드를 반환"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10]
  card = random.choice(cards)
  return card

def calculate_score(cards): # 블랙잭과 카드를 합쳤을때 21이 초과가 되면 게임이 바로 종료 될 수 있게 만들고 점수를 구하기 위해 만든 함수
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) >21:
    cards.remove(11)
    cards.append(1)
    
  return sum(cards)

def play_game(): # 블랙잭 게임을 계속 돌리기 위해 함수화

  print(art.logo)
  
  user_cards=[]
  computer_cards=[]
  is_game_over = False

  def compare(user_score, computer_score): # 플레이어와 딜러의 점수를 합산하여 결과를 나타내주는 함수
    if user_score == computer_score:
      return "무승부!!!!"
    elif computer_score == 0:
      return "너의 패배ㅋㅋㅋ"
    elif user_score == 0:
      return "플레이어 승!!!!!! 축하축하"
    elif user_score > 21:
      return "합계 초과로 너의 패배!!!ㅋㅋㅋㅋ"
    elif computer_score > 21:
      return "딜러 합계 초과로 플레이어 승!!! 축하축하"
    elif user_score > computer_score:
      return "플레이어 승!!!! 축하축하"
    else:
      return "너의 패배 키득키득~~"

  for _ in range(2): # 게임시작시 플레이어와 딜러에게 2장의 카드 배분을 해주기 위한 for문
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over: 
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  플레이어 카드 : {user_cards}, 현재 점수 : {user_score}")
    print(f"  딜러 첫번째 카드 : {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21: # 블랙잭일 경우 바로 종료되게하는 조건문
      is_game_over = True
    else:
      user_card_chocie = input("카드를 한장 더 받고싶으면 'y' 이대로 멈추겠으면 'n'을 입력해주세요.(y/n)").lower() 
      if user_card_chocie == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score !=0 and computer_score < 17: # 컴퓨터가 블랙젝이 아닌 상태에서 두장의 카드의 합이 17미만일 경우 자동으로 한장 더 받게 하는 시스템
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"플레이어의 최종 카드는 : {user_cards}, 플레이어의 최종 점수는 : {user_score}")
  print(f"딜러의 최종 카드는 : {computer_cards}, 딜러의 최종 점수는 : {computer_score}")
  print(compare(user_score, computer_score))

while input("게임을 계속 하시고 싶으시면 'y'를, 종료하고 싶으시면 'n'을 입력해주세요 : ").lower() == 'y':
  os.system('cls')
  play_game()