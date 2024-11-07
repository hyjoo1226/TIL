부모는 자식에게 데이터를 전달(Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event)
- Props: 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성
  - 부모 속성이 업데이트되면 자식으로 전달되지만 그 반대는 안됨
  - 자식 컴포넌트 내부에서 props를 변경하려고 시도해서는 안되며 불가능
  - 부모 컴포넌트가 업데이트될 때마다 이를 사용하는 자식 컴포넌트의 모든 props가 최신값으로 업데이트
  - 모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩을 형성(One-Way Data Flow)
    - 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위함 - 데이터 흐름의 일관성, 단순화
  - Props 선언
    - ```python
      #Parent.vue

      <template>
        <div>
          <ParenChild my-msg="message"/>  #정적 props
          #props이름 = props값
        </div>
      </template>
    - ```python
      #ParentChild.vue

      <template>
        <div>
          {{ myMsg }}
          <ParentGrandChild :my-msg="my-Msg"/>  #동적 props - 자바스크립트 영역이 됨
        </div>
      </template>

      <script setup>
      # 내려받은 props를 선언
      # 1. 배열 선언 방식(영억이 달라 케밥케이스 -> 카멜케이스로 작성)
        # 자바스크립트에서 -을 대문자로 변환
      defineProps(['myMsg']) 

      # 2. 객체 선언 방식(권장) - 가독성, 유효성 검사, 기본값 활용 등
      defineProps({
        myMsg: String
      })
      </script>
    - ```python
      #ParentGrandChild

      <template>
        <div>
          {{ myMsg }}
        </div>
      </template>
      <script setup>
      defineProps({
        myMsg: String
      })
      </script>

- Emit: 자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드
  - $emit(event, ...args)
    - ```html
      <!-- $emit을 사용하여 템플릿 표현식에서 직접 사용자 정의 이벤트를 발신 -->
      <button @click="$emit('someEvent')">클릭</button>
    - ```python
      ## emit 이벤트 선언 방식(권장)
      <template>
        <button @click="buttonClick">클릭</button>
      </template>

      <script setup>
      const emit = defineEmits(['someEvent'])

      const buttonClick = function () {
        emit('someEvent')
      }
      </script>
    - ```html
      <!-- 부모는 v-on을 사용하여 수신 -->
      <ParentComp @some-event="someCallback" />