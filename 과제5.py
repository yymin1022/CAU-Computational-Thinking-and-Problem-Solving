while 1:
    start = int(input('시작 단?'))
    stop = int(input('끝 단?'))

    if stop < start:
        print('시작 단의 입력값이 끝 단의 입력값보다 작아야 합니다. 다시 입력해주세요.')
        continue

    '''
    시작 단과 끝 단의 각 입력값 사이 차가 4 이하라는 문제의 제시 조건을 만족하기 위한 if문
    각 입력값 사이 차 크기에 따라 출력시의 간격 크기를 지정
    '''
    if (stop - start) > 4:
        print('시작 단과 끝 단 사이의 차가 4 이하가 되어야 합니다. 다시 입력해주세요.')
        continue
    elif (stop - start) == 4:
        endStr = '  '
    elif (stop - start) == 3:
        endStr = '    '
    elif (stop - start) == 2:
        endStr = '        '
    elif (stop - start) == 1:
        endStr = '              '

    for i in range(1, 10):
        for j in range(start, stop + 1):
            print(endStr, j, 'X', i, '=', j * i, end='' if j*i > 9 else ' ')
            j += 1
        print(' ')