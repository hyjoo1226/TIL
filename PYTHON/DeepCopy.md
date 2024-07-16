- 얕은 복사(Shallow copy)
    - 주소값을 복사하여 새로운 인스턴트를 생성하지 않아 같은 메모리를 가리킨다.
    - 슬라이싱, '=' 대입 연산자를 통해 할당, copy 메소드(import copy)
- 깊은 복사(Deep copy)
    - 데이터 자체를 통째로 복사하여 두 객체는 서로 완전히 독립적인 메모리를 차지한다.
    - copy.deepcopy 메소드(import copy)
    - arr[:] for arr in x
    ```
    backup_a = []
    for arr in a:
    backup_a.append(arr[:])
    ```
arr[:]는 새로운 주소값을 만든다. 빈 리스트 backup_a의 각 인덱스마다 새로운 주소값을 가진 arr을 추가한다. -> 이중배열이어도 깊은 복사 가능