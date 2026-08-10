#클래스 
class Car :
    #멤버 변수 
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value
    
    def downSpeed(self, value):
        self.speed -= value
        
#상속  -> 부모:Car 자식 : Sedan      
class Sedan(Car):
    seatNum=0
    
    def getSeatNum(self):
        return self.seatNum
    
class Truck(Car):
    capacity=0
    
    def getCapacity(self):
        return self.capacity
    
#메인 
sedan1 = Sedan()
truck1 = Truck()

#각 클래스의 멤버 변수 사용 
sedan1.upSpeed(60)
truck1.upSpeed(100)
sedan1.seatNum=5
truck1.capacity=50
truck1.downSpeed(40)

print("승용차의 현재 속도는 %dkm 이고, 죄석수는 %d 입니다." % (sedan1.speed, sedan1.getSeatNum()))
print("트럭의 현재 속도는 %dkm 이고, 총중량은 %d 입니다." % (truck1.speed, truck1.getCapacity()))
