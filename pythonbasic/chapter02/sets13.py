#집합(Sets)

#선언
a = set()
b = set([0,1,2,3])
c = set([0,3,4,5])
d = set([0, 1, 'car', 'apple', 'apart'])

print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)

#튜플 변환
t = tuple(b)
# <class 'tuple'> (0,1,2,3)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

#리스트 변환 
l = list(c)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])

#집합 자료형
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#Intersection 교집합 
print('교집합w.& - ', s1 & s2) #and 
print('l - ', s1.intersection(s2)) #intersection 

#union 합집합
print('합집합w.| - ', s1 | s2) #and 
print('union - ', s1.union(s2)) #intersection 

#difference 차집합
print('차집합w.- - ', s1 - s2) #and 
print('difference - ', s1.difference(s2)) #intersection 

#추가 & 제거
s1 = set([0,1,2,3])
s1.add(4)
print('s1 - ', s1)
s1.remove(2)
print('s1 - ', s1)


