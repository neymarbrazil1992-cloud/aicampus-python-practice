#클래스 

class Car: 
    #맴버 변수 
    color = ""
    speed = 0
            
    def upSpeed (self, value):
        self.speed += value
        
    def downSpeed (self, value):
        self.speed -= value
        
#객체 ========================================
#메인
myCar1=Car() #Car myCar = new Car()
myCar1.color="빨간색"
myCar1.speed=0

myCar2=Car()
myCar2.color="파란색"
myCar2.speed=0

myCar3=Car()
myCar3.color="노란색"
myCar3.speed=0 

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm 입니다. " %(myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm 입니다. " %(myCar2.color, myCar2.speed))

myCar3.upSpeed(90)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm 입니다. " %(myCar3.color, myCar3.speed))

myCar3.downSpeed(30)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm 입니다. " %(myCar3.color, myCar3.speed))

