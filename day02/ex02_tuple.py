# 요소 값 수정 못함
# () 
t1 = (1,2,3)
t2 = (1,) # 콤마필수
print(t2)
t3 = 1,2,3
print(type(t3))

# 인덱싱 ,슬라이싱, + , * ,len() 만 가능
print(t3[0:2])
print(t1+t3)
print(t1*3)
print(len(t1))