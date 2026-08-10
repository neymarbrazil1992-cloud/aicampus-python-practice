class Animal:
    # 멤버 변수 
    name = ""
    age = 0
    
    # 메서드 
    def setName(self, name):
        self.name = name
        
    def setAge(self, age):
        self.age = age
           
    def getInfo(self):
        return f"이름: {self.name}, 나이: {self.age}살"
    
#상속
class Dog(Animal):
    breed= " "
    
    def setBreed(self, breed):
        self.breed = breed

    def bark(self):
        return "멍멍!"

    #오버라이딩 
    def getInfo(self):
        return super().getInfo() + f", 품종: {self.breed}"
    
class Bird(Animal):
    wingSpan = 0
    
    def setWingSpan(self, wingSpan):
        self.wingSpan = wingSpan

    def chirp(self):
        return "짹짹!"

    #오버라이딩 
    def getInfo(self):
        return super().getInfo() + f", 날개길이: {self.wingSpan}cm"
    
#-----------------------------------------------------------
#메인

dog1 = Dog()
bird1 = Bird()

#강아지 정보 
dog1.name = "탄빵이"
dog1.age = 4
dog1.setBreed("피니쉬스피츠")
dog1.bark()


#새정보 

bird1.name = "참새"
bird1.age = 1
bird1.setWingSpan("20")
bird1.chirp()

#출력

# print("강아지의 이름은 %s고 %d살이고 종은 %s이고 %s 짖습니다" %(dog1.name,dog1.age,dog1.setBreed,dog1.bark))
# print("새는 %s이고 %s살이고 날개는 %d있고 %s웁니다" % (bird1.name, bird1.age, bird1.setWingSpan, bird1.chirp))

print(dog1.getInfo())
print(dog1.bark()+" 짖습니다.")
print(bird1.getInfo())
print(bird1.chirp()+" 웁니다.")




    