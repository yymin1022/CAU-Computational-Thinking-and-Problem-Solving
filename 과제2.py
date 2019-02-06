listDong = ['흑석동', '사당동', '상도동', '노량진동', '규동']

while 1:
    inputDong = str(input('동을 입력하세요 : '))
    if listDong.count(inputDong):
        print('%d번째 동입니다.' %(listDong.index(inputDong)+1))
    else:
        listDong.append(inputDong)
        print('%d번째 동으로 등록합니다.'%(len(listDong)))