#기본
A = input()

#한줄 입력값 여러개
A, B, C = input().split()

#각 줄마다 입력값 한개씩
A = input()
B = input()
C = input()
...

#정수형으로 입력값
A = int(input())

# 정수형으로 입력값 여러개
A, B, C = map(int, input().split())

#정수형 입력값 리스트
A = list(map(int, input().split()))

# 특정 횟수만큼 입력값 받기
for i in range(T):
    A = input()

# 이차원 배열로 입력값 받기
number_list = [list(map(int, input().split())) for _ in range(N)]