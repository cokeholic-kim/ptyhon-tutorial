#ex01_print.py

print('python' 'javascript' "java")
print("pyton"+'javascript'+'java')
print('python','javascript','java') #한칸씩 띄어쓰기 처리됨
# print함수 호출시 end매개변수에 끝 문자를 지정할 수 있음
# 지정하지 않으면 \n 이 지정되어있음
print(1,end= ' ')
print(2)
for i in range(5):
    print(i, end = " ")
    