score=int(input('점수를 입력하세요 : '))

if score>100 or score<0:
    print("점수를 다시 입력해주세요")    
else:
    if score >=90:
        print('A')
    else:
        if score >= 80:
            print('B')
        else:
            if score >=70:
                print('C')
            else:
                if score >= 60:
                    print('D')
                else:
                    print('F')                   
    print("학점입니다. ")