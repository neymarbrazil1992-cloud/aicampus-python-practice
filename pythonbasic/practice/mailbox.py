mailbox = []
top = 0
mailNum = 1
select = 9

while select != 3:
    select = int(input("<1> 편지받기 <2> 편지읽기(꺼내기) <3>종료: "))
    
    if select == 1:
        if top >= 10:
            print("편지함이 가득 찾습니다.")
            print("더 많은 이메일을 받기위해서 정리해주세요")
        else:
            mailName = "mail" + str(mailNum) + "@email.com"
            mailbox.append(mailName)
            print("%s 도착함. 편지함 상태 ===> \n%s" % (mailbox[top], mailbox))
            top += 1
            mailNum += 1
    elif select == 2:
        if top <= 0:
            print("읽을 편지가 없습니다.")
        else:
            outMail = mailbox.pop()
            print("%s 편지 읽음. 편지함 상태 ===> %s" % (outMail, mailbox))
            top -= 1
    elif select == 3:
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요") 
        
print("편지함에 %s개의 메일이 있습니다" % top)
print("편지함 종료")
            
            