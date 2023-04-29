import random # 랜덤
import img1 # 이미지 파일
import word_list # 단어 파일

print(img1.logo) # hangman 로고 이미지

life = 6 # 틀렸을때 게임을 끝내기 위해 수명 지정

choice_word = random.choice(word_list.word) # random모듈을 사용하여 단어파일에 있는 단어를 랜덤하게 하나 뽑음

display = [] # 랜덤으로 선택된 단어가 몇글자인지 표시하기 위해 지정
for i in range(len(choice_word)):
  display += '_'
print(display) # for 반복문을 사용하여 '_'로 몇글자 단어인지 표시하여 보여줌

end_of_game = False # while 반복문을 위해 준비된 변수
while not end_of_game: 
  put_word = input('생각나는 알파벳을 작성하세요 : ').lower() # 상대방이 단어를 적는 부분

  for position in range(len(choice_word)): # for 반복문을 이용하여 put_word에 적은 단어가 맞는다면 '_'를 put_word로 바꿔주는 과정
    if choice_word[position] == put_word:
      display[position] = put_word

  if put_word not in choice_word: # if 조건문을 통해 put_word에 적은 알파벳이 들어있지 않으면 "땡"을 출력하고 초기 생명을 -1 감소시키면서 생명이 0이되면 게임도 끝나게 설정
    life = life - 1
    print("떙")
    if life == 0:
      end_of_game = True
      print("넌 졌어...")

  print(display)

  if "_" not in display: # 모든 단어를 맞추면 승리를 표시하기 위해 if 조건문 사용
    end_of_game = True
    print("너의 승리야!")

  print(img1.stages[life]) # life를 잃을때마다 행맨게임의 교수형 이미지를 하나씩 생성
