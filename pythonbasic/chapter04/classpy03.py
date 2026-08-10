class Person:
    
    # 오버로딩 
    def __init__(self, name, age, ssn):
        self.name = name #public
        self._age = age #pretected (상속관계에서 사용)
        self.__ssn = ssn #private 외부 접근 안됨 
    
    
    
p = Person("홍길동", 30, "123456")
print(p.name) #접근 가능 
print(p._age) #접근은 되지만 가를 패키지에서 제한 
# print(p.__ssn) #접근 안됨
print(p._Person__ssn) #접근 가능 (Name Mangling)



