from math import sin, pi

for i in range(20):    # 20개의 *을 이용해 sin 함수의 한 주기 그래프를 그리도록 하기 위해 20번 반복
    # i가 0일 때 sin(0), i가 10일 때 sin(pi), i가 20일 때 sin(2 * pi)의 값을 갖도록 range값 지정 후 해당 값만큼 공백 출력
    for j in range(10 + int(10* (sin(i * pi / 10)))):
        print(' ', end='')
    # 공백 이후에 1개의 *을 출력해 그래프가 작성되도록 구현
    print('*')