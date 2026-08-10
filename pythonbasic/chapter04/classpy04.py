class Person:
    
    def __init__(self, name, age,):
        self.name = name
        self._age = age 
        
    @property #getter
    def age(self):
        return self._age
    
    @age.setter #setter
    def age(self, value):
        if value < 0:
            raise ValueError("나이는 음수 일 수 없습니다.")
        self._age= value
        
p = Person("홍길동", 30)
print(p.age)
p._age = 25
print(p.age)
p._age = -25
print(p.age)

