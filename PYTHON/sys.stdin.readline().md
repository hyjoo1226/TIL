반복문으로 여러줄 입력받는 상황에서는 input() 사용 시 시간초과가 발생할 수 있음. sys.stdin.readline() 사용 시 시간초과 발생하지 않음
```
import sys
A = int(sys.stdin.readline())
```