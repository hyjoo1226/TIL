# 파이썬은 음수 인덱스를 사용해도 에러가 뜨지 않는다.
# 1. 넘어갔어?
# 2. 안넘어갔어?
# Falsy, Truthy 어떤 값이 True or False로 평가되는가
# 부정연산자
# is_safe: 가도 괜찮은지를 평가 후 Boolean을 반환
    # True: NxM 내에 있다.
    # not is_safe:
        # 로직 x
    # is_safe
        # 로직 O

num_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 5의 입장에서 상, 하, 좌, 우에 있는 숫자 출력하기
for r in range(len(num_list)):
    # print('r', r)
    for c in range(len(num_list[0])):
        #5를 찾자
        tmp = num_list[r]
        #tmp [1, 2, 3]
        #tmp[0] #1
        # if num_list[r][c] == 5
        if tmp[c] == 5: #값이 5라면
            #상하좌우
            print(num_list[r - 1][c])  #상
            print(num_list[r + 1][c])  #하
            print(num_list[r][c - 1])  #좌
            print(num_list[r][c + 1])  #우

# 1. 벽을 넘어가는 경우 아무것도 하지않기기
num_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, -1]
x = 1
y = 1

for d in range(4):
    # 다음 행 & 다음 열 -> 이동 후 새로운 위치 좌표
    nx = x + d_row[d]
    ny = y + d_col[d]

    # map(범위)을 벗어나는지 체크
    if nx < 0 or nx >= len(num_list) or ny < 0 or ny >= len(num_list):
        # 종료할 수도 있고 break
        # 그 인덱스를 패스 continue
        print(num_list[nx][ny])