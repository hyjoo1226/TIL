- Block box
   - 항상 새로운 행으로 나뉨
   - padding, margin, border로 인해 다른 요소를 상자로부터 밀어냄
   - width와 height 속성 사용 가능
   - width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함(상위 컨테이너 너비 100%로 채우는 것)
   - h1~6, p, div 등

- Inline box
   - 새로운 행으로 넘어가지 않음
   - width와 height 속성을 사용할 수 없음
   - 수직 방향: padding, margin, border가 적용되지만 다른 요소를 밀어낼 수는 없음
   - 수평 방향: padding, margin, border가 적용되어 다른 요소를 밀어낼 수 있음
   - a, img, span, strong, em 등

- inline-block
  - inline과 block 요소 사이의 중간 지점을 제공
  - width 및 height 속성 사용 가능
  - padding, margin, border로 인해 다른 요소가 상자에서 밀려남
  - 새로운 행으로 넘어가지 않음
  - 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용