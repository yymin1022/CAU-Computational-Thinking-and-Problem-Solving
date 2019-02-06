inputList = []
count = 0;

print('데이터를 입력하세요(입력을 마치려면 0을 입력하세요)')
while 1:
    inputNum = int(input())
    if inputNum:
        inputList.append(inputNum)
        count += 1
    else:
        break

# 입력된 값들을 리스트 내에서 크기순으로 정렬
inputList.sort()

for i in range(len(inputList)):
    print(inputList[i], end=' ')