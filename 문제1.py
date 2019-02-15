while 1:
    inputNum = int(input('숫자를 입력하세요 : '))

    if inputNum == 0:
        print('프로그램을 종료합니다.')
        break
    elif inputNum < 0:
        # 입력된 값이 음수인 경우, -1을 곱해 그 절대값을 출력
        print('입력된 숫자의 음수이며, 절대값은 %d입니다.' %(inputNum * -1))
    elif inputNum > 0:
        # 입력된 값이 양수인 경우, 그대로 출력 
        print('입력된 숫자는 양수 %d입니다.' %inputNum)