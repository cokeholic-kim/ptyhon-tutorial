f = open('test2.txt','w',encoding='utf-8')
f.write("Life is too short \n you need java")
f.close()

f = open('test2.txt','r')
body = f.read()
f.close()

body = body.replace("java","python")

f = open('test2.txt',"w",encoding='utf-8')
f.write(body)
f.close()
