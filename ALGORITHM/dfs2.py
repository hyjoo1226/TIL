node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']  #0번 무시하고 1번부터 문제풀겠다
#노드를 코드로 옮길 때 인접리스트와 인접행렬의 방법이 있다
'''
인접 행렬(adjacency matrix)
- n x m 크기의 정사각형 행렬
- 노드들 간의 연결 관계를 행렬로 표현한 것
- 무방향 그래프에서는
    - 정점 i와 j 사이에 간선이 있다면 matrix[i][j] = matrix[j][i] = 1, 없으면 0 #대칭구조의 행렬

'''
#       A  B  C  D  E  F  G
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],   #A
    [0, 1, 0, 0, 1, 1, 0, 0],   #B
    [0, 1, 0, 0, 0, 1, 0, 0],   #C
    [0, 0, 1, 0, 0, 0, 1, 0],   #D
    [0, 0, 1, 1, 0, 0, 1, 0],   #E
    [0, 0, 0, 0, 1, 1, 0, 1],   #F
    [0, 0, 0, 0, 0, 0, 1, 0],   #G
]

def DFS(s, V): #시작정점 s, 정점의 개수 V
    #stack에 시작 정점을 push
    stack = [s]
    #방문 여부를 체크하는 리스트
    visited = [0] * (V + 1)

    #스택이 빌 때까지 DFS 진행(스택에 값이 있는 동안 진행)
    while stack:
        #현재 조사할 노드
        current = stack.pop()

        #방문하지 않은 노드라면
        if visited[current] == 0:
            #방문 표시
            visited[current] = 1
            #방문한 노드 출력
            print(node[current])

            #현재 노드에서 갈 수 있는 다음 노드들을 스택에 추가
            for next in range(V, 0, -1): #후입선출,  반대방향(큰번호우선)으로 확인(1, v + 1)
                #다음 노드가 간선이 연결이 되어있고 + 방문한 적이 없다면
                if matrix[current][next] == 1 and visited[next] == 0:
                    #stack에 push
                    stack.append(next)

#인접행렬 만들기
#V = 노드의 개수, E = 간선의 개수
V, E = map(int, input().split())

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]  #0번째 인덱스 신경안쓰지만 있으므로

#노드별 간선 정보
data = list(map(int, input().split()))
#간선 정보를 넣기
#간선의 개수만큼 반복하면서 넣기
for i in range(E):
    n1 = data[i * 2]
    n2 = data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1
# for _ in range(E):
#     i, j = map(int, input().split())
#     adj_matrix[i][j] = 1
#     adj_matrix[j][i] = 1

DFS(1, 7)