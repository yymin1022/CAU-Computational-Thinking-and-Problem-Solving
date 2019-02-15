menu = {'noodle':'500원', 'ham':'200원', 'egg':'100원', 'spaghetti':'900원'}

# Dictionary로 선언된 메뉴에서 메뉴의 이름(key)만을 추출해 리스트로 생성 및 해당 리스트를 메뉴목록으로 출력하기 위한 String 작업 수행
menuList = list(menu.keys())
menuStr = '('
i = 0
for i in range(len(menuList)):
   menuStr += menuList[i] + ' '
   i += 1
menuStr += ')'

while 1:
    print('안녕하세요 다음의 메뉴 중 원하는 메뉴를 선택하세요.')
    inputMenu = str(input(menuStr+' '))

    if inputMenu in menu:
        # 입력된 메뉴가 존재하는 메뉴인 경우 메뉴 Dictionary로부터 가격을 가져와 출력
        print(menu.get(inputMenu))
    else:
        print('그런 메뉴는 없습니다.')