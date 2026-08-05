
...
ss='아이브짱!'

sslen=len(ss) # 5

for i in range(0, sslen):
    print(ss[i] + '$', end=" ")
    
#변수
inStr, outStr="", ""
count, i = 0,0

#메인
inStr = input("\n문자열을 입력하세요 : ") # 솔데스크
count=len(inStr)  # 4
print()

for i in range(0, count): # 0~3
    outStr+=inStr[count-(i+1)]
print("내용을 거꾸로 출력 ==> %s" % outStr) #  크스데솔

...

ss = input("문자열 입력 ==> ")
print("출력 문자열 ==> ", end='')

if ss.startswith('(') == False :
    print('(', end='')
    
print(ss, end='')

if ss.endswith(')') == False :
    print(')', end='')
    
print()


inStr = "   한글    Python    프로그래밍   "
outStr = ""

for i in range(0, len(inStr)):
    if inStr[i] !=' ':
        outStr += inStr[i]
        
print("원  문자열 ==> " + '[' + inStr + ']')
print("원  문자열 ==> " + '[' + outStr + ']')
print("-----------------------------------")

str=input("문자열 입력 ==> ")

print("출력 문자열 ==> ", end='')
for i in range(0, len(str)):
    if str[i] !='o': 
        print(str[i], end='')
    else :
        print('$', end='')
        
print("-----------------------------------")
    
date = input("날짜(연/월/일) 입력 ==> ") # 2026/08/05

ssList = date.split('/') # 분리하여 리스트에 배열로 추가 2026 04 17

print("입력한 날짜의 10년 후 ==> ", end='')
print( str(int(ssList[0]) + 10) + "년 " , end='')
print(ssList[1] + "월 " , end='')
print(ssList[2] + "일")

