# 딕셔너리
foods={'떡볶이':'순대',
       "짜장면":"탕수육",
       "라면":"김치",
       "피자":"피클",
       '맥주':"먹태",
       "치킨":"콜라",
       "삼겹살":"소주"}

# Map<String> m = new hashmap; -> 자바 버젼

#메인
while(True):
    myfood = input(str(list(foods.keys()))+"중 오늘의 메뉴는: ")
    if myfood in foods:
        print("<%s>에 맞는 궁합 음식은 <%s>입니다." % (myfood, foods.get(myfood)))
    elif myfood == '끝': # equals.
        break
    else:
        print("메뉴에 없는 음식입니다. 다시 주문해 주세요~~")