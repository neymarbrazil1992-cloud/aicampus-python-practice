#함수 
def pata2_func(v1, v2):
    result=0
    result=v1+v2
    return result

def pata3_func(v1, v2, v3):
    result=0
    result=v1+v2+v3
    return result

sum = 0

#Main
sum = pata2_func(10,20)
print("매개변수 2개 ==> %d" % sum)

sum = pata3_func(10,20,30)
print("매개변수 3개 ==> %d" % sum)
print("-----------------------")

def pata4_func(v1, v2, v3 = 0): #3개짜리지만 초기화가 세팅되어있기때문에 매개변수 2개도 작동된다 => initial
    result=0
    result=v1+v2+v3
    return result

hap = 0 
hap = pata4_func(100,200)
print("매개변수 2개 ==> %d" % hap)
hap = pata4_func(100,200,300)
print("매개변수 3개 ==> %d" % hap)
# hap = pata4_func(100,200,300,400)
# print("매개변수 4개 ==> %d" % hap) --> 이건 안된다
print("-----------------------------")

def func1():
    a=10 #지역변수 
    print("func1()에서 a의 값 %d" % a)
    print("-------------------")
    
def func2():
    global a #전역변수 (Data)
    a=30 
    print("func2()에서 a의 값 %d" % a)
    print("-------------------")
    
#전역변수 
a=20 

#Main
func1()
func2()