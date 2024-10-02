# stack = []
# stack.append(1) #push(1)
# stack.append(2) #push(2)
# stack.append(3) #push(3)
# print(stack.pop())  #pop(3)
# print(stack.pop())  #pop(2)
# print(stack.pop())  #pop(1)

STACK_SIZE = 10
stack = [0] * STACK_SIZE
top = -1

top += 1    #push(1)
stack[top] = 1
top += 1    #push(2)
stack[top] = 2
top += 1    #push(3)
stack[top] = 3

print(stack[top])   #pop(3)
top -= 1