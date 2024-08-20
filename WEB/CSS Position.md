1. static
    - 요소를 Normal Flow에 따라 배치
    - top, right, bottom, left 속성이 적용되지 않음
    - 기본 값

2. relative(상대위치)
    - 요소를 Normal Flow에 따라 배치
    - 자신의 원래 위치(static)을 기준으로 이동
    - top, right, bottom, left 속성으로 위치를 조정
    - 다른 요소의 레이아웃에 영향을 주지 않음(요소가 차지하는 공간은 static일 때와 같음)

3. absolute(절대위치)
    - 요소를 Normal Flow에서 제거
    - 가장 가까운 relative 부모요소를 기준으로 이동
      - 만족하는 부모 요소가 없다면 body 태그를 기준으로 함
    - top, right, bottom, left 속성으로 위치를 조정
    - 문서에서 요소가 차지하는 공간이 없어짐

4. fixed
    - 요소를 Normal Flow에서 제거
    - 현재 화면영역(viewport)을 기준으로 이동
    - 스크롤해도 항상 같은 위치에 유지됨
    - top, right, bottom, left 속성으로 위치를 조정
    - 문서에서 요소가 차지하는 공간이 없어짐

5. sticky
    - relative와 fixed의 특성을 결합한 속성
    - 스크롤 위치가 임계점에 도달하기 전에는 relative처럼 동작
    - 스크롤이 특정 임계점에 도달하면 fixed처럼 동작하여 화면에 고정됨
    - 만약 다음 sticky요소가 나오면 다음 sticky요소가 이전 sticky요소의 자리를 대체
      - 이전 sticky요소가 고정되어 있던 위치와 다음 sticky요소가 고정되어야 할 위치가 겹치게 되기 때문

6. z-index
   - 요소의 쌓임 순서(stack order)를 정의하는 속성
   - 정수 값을 상용해 Z축 순서를 지정
   - 값이 클수록 요소가 위에 쌓이게 됨
   - static이 아닌 요소에만 적용됨
   - 특징
     - 기본값음 auto
     - 부모 요소의 z-index값에 영향을 받음
     - 같은 부모 내에서만 z-index 값을 비교
     - 부모의 z-index가 낮으면 자식의 z-index가 아무리 높아도 부모보다 위로 올라갈 수 없음
     - z-index 값이 같으면 HTML 문서 순서대로 쌓임