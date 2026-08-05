i,k,heartNum = 0,0,0
numStr, ch, heartStr = "", "", ""

#메인
numStr = input("숫자를 입력하세요: ") #int arr = new int[5]...
            #=> 알아서 배열로 인식  ={5,4,3,2,1} ...num.length
print("")

i=0
ch=numStr[i] #하나씩 읽어오기

while True:
    heartNum=int(ch) # 숫자로 형 변환 
    
    heartStr=""
    for k in range(0, heartNum): #for(int i=0;i<numStr.length;i++)
        heartStr+="\u2665" #하트모양의 유니코드
    print(heartStr)
    
    i+=1
    
    if (i>len(numStr)-1):
        break

    ch=numStr[i]