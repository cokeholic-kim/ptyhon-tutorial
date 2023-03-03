# ex05_random.py
# import 모듈 불러오기

import random 
# random() 0.0~1.0 사이의 난수값을 반환
# randint(start,end) start ~ end 정수 랜덤 값을 반환 
num = random.random()
print(num)
# randint (start,end) start ~ end 정수 랜덤 값을 반환
num2 = random.randint(1,5)
print(num2)

# 평균구하기 
# [70,60,55,75,95,90,80,80,85,100]
# for문을 사용하여 A학급의 평균 점수를 구해보자
# len(리스트) --> 리스트길이
score = [70,60,55,75,95,90,80,80,85,100]
count = 0
average = 0
for i in score :
    average += i
    count +=1
print('점수총합 %d 명수 %d 평균 %d' %(average,count,average/count))
# * 출력 
# *
# **
# ***
number1 = 1
number2 = 10
while number1 < number2 :
    while number2 > number1:
        print(number2 * " ",number1 * '*')
        number1 += 1
    


# 가위바위보 게임 만들기.
# 가위 바위 보 중 하나를 입력받고 컴퓨터는 랜덤으로 가위,바위,보 중 하나를 지정하고
# 누가 이겼슨지 출력
# while 1:
#     human = input("가위 바위 보 중의 하나를 입력하세요 :")
#     if human == "그만" :
#         break
#     rand = random.randint(1,3)
#     computer = ""
#     if rand == 1:
#         computer = "가위"
#     elif rand == 2:
#         computer = "바위"
#     else :
#         computer = "보"
#     if human != "가위" and human != "바위" and human != "보":
#         print("잘못입력하셨습니다")
#     else:
#         if human == "가위" :
#             if computer == "가위":
#                 print(computer)
#                 print("비겼습니다")
#             elif computer == "바위":
#                 print(computer)
#                 print("졌습니다")
#             elif computer == "보":
#                 print(computer)
#                 print("이겼습니다")
#         elif human == "바위" :
#             if computer == "바위":
#                 print(computer)
#                 print("비겼습니다")
#             elif computer == "보":
#                 print(computer)
#                 print("졌습니다")
#             elif computer == "가위":
#                 print(computer)
#                 print("이겼습니다")
#         elif human == "보" :
#             if computer == "보":
#                 print(computer)
#                 print("비겼습니다")
#             elif computer == "가위":
#                 print(computer)
#                 print("졌습니다")
#             elif computer == "바위":
#                 print(computer)
#                 print("이겼습니다")  

