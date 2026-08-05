matrix = [[1,2,3], [4,5,6]]

for i, row in enumerate(matrix):
    print(i, "행: ", row)
    for j, value in enumerate(row):
        print(" ", j, "열: ", value)
        
print("==================")
        
list1 = []
list2 = []
value = 1

for i in range(0, 3):
    for j in range(0, 4):
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []

# enumerate로 몇 번째 그룹인지 + 그 안의 값들 출력
for i, group in enumerate(list2):
    print(i, "번째 그룹:", group)