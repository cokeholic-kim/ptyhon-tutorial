num1 = 10
num2 = 3

#연산자
# +:덧셈,-:뺼셈,*:곱셈,/:나눗셈,**:제곱,%:나머지  ,//
print( num1 * num2)
print( num1 / num2)
print( num1 // num2)
print( num1 + num2)
print( num1 - num2)

#문자열 더하기
head = "python"
tail = "is fun"
print(head + tail)
print(head * 2)
#문자열 길이 구하기
a = "python";
print(len(a))
print(a[5])

#문자열 슬라이싱
#문자열 슬라이싱 문자열[문자열 시작번호: 끝번호] - 끝번호 제외
print(a[0:2])

print(a[:3])
print(a[2:])

#포맷팅:문자열안에 어떤 값을 삽입.
# 포맷코드 %s 문자열 $d 정수 $f 소수
# number = 18
# print("현재 온도는 %d도 입니다."%number) // 현재온도는 18도 입니다.
# print("%0.4f"%3.1415923534)
# num = 3
# print("나는 사과 %d개를 먹었다"$num)

num = 3
str3 = "어제"
print("나는 %s 사과 %d개를 먹었다" % (str3 , num))
#소수점 표현하기
print("%0.4f"%3.1415923534) # .4 는 나타낼 소숫점자리의 수를 의미

#format함수 사용하기
# 나는 사과 {0}개를 먹었다 .format(변수)
num2 = 10
print("나는 {0} 사과 {num2}개를 먹었다".format(str3,num2=30))

name = "green"
age = 30
print(f'나의 이름은 {name}이고 나이는 {age}이다.')
print(f'내년이면 내 나이는 {age+1}이 됩니다')