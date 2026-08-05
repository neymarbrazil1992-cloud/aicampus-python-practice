i, sum = 0,0
snum, endnum, num = 0,0,0

snum = int(input("시작값 입력: "))
endnum = int(input("끝값 입력: "))
num = int(input("증가값 입력: "))

for i in range(snum, endnum+1, num):
    sum += i
print("%d에서 %d까지 %d씩 증가한 값의 합: %d" % (snum, endnum, num, sum))