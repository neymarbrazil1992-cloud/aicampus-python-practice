import random

#메서드 
def getNumber():
    return random.randrange(1,46)

#변수 
lotto=[]
num=0

#메인
print("**로또 추첨을 시작합니다.**")

for round in range(1,11): #10회
    lotto = []
    while(True):
        num = getNumber()
        
    #중복 제어 
        if lotto.count(num) == 0:
            lotto.append(num)
        if len(lotto) >= 6 :
            break
    print(f"{round}회차 추첨된 로또 번호 ==> ", end =" ")    
    
    lotto.sort()
    for i in range(0, 6):
        print("%d " % lotto[i], end="")
    print()
    
    