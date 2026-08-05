ch = 0
a,b = 0,0

while True:
    a= int(input("계산할 첫번째 수 입력(종료시 0입력): "))
    if a == 0:
        break
    
    b = int (input("계산할 두 번째 수 입력: "))
    ch = input ("연산자를 입력하세요: ")
    
if  (ch == "+"):
    print(("%d + %d = %d입니다.") % (a,b,a+b))
elif  (ch == "-"):
    print(("%d - %d = %d입니다.") % (a,b,a-b))
elif  (ch == "*"):
    print(("%d * %d = %d입니다.") % (a,b,a*b))
elif  (ch == "/"):
    print(("%d / %d = %d입니다.") % (a,b,a/b))
elif  (ch == "//"):
    print(("%d // %d = %d입니다.") % (a,b,a//b))
elif  (ch == "**"):
    print(("%d ** %d = %d입니다.") % (a,b,a**b))
if  (ch == "%"):
    print(("%d % %d = %d입니다.") % (a,b,a%b))
else :
    print("잘 못 입력하셨습니다.")

    
    
