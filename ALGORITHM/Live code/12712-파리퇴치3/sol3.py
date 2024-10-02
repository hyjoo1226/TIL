"""
- calculate_sum 함수는 주어진 시작점(x, y)에서 특정 방향들로 m칸 이동하며 값을 누적
- 메인 로직에서는 배열의 모든 위치에 대해 십자 모양과 X자 모양의 합을 계산하고, 최대값을 갱신
"""

import sys

sys.stdin = open('input.txt')


def calculate_sum(arr, x, y, directions, m):
    """
    주어진 방향으로 m칸 이동하며 합을 계산
    """
    total = arr[x][y]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        for _ in range(m - 1):
            if 0 <= nx < n and 0 <= ny < n:
                total += arr[nx][ny]
                nx += dx
                ny += dy
            else:
                break
    return total


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 십자 모양과 X자 모양 방향 정의
    cross = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    diagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    max_sum = 0
    for i in range(n):
        for j in range(n):
            # 십자 모양과 X자 모양의 합 계산
            cross_sum = calculate_sum(arr, i, j, cross, m)
            diagonal_sum = calculate_sum(arr, i, j, diagonal, m)
            max_sum = max(max_sum, cross_sum, diagonal_sum)

    print(f'#{tc} {max_sum}')
