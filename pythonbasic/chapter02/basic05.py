parking=[]
top, carName, outCar=0,"A",""
select = 9

#메인
while(select != 3):
    select = int(input("<1> 임차 <2> 출차 <3> 종료 : "))
    
    if(select == 1):
       if(top >=5):
            print("만차입니다.")
       else:
            parking.append(carName) #추가
            print("%s 자동차 입차됨. 주차장 상태 ===> %s "  % (parking[top], parking))
            top += 1
            carName = chr(ord(carName)+1)
    elif(select == 2):
        if(top <= 0):
            print("출차할 차가 없습니다.")
        else:
            outCar = parking.pop() #끝에서 부터 타고 올라온다 A|B|C|D|E -> A|B|C|D
            print("%s 자동차 출차됨. 주차장 상태 ==> %s" % (outCar, parking))
            top = -1
            carName = chr(ord(carName)-1)
    elif(select == 3):
        break
    else:
        print("잘 못 입력하셨습니다. 다시 입력하세요")
        
print("현재 주차장에 %d 대가 있습니다." % top) 
print("주차장 영업 종료") 
            
    