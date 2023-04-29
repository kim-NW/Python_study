import main
machine = True

for i in main.MENU:
    a = main.MENU[i]
    print(a["ingredients"])


# def black(machine):
#     if main.resources['water'] - 50 > 0 and main.resources['coffee'] - 18 > 0:
#         main.resources['water'] -= 50
#         main.resources['coffee'] -= 18
#         print("150원 입니다 손님")
#         a = int(input("10원짜리 동전 몇개 넣으십니까? ")) * 10
#         b = int(input("50원짜리 동전 몇개 넣으십니까? ")) * 50
#         c = int(input("100원짜리 동전 몇개 넣으십니까? ")) * 100
#         d = int(input("500원짜리 동전 몇개 넣으십니까? ")) * 500
#         sum = a+b+c+d
#         if sum > 150:
#             change = sum - 150
#             print(f"거스름 돈 {change} 드리겠습니다.")
#             print("잠시만 기다려주세요~ 커피 준비중입니다.")
#             print("맛있게 드세요!!")
#             main.profit += 150
#         else:
#             print(f"금액이 부족합니다. {sum}원이 반환됩니다.")
#             pass
#     else:
#         print("죄송합니다... 재료가 부족합니다.")
#         machine = False


# def milk(machine):
#     if main.resources['water'] - 50 > 0 and main.resources['coffee'] - 24 > 0 and main.resources['milk'] - 100 > 0:
#         main.resources['water'] -= 50
#         main.resources['coffee'] -= 24
#         main.resources['milk'] -= 100
#         print("250원 입니다 손님")
#         a = int(input("10원짜리 동전 몇개 넣으십니까? ")) * 10
#         b = int(input("50원짜리 동전 몇개 넣으십니까? ")) * 50
#         c = int(input("100원짜리 동전 몇개 넣으십니까? ")) * 100
#         d = int(input("500원짜리 동전 몇개 넣으십니까? ")) * 500
#         sum = a+b+c+d
#         if sum > 250:
#             change = sum - 250
#             print(f"거스름 돈 {change} 드리겠습니다.")
#             print("잠시만 기다려주세요~ 커피 준비중입니다.")
#             print("맛있게 드세요!!")
#             main.profit += 250
#         else:
#             print(f"금액이 부족합니다. {sum}원이 반환됩니다.")
#             pass
#     else:
#         print("죄송합니다... 재료가 부족합니다.")


# def cream(machine):
#     if main.resources['water'] - 70 > 0 and main.resources['coffee'] - 24 > 0 and main.resources['milk'] - 80 > 0:
#         main.resources['water'] -= 70
#         main.resources['coffee'] -= 24
#         main.resources['milk'] -= 80
#         print("300원 입니다 손님")
#         a = int(input("10원짜리 동전 몇개 넣으십니까? ")) * 10
#         b = int(input("50원짜리 동전 몇개 넣으십니까? ")) * 50
#         c = int(input("100원짜리 동전 몇개 넣으십니까? ")) * 100
#         d = int(input("500원짜리 동전 몇개 넣으십니까? ")) * 500
#         sum = a+b+c+d
#         if sum > 300:
#             change = sum - 300
#             print(f"거스름 돈 {change} 드리겠습니다.")
#             print("잠시만 기다려주세요~ 커피 준비중입니다.")
#             print("맛있게 드세요!!")
#             main.profit += 150
#         else:
#             print(f"금액이 부족합니다. {sum}원이 반환됩니다.")
#             pass
#     else:
#         print("죄송합니다... 재료가 부족합니다.")
#         machine = False

# #coin
# while coin>0:
#     판별식 =>
#     user_choice = input("무엇을 드시겠습니까? (블랙커피, 밀크커피, 크림커피) ")
#     if user_choice == "off":
#         machine = False
#     elif user_choice == "report":
#         print(main.profit)
#         print(main.resources)
#     elif user_choice == "블랙커피":
#         black()
#     elif user_choice == "밀크커피":
#         milk()
#     elif user_choice == "크림커피":
#         cream()
#     print(f"재료는 {main.resources}만큼 남았습니다.")
# print(f"총 수입은 {main.profit}입니다.")
