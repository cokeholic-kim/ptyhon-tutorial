# ex07_function.py 함수
# 함수 입력값 ===> 함수 ===> 리턴값
# 1.일반적인함수 : 입력값과 리턴값이 있는 함수
def add(a,b):
    return a+b

re = add(10,20)
print(re)

# 입력값이 없는 함수
def printHi():
    print("HI")
    return 10
    
print(printHi())

# 매개변수 지정해서 호출하기
# 매개변수를 지정해서 호출하면 순서에 상관없이 사용할수있음
def sub(a,b):
    return a-b

re2 = sub(b=10,a=20)
print(re2)

# 입력값이 몇개가 될지 모를때.
def addMany(args):
    result = 0
    for i in args:
        result = result + i
    return result

re3 = addMany(1,2,3,4,5)
re4 = addMany(2,3,4)
print(re3)
print(re4)

# 매개변수에 초기값 설치하기.
def sayMy(name, age, man=True):
    print("나의 이름은 %s" %name)
    print("나의 나이는 %d살 입니다." %age)
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")
        
sayMy('김그린',22)
sayMy('이블루',30,False)