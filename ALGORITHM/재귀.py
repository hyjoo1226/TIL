# def fact(n):
#     if n == 1:  #중단조건
#         return 1
#     return n * fact(n-1)    #실행하는것
#
# print(fact(5))
#재귀로 모든 배열에 접근
def f(i, N):    #i 현재 인덱스, N 크기
    if i == N:  #배열을 벗어난 경우
        return
    else:
        print(arr[i])
        f(i + 1, N)
        return

arr = [1, 2, 3]
N = 3
f(0, N)