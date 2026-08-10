#클래스 
class Car:
    
    #멤버변수
    color=""
    speed=0
    count=0
    
    #생성자
    def __init__(self):
       # pass #---> abstract Method : public void Sum()
        Car.count += 1 #Static -> Data
        self.speed = 0 
        
#메인 
myCar1 = Car() #객체 생성 : count 1 / speed = 0 
myCar2 = Car()
myCar3 = Car()
myCar1.speed=60
print("자동차1의 현재 속도는 %dkm 이고, 생성된 자동차 수는 %d 입니다. " %(myCar1.speed, Car.count))
myCar2.speed=50
print("자동차2의 현재 속도는 %dkm 이고, 생성된 자동차 수는 %d 입니다. " %(myCar2.speed, Car.count))
myCar3.speed=120
print("자동차3의 현재 속도는 %dkm 이고, 생성된 자동차 수는 %d 입니다. " %(myCar3.speed, Car.count))


