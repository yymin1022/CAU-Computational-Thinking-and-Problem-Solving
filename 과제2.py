listDong = ['흑석동', '사당동', '상도동', '노량진동', '규동']

while 1:
    inputDong = str(input('동을 입력하세요 : '))
    if listDong.count(inputDong):
        # 입력된 동이 존재하는 경우 몇번째 동인지 출력
        print('%d번째 동입니다.' %(listDong.index(inputDong)+1))
    else:
        # 입력된 동이 존재하지 않는 경우 리스트에 추가(apped)
        listDong.append(inputDong)
        print('%d번째 동으로 등록합니다.'%(len(listDong)))