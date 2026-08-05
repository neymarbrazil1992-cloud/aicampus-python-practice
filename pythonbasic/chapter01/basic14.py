# 1 ~ 100의 합에서 최초로 1000 이 넘는 위치 index
j=0
sum=0

for j in range(1, 101):
    sum+=j
    if sum>1000:
        break
    
print(sum)
print("1000이 넘는 인덱스는 %d입니다" % j)

print("=================================")
i=0
hap=0

for i in range(1,101):
    if i%3 == 0:
        continue
    hap += i

print("3의 배수를 제외한 합: %d" % hap)