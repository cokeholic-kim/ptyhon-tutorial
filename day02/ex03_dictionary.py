# 딕셔너리 자료형
# 리스트나 튜플처럼 순차적으로 요소값을 구하지 않고
# key를 통해 value에 접근한다.
# { key1: value1, key2: value2, key3: value3 }
# key는 중복안됨 
dic = {'name':"green","phone":'01012341234',"age":30}
dic2 = {1:"a",2:"b",3:"c"}

# 속성 추가하기
dic["isJob"] = True
print(dic)
# value값 접근
print(dic['name'])
# 요소 삭제하기
del dic['phone']
print(dic)
dic2[4] = "d"
print(dic2)

# 키는 중복해서 사용할수없고 고유한 값을 사용해야한다
# 같은 키를사용하면 뒤에사용한키의 값이 적용된다.
dic3 = {'name':"G",'age':30,'name':'b'}
print(dic3)

# key리스트 만들기
dic3key = dic3.keys()
print(dic3key)
dic3keylist = list(dic3key)
print(dic3keylist)
#value 리스트 만들기 values()
dic3value = dic3.values()
print(list(dic3value))
#key,value 쌍 얻기 items()
dic3item = dic3.items()
print(list(dic3item))

# key,value 쌍 모두 지우기 clear()
dic3.clear()
print(dic3)

# key로 value값 얻기 get(key)
dic4 = {'name': '구름','age':3,'color':'white'}
print(dic4.get('name'))
print(dic4.get('age'))
print(dic4.get('a','aaaaa')) #없는 키로 호출시 none을 반환 default지정가능

# 해당 key가 있는지 in 
print('name' in dic4) #true
print('a' in dic4) #false