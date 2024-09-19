Django Template Language(DTL)
- Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템
- 1. Variable
    - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
    - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
    - dot(.)을 사용하여 변수 속성에 접근할 수 있음
    - ```python
        {{ variable }} {{ variable.attribute }}
- 2. Filters
    - 표시할 변수를 수정할 때 사용(변수 + '|' + 필터)
    - chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
    - 약 60개의 built-in template filters를 제공
    - ```python
        {{ variable | filter}} {{ name | truncatewords:30 }}
- 3. Tags
    - 반복 또는 논리를 수행하여 제어 흐름을 만듦
    - 일부 태그는 시작과 종료 태그가 필요
    - 약 24개의 built-in template tags를 제공
    - ```python
        {% tag %}
        {% if %} {% endif %}
- 4. Comments
    - 주석
    - ```python
        {% comment %}
        {% endcomment %}
- 주의사항
    - python처럼 일부 프로그래밍 구조를 사용할 수있지만 python과는 관련없음
    - 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리할 것

템틀릿 상속
- 페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축
- 'extends' tag
    - 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
    - 반드시 자식 템플릿 최상단에 작성되어야 함(2개 이상 사용 불가)
    - ```python
        {% extends 'path'%}
- 'bloack' tag
    - 하위 템플릿에서 재정의 할 수 있는 목록을 정의
    - 상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정하는 것
    - ```python
        {% block name %} {% endblock name %}

HTML 'form' (요청과 응답)
- 'form' element
    - 사용자로부터 할당된 데이터를 서버로 전송
    - 웹에서 사용자 정보를 입력하는 여러 방식(text, password, checkbox 등)을 제공
    - action
        - 입력 데이터가 전송될 URL을 지정(목적지)
        - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
    - method
        - 데이터를 어떤 방식으로 보낼 것인지 정의
        - 데이터의 HTTP request method(GET, POST)를 지정
    - 데이터를 어디(action)로 어떤 방식(method)으로 요청할지
    - 'input' element
        - 사용자의 데이터를 입력받을 수 있는 요소
        - type 속성 값에 따라 다양한 유형의 입력 데이터를 받음
        - 핵심 속성 - name
            - 사용자가 입력한 데이터에 붙이는 이름(key)
            - 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수있음
     - Query String Parameters
        - 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
        - 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성되며, 기본 URL과는 물음표(?)로 구분됨
        - ex. http://host:port/path?key=value&key=valeu
- HTTP request 객체
    - form으로 전송한 데이터 뿐만 아니라 Django로 들어오는 모든 요청 관련 데이터가 담겨 있음(view 함수의 첫번째 인자로 전달됨)
    - GET메서드에서 딕셔너리의 키값으로 접근
- throw-catch 간 요청과 응답