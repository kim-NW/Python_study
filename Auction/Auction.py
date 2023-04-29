import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(
    f"\n\n\n경매 시작!!!!!!\n {logo} \n\n\n                        탕!!탕!!탕!!\n\n\n\n")

dit = {}
max_num = 0
win_people = ''
anypeople = '예'
while not anypeople == '아니요':
    name = input("경매에 참여한 성명을 입력해 주세요 : ")
    money = input("낙찰 금액을 입력해 주세요 : ")
    dit[name] = money
    anypeople = input("경매에 참여하는 사람이 또 있나요? (예/아니요) - ")
    if anypeople == '예':
        os.system('cls')
    else:
        for i in dit:
            if max_num < int(dit[i]):
                max_num = int(dit[i])
                win_people = i
        print(f"\n\n\n축하합니다!!!! 경매 낙찰자는 {win_people}입니다.!!!!!!!!!!!!!!")
