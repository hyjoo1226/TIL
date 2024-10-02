'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
#정점의 개수, 간선의 개수
V, E = map(int, input().split())

#간선 정보
data = list(map(int, input().split()))

def DFS(start):
    stack = [start] #시작지점
    visited = [0] * (V + 1) #방문 여부를 체크하는 리스트

    #True 동안 돈다.(False 일때까지 돈다)
    while stack:    #스택에 값이 있는 동안 반복
        current = stack.pop()   #현재 조사할 노드

        #방문하지 않은 노드라면
        if visited[current] == 0:
            visited[current] == 1   #방문 표시 1
            print(current, end = ' ')   #방문한 노드 출력

            #현재 노드에서 갈 수 있는 다음 노드들을 찾아야 함(찾아서 스택에 넣어야 함)
            for next in range(V, 0, -1):
                #다음 노드들 중에
                # 1.현재 노드와 간선되어 연결되어 있는지
                # 2.방문한 적이 없는지
                if matrix[current][next] == 1 and visited[next] == 0:
                    stack.append(next)


#인전행렬 생성
#빈 도화지 만들기
matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    n1 = data[i * 2]
    n2 = data[i * 2 + 1]
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1
