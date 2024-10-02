"""
2차원 배열에서 십자 모양과 X자 모양으로 M칸씩 이동하며 값을 누적하는 문제를 해결
- search 함수는 주어진 시작점에서 특정 방향으로 M칸까지 이동하며 값을 누적
- 모든 위치에서 십자 모양과 X자 모양으로 탐색을 수행하고, 그 중 최대값을 찾아 출력
- 메인 로직에서는 배열의 모든 위치에 대해 십자 모양(d=0부터 시작)과 X자 모양(d=4부터 시작)으로 탐색하여 최대값을 갱신
"""

import sys

sys.stdin = open('input.txt')

# 상 하 좌 우 좌상 우상 좌하 우하 방향을 나타내는 델타 값
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def search(x, y, d, M):
    # 현재 위치(x, y)의 값으로 합계 시작
    tmp = arr[x][y]
    # 주어진 방향 d부터 시작하여 4방향에 대해 탐색
    # d가 0이면 십자 모양, 4면 X자 모양 탐색
    for i in range(d, d + 4):
        p = M - 1  # 현재 위치를 제외한 탐색할 남은 칸 수
        nx, ny = x + dx[i], y + dy[i]  # 다음 위치 계산
        while p:
            if 0 <= nx < N and 0 <= ny < N:  # 배열 범위 내인지 확인
                tmp += arr[nx][ny]  # 범위 내라면 값 누적
                nx += dx[i]  # 같은 방향으로 계속 이동
                ny += dy[i]
            p -= 1  # 탐색한 칸 수 감소 (범위 밖이어도 감소)
    return tmp  # 누적된 합 반환


T = int(input())  # 테스트 케이스 수 입력
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열 크기 N과 이동 칸 수 M 입력
    arr = [
        list(map(int, input().split())) for _ in range(N)
    ]  # N x N 2차원 배열 입력

    result = 0
    for i in range(N):
        for j in range(N):
            # 십자 모양(상하좌우)으로 탐색
            tmp = search(i, j, 0, M)
            # X자 모양(대각선)으로 탐색
            tmp2 = search(i, j, 4, M)
            # 두 패턴 중 최대값으로 result 갱신
            result = max(result, tmp, tmp2)

    print(f'#{tc} {result}')  # 테스트 케이스 번호와 최대 합계 출력
