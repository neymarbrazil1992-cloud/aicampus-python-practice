#리스트 자료형 (순서o, 중복o, 수정o, 삭제o) append, remove, sort
#--> type이 달라도 다 쓸 수 있다 

#선언
a=[]
b=list()
c=[0,0,1,2]
d=[0,1,'car','apple', 'apart']
e=[0,1,['car','apple','apart']] #---> 리스트 안에 리스트도 넣을 수 있다 

#인덱싱
print("#====================================")
print("d -", type(d), d)
print("d -", d[1])
print("d -", d[1]+d[1]+d[1]) #---> 산술 연산도 가능하다 
print("d -", d[-1]) #apart
print("e -", e[-1][1])
print("e -", e[-1][1][4]) #하나씩 안으로 들어가면서 읽는다
print("e -", list(e[-1][1]))

#슬라이싱
print("#=====================================")
#d=[0,1,'car','apple', 'apart']
print("d -", d[0:3]) #0에서 부터 2까지 읽는다
print("d -", d[2:])
print("d -", d[2][1:3])

#리스트 연산 
print("==================================")
c=[0,0,1,2]
print('c + d -', c + d)
print('c * 3 -', c * 3)
print("'hi' + c[0] -", 'hi' + str(c[0])) #String은 str