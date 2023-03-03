# ex01_while.py

# while 조건문 :
    # 수행할문장

treeHit = 0
while treeHit < 10:
    print("나무를 %d번 찍었습니다." %treeHit)
    treeHit += 1
    
# number = 0
# while number != 4:
#     print("4가 아닙니다")
#     number = int(input())
    
# 복습

fruits = ["사과","오렌지"]
fruits.append("딸기") #리스트 끝에 추가
fruits.insert(1,"수박") #원하는 위치에 추가
print(fruits)

# while 문을 사용해서 1~10까지 숫자중 홀수만 리스트에 넣어주세요
numlist = []
number = 0
while number <= 10 :
    if number % 2 == 1 :
        numlist.append(number)
    number += 1
    
print(numlist)