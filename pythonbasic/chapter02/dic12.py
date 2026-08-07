#딕셔너리 자료형(순서X, 중복X, 수정O, 삭제O)

#선언
a = { 'name': 'kim', 'phone': '01077777777', 'birth': '700124' }
#Map<String, String> a = new HAshMap<>(); -> a = {}
# a.put("name", "kim"); -> a['name'] = 'kim'
# a.get("name") -> a.get('name') or a['name']

b = { 0: 'Hello World!' }
c = { 'arr': [0,1,2,3] }
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)

#출력
print('a - ', a['name'])
print('a - ', a.get('name'))
print('a - ', a.get('phone'))
print('a - ', a.get('birth'))

print('b - ', b[0])
print('b - ', b.get(0))

print('c - ', c['arr'])
print('c - ', c.get('arr'))
print('c - ', c['arr'][3])
print("================================================")

# 딕셔너리 추가 
# a = { 'name': 'kim', 'phone': '01077777777', 'birth': '700124' }
a["address"]='seoul'
print('a -', a)
a['rank'] = [1,2,3]
print('a -', a)
a["gender"] = 'male'
print('a -', a)
print('a -', a['address'])
print('a -', a.get('phone'))
print('a -', a['gender']) #이쪽이 자동완성이 나와서 좀 더 쉽네 a['']

for key in a :
    print(key, ":", a[key])
#for (String key : a.keySet()) {
#    Syso(key + ": " + a.get(key))
#}     
        
print("================================================")
    
for key, value in a.items():
    print(key, ":", value)
    
# for (Map. Entry<String, String> entry : a.entrySet()){
#     (entry.getKey() + ":" + entry.getValue())
# }    

#dic_keys, dic_value, dic_items : 반복문 (iterate) 사용 가능 
print('a -', a.keys())
print('b -', b.keys())
print('c -', c.keys())
print("=======================================================")
print('a -', list(a.keys()))
print('b -', list(b.keys()))
print('c -', list(c.keys()))
print("=======================================================")
print('a -', a.values())
print('b -', b.values())
print('c -', c.values())
print("=======================================================")
print('a -', list(a.values()))
print('b -', list(b.values()))
print('c -', list(c.values()))
print("=======================================================")
print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print("=======================================================")
print('a -', list(a.items()))
print('b -', list(b.items()))
print('c -', list(c.items()))
print("=======================================================")

# a = { 'name': 'kim', 'phone': '01077777777', 'birth': '700124' }
# a 라는 객체에 name 또는  addr이라는 key 가 있는지
print('a -', 'name' in a)
print('a -', 'addr' in a)