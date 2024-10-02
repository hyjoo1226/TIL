N = 10
q = [0] * N
front = -1
rear = -1

rear += 1   #enqueue(1)
q[rear] = 1
rear += 1   #enqueue(2)
q[rear] = 2
rear += 1   #enqueue(3)
q[rear] = 3

front += 1  #dequeue()
print(q[front])
front += 1  #dequeue()
print(q[front])
front += 1  #dequeue()
print(q[front])

#이 방식은 데이터 많아지면 많이느려짐
q2 = []
q2.append(10)
q2.append(20)
print(q2.pop(0))
print(q2.pop(0))