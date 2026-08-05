## 변수 선언 부분
intStr, outStr = "", ""
ch = ""
count, i = 0,0

#메인코드
intStr = input("문자열을 입력하세요 : ")
count = len(intStr)

for i in range(0, count):
    ch= intStr[i] 
    if (ord(ch) >= ord("A") and ord(ch) <= ord("Z")):
        newCh=ch.lower()
    elif (ord(ch) >= ord("a") and ord(ch) <= ord("z")):
         newCh=ch.upper()
    else:
        newCh = ch
    outStr += newCh

print("대소문자 변환기 : %s" % outStr)