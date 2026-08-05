#변수
money, c1000, c500, c100, c50, c10=0,0,0,0,0,0
#메인
money=int(input("교환할 돈을 입력하세요 : ")) #8770

c1000=money//1000 # 8 몫
money %= 1000 #770 나머지

c500=money//500 # 1
money %= 500 #270

c100=money//100 # 2
money %= 100 #70

c50=money//50 # 1
money %= 50 #20

c10=money//10 # 2
money %= 10 #0

print("\n 천원짜리 ==>  %d개 " % c1000)
print("\n 오백원짜리 ==> %d 개 " % c500)
print(" 백원짜리   ==> %d 개 "% c100)
print(" 오십원짜리 ==> %d 개 "% c50)
print(" 십원짜리   ==> %d 개 "% c10)
print(" 바꾸지 못한 잔돈 ==> %d 원 \n"% money)