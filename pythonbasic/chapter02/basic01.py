aa= [] # 리스트 -> java의 모든 list를 하나로 
#초기화
for i in range(0,4):
    aa.append(0)
    
hap = 0
#-----------------------
#입력
for i in range(0,4):
    aa[i] = int (input(str(i+1)+"번째 숫자: "))
    
#출력
hap = aa[0] + aa[1] + aa[2] + aa[3]
print("합계: %d" % hap)
