# 윤년 구하기
# 년도를 입력받아서 윤년인지 평년인지 나타내주세요
# 연수가 4로 나누어 떨어지는 해는 윤년으로한다.
# 이중에서 100으로 나누어떨어지는 해는 평년
# 이중에서 400으로 나누어 떨어지는 해는 윤년으로한다
# 정수로 연도를 받음 ,입력받은 년도가 윤년인지 평년인지 출력하세요

year = int(input("년도를 입력하세요 :"))
if year % 4 == 0:
        if year % 100 == 0 :
            print("평년입니다.")
            if year % 400 == 0 :
                print("윤년입니다.")
        else :
            print('윤년입니다')
else :
    print("평년입니다.")

    
# if year % 400 == 0:
#     print("윤년입니다")
# elif year % 100 == 0:
#     print("평년입니다")
# elif year % 4 == 0:
#     print("윤년입니다.")
# else:
#     print("아무것도아님")