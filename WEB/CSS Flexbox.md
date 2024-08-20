- Flex Container 안에 Flex Item들 존재
- main axis(주 축) / cross axis(교차 축, main에 수직)
- display: flex; (display: inline-flex;)
- 목적에 따른 속성 분류
  - 배치: flex-direction, flex-wrap
  - 공간 분배: justify-content, aligh-content
  - 정렬: align-items, align-self

1. Flex Container 속성
   - flex-direction: row;(column, row-reverse, column-reverse)
     - 주 축 방향 설정
   - flex-wrap: no wrap(wrap)
     - item 목록이 container 한 행에 들어가지 않을 경우 다른 행에 배치할지 여부 결정
   - justify-content: flex-start(center, flex-end, space-between, space-around, space-evenly)
     - 주 축을 따라 item과 주위에 공간을 분배
     - justify-items, self 속성이 없는 이유
       - 필요 없기 때문. margin auto를 통해 정렬 및 배치가 가능
   - align-content: flex-start(center, flex-end, space-between, space-around, space-evenly)
     - 교차 축을 따라 item과 주위에 공간을 분배
       - flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용(한 행x)
   - align-items(한 행), align-self(한 요소): flex-start(center, flex-end, stretch)
   - 수직 수평 중앙 정렬
        ```
        justify-contet: center;, align-items: center;
        ```

2. Flex item 속성
    - flex-grow
      - 남은 행 여백을 비율에 따라 각 item에 분배
        - item이 container 내에서 확장하는 비율을 지정(배율이 아니라 등분을 해서 개수대로 나눠주는 것)
        - 반대는 flex-shrink
    - flex-basis
      - item의 초기 크기값을 지정
      - flex-basis와 width값을 동시에 적용한 경우 flex-basis가 우선