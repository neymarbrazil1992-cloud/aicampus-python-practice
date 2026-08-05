aa= []
bb= []
value = 0
        # 리스트 -> java의 모든 list를 하나로 
#초기화
for i in range(0,100):
    aa.append(value)
    value += 2
print("aa[0]는 %d, aa[99]는 %d 입력됨 " %(aa[0], aa[99]))

print("")    
#-----------------------
#입력
for i in range(0,100):
    bb.append(aa[99-i])
    
#출력

print("bb[0]는 %d, bb[99]는 %d 입력됨 " % (bb[0], bb[99]))