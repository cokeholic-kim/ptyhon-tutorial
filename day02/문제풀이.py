# 01.pin = "881120-16068234" 성별을 나타내는 숫자를 출력하세요
pin = "881120-16068234"
print(pin[7])

# 02.문자열 "a:b:c:d" 가 있다 replace를 사용해서 "a#b#c#d"바꿔서 출력하세요
a= "a:b:c:d"
b = a.replace(":","#")
print(b) #"a#b#c#d"

# 03.[1,3,5,4,2] 리스트를 [5,4,3,2,1]로 출력
list1 = [1,3,5,4,2]
list1.sort()
list1.reverse()
print(list1)

# 04.["life","is","too","short"]리스트를 문자열로 만들어서 출력하세요
list2 = ["life","is","too","short"]
result = " ".join(list2)
print(result)

#05 [1,1,1,2,2,2,,3,3,4,4,5,5,6] ---> [1,2,3,4,5,6] 리스트에서 중복을 제거하여 출력하세요
list3 = [1,1,1,2,2,2,3,3,4,4,5,5,6]
setlist3 = set(list3)
list4 = list(setlist3)
print(list4)