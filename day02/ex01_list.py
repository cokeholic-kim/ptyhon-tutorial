list1 = ['a','b','c','d','e']
print(list1)
print(type(list1))

# 리스트는 인덱싱과 슬라이싱이가능
print(list1[1])

# 슬라이싱
print(list1[:3])
print(list1[2:])

list2 = [1,2,3]
list3 = [4,5,6]
# 리스트 더하기 +기호로 리스트를 합칠수있다.
list4 = list2 + list3
print(list4)

# 리스트 반복하기 *기호를 사용하면 리스트를 반복해서 
# 새로운 리스트를 반환함
list5 = list2 * 2
print(list5)

#리스트 길이 구하기 len(리스트)
print(len(list5))

#리스트 수정 , 삭제(del)
list2[0] = 10
print(list2)
del list2[0]
del list5[4:]
print(list2)
print(list5)

students = ["stu1","stu2","stu3","stu4"]

# 리스트에 요소추가 append
students.append("stu5")
print(students)

# 리스트에 요소추가 (원하는 위치에) insert(start,value)
students.insert(1,"newStu")
print(students)

# 뒤집기 reverse
students.reverse()
print(students)

# 정렬 srot
students.sort()
print(students)
numberList = [5,2,1,6,7,8,2,10]
numberList.sort()
print(numberList)

# 인덱스 반환 index(value)
num = students.index("stu3")
print(num)  

# 리스트 요소제거 remove(value)
students.remove("stu3")
print(students)
numberList.remove(2)
print(numberList)

# 리스트 마지막요소 리턴후 삭제 pop()
lastlist = students.pop()
print(lastlist)
print(students)

# 리스트에 포함된 요소의 개수 세기 count(value)
fruits = ["사과","딸기","사과","바나나","사과","귤"]
applenum = fruits.count("사과")
print(applenum)