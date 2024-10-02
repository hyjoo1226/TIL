Q_SIZE = 4
cQ = [0] * Q_SIZE
front = rear = 0

rear = (rear + 1) % Q_SIZE  #enq(1)
cQ[rear] = 1

rear = (rear + 1) % Q_SIZE  #enq(1)
cQ[rear] = 2

rear = (rear + 1) % Q_SIZE  #enq(1)
cQ[rear] = 3

front = (front + 1) % Q_SIZE    #deq
print(cQ[front])

front = (front + 1) % Q_SIZE    #deq
print(cQ[front])

front = (front + 1) % Q_SIZE    #deq
print(cQ[front])

#여기서 기존 큐처럼 넣었으면 인덱스 에러
rear = (rear + 1) % Q_SIZE  #enq(1)
cQ[rear] = 10

rear = (rear + 1) % Q_SIZE  #enq(1)
cQ[rear] = 20

rear = (rear + 1) % Q_SIZE  #enq(1)
cQ[rear] = 30