# 랜덤모듈 불러오기
import random
# 로또번호 출력
# 1~45 겹치지 않게 랜덤한 숫자로 6개 출력
# lottolist  = [range(1,46)] ,resultlost = []
lottolist = list(range(1,46))
resultlist = []
for i in range(6):
    randnum = random.randint(1,len(lottolist))-1
    resultlist.append(lottolist[randnum])
    lottolist.remove(lottolist[randnum])
    # lottol = lottolist.pop(randomNum)
    # result.append(lottol)
print(resultlist)