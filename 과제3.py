menu = {'noodle':'500원', 'ham':'200원', 'egg':'100원', 'spaghetti':'900원'}

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
        print(menu.get(inputMenu))
    else:
        print('그런 메뉴는 없습니다.')