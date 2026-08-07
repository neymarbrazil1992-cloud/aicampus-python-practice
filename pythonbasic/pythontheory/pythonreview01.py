#===종합 복습 : 학생 성적 관리

#1. 변수 & 리스트 초기화 
names = []
scores = []
total = 0

print("=====학생 3명의 이름과 점수를 입력하세요=====")

#2. for + input + 리스트 append
for i in range(0,3):
    name = input(str(i+1) + "번째 이름: ")
    score = int(input(str(i+1) + "번째 학생 점수: "))
    names.append(name)
    scores.append(score)
print()

#3. enumerate로 인덱스 + 값 동시 출력 
print("===== 입력한 학생 목록 =====")
for i, name in enumerate(names):
    print("%d번: %s - %d점" % (i + 1, name, scores[i]) )
print()

# 4. 반복문으로 합계, 평균 계산 
for s in scores:
    total += s
avg = total / len(scores)
print("총점: %d, 평균: %.1f") % (total, avg)
print()

#5. 조건문 + break/continue로 등급 매기기
print("=====등급 판정=====")
for i in range(0, len(scores))