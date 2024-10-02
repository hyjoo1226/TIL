"""
1. check 함수는 주어진 집합(행, 열, 또는 3x3 서브그리드)에 1부터 9까지의 숫자가 모두 있는지 확인
2. 각 테스트 케이스마다 9x9 퍼즐을 입력받음
3. 행, 열, 3x3 서브그리드를 각각 확인하며, 하나라도 유효하지 않으면 즉시 검사를 중단하고 결과를 0으로 설정
4. 집합(set)을 사용하여 중복을 쉽게 확인. 차집합 연산을 통해 1-9가 모두 있는지 빠르게 확인
5. 3x3 서브그리드 확인 시 이중 반복문을 사용하여 효율적으로 모든 서브그리드를 순회
"""

import sys

sys.stdin = open('input.txt')


def check(arr):
    # 1부터 9까지의 숫자가 모두 있는지 확인
    return 0 if check_list - arr else 1


T = int(input())  # 테스트 케이스 수 입력

for tc in range(1, T + 1):
    # 9x9 스도쿠 퍼즐 입력 받기
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    check_list = set(
        range(1, 10)
    )  # 1부터 9까지의 숫자 집합 생성 (차집합을 구해 공집합이 되는지 비교하기 위한 베이스)
    result = 1  # 초기 결과값 설정 (유효한 스도쿠로 가정)

    for i in range(9):
        row = set(puzzle[i])  # 각 행을 집합으로 변환
        if not check(row):  # 행에 1-9가 모두 있는지 확인 (공집합이 아니라면)
            result = 0  # 유효하지 않으면 결과를 0으로 설정
            break  # 더 이상 확인할 필요 없음

        col = set()  # 열 확인을 위한 빈 집합 생성
        for j in range(9):
            col.add(puzzle[j][i])  # 현재 열의 모든 숫자를 집합에 추가
        if not check(col):  # 열에 1-9가 모두 있는지 확인 (공집합이 아니라면)
            result = 0
            break

    # 3x3 서브그리드 확인
    for i in range(0, 9, 3):  # 3칸씩 건너뛰며 시작점 설정
        for j in range(0, 9, 3):
            matrix = set()  # 3x3 서브그리드를 위한 집합
            for x in range(3):
                for y in range(3):
                    # 현재 3x3 서브그리드의 모든 숫자를 집합에 추가
                    matrix.add(puzzle[i + x][j + y])
            if not check(matrix):  # 서브그리드에 1-9가 모두 있는지 확인
                result = 0
                break

    print(f'#{tc} {result}')  # 테스트 케이스 번호와 결과 출력
