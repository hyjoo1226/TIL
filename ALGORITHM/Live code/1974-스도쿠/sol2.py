"""
check_group 함수는 
- 주어진 그룹(행, 열, 서브그리드)의 유효성을 검사
- 0을 제외한 숫자들의 집합 크기와 0이 아닌 숫자들의 개수를 비교하여 중복을 확인
"""

import sys

sys.stdin = open('input.txt')


def is_valid_sudoku(puzzle):
    """
    주어진 스도쿠 퍼즐의 유효성을 검사

    Returns: 유효한 스도쿠면 1, 그렇지 않으면 0

    스도쿠 규칙:
    1. 각 행에 1부터 9까지의 숫자가 중복 없이 있어야 함
    2. 각 열에 1부터 9까지의 숫자가 중복 없이 있어야 함
    3. 각 3x3 서브그리드에 1부터 9까지의 숫자가 중복 없이 있어야 함
    """

    def check_group(group):
        """
        주어진 그룹(행, 열, 또는 3x3 서브그리드)의 유효성을 검사

        Args: 검사할 숫자 그룹

        Returns: 그룹이 유효하면 True, 그렇지 않으면 False
        """
        # 0을 제외한 숫자들의 집합 생성
        non_zero_set = set()
        non_zero_count = 0
        for num in group:
            if num != 0:  # 0은 빈 칸을 의미하므로 제외
                non_zero_set.add(num)
                non_zero_count += 1
        # 중복이 없다면 집합의 크기와 0이 아닌 숫자의 개수가 같아야 함
        return len(non_zero_set) == non_zero_count

    # 행 검사
    for row in puzzle:
        if not check_group(row):
            return 0  # 유효하지 않은 행 발견

    # 열 검사
    for col_index in range(9):
        column = []
        for row_index in range(9):
            column.append(puzzle[row_index][col_index])
        if not check_group(column):
            return 0  # 유효하지 않은 열 발견

    # 3x3 서브그리드 검사
    for i in range(0, 9, 3):  # 서브그리드의 시작 행 (0, 3, 6)
        for j in range(0, 9, 3):  # 서브그리드의 시작 열 (0, 3, 6)
            subgrid = []
            for x in range(3):
                for y in range(3):
                    subgrid.append(puzzle[i + x][j + y])
            if not check_group(subgrid):
                return 0  # 유효하지 않은 서브그리드 발견

    return 1  # 모든 검사를 통과하면 유효한 스도쿠


# 테스트 케이스 수 입력
T = int(input())

for tc in range(1, T + 1):
    # 9x9 스도쿠 퍼즐 입력 받기
    puzzle = []
    for _ in range(9):
        row = list(map(int, input().split()))
        puzzle.append(row)

    result = is_valid_sudoku(puzzle)  # 스도쿠 유효성 검사
    print(f'#{tc} {result}')  # 결과 출력
