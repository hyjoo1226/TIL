"""
- 2차원 배열에서 십자 모양과 X자 모양으로 탐색하여 최대 합을 찾기
- 각 위치에서 십자 모양과 X자 모양으로 별도로 탐색하며, 배열 범위를 벗어나거나 m칸을 모두 탐색하면 중단
"""

import sys

sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 수 입력
for tc in range(1, T + 1):
    n, m = map(int, input().split())  # 배열 크기 n과 이동 칸 수 m 입력
    arr = [
        list(map(int, input().split())) for _ in range(n)
    ]  # n x n 2차원 배열 입력

    # 십자 모양 방향 (상, 하, 좌, 우)
    dr1 = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # X자 모양 방향 (좌상, 우상, 좌하, 우하)
    dr2 = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    ans = 0  # 최대 합계를 저장할 변수

    for i in range(n):
        for j in range(n):
            tmp1, tmp2 = arr[i][j], arr[i][j]  # 현재 위치 값으로 시작

            # 십자 모양 탐색
            for dx, dy in dr1:
                x, y = i + dx, j + dy  # 다음 위치 계산
                cnt = 1  # 이동한 칸 수 카운트
                while 0 <= x < n and 0 <= y < n and cnt < m:
                    tmp1 += arr[x][y]  # 값 누적
                    x += dx  # 같은 방향으로 계속 이동
                    y += dy
                    cnt += 1

            # X자 모양 탐색
            for dx, dy in dr2:
                x, y = i + dx, j + dy
                cnt = 1
                while 0 <= x < n and 0 <= y < n and cnt < m:
                    tmp2 += arr[x][y]
                    x += dx
                    y += dy
                    cnt += 1

            ans = max(ans, tmp1, tmp2)  # 최대값 갱신

    print(f'#{tc} {ans}')  # 테스트 케이스 번호와 최대 합계 출력
