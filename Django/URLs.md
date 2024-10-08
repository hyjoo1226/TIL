- URL dispatcher(운항 관리자, 분배기)
    - URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 View 함수를 연결(매핑)
- 템플릿의 많은 부분이 중복되고, URL의 일부만 변경된다면
    - Variable Routing
        - URL 일부에 변수를 포함시키는 것(변수는 view 함수의 인자로 전달할 수 있음)
        - <path_converter:variable_name>
        - Path converters: URL 변수의 타입을 지정(str, int 등 5가지 타입 지원)
- 2번째 앱 pages 생성 후 발생할 수 있는 문제
    - view 함수 이름이 같거나 같은 패턴의 URL 주소를 사용하게 되는 경우
    -> URL을 각자 app에서 관리
- URL 구조가 변경되면 유지보수가 어려운 문제
    - URL 이름 지정: path 함수의 name 키워드 인자를 정의
        - 'url' tag
            - 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환
            - ```python
                {% url 'url name' arg1 arg2 %}
- 2번째 앱의 url 이름과 첫 앱의 url 이름이 같은 문제
    - 이름에 성(key)를 붙이자
    - 'app_name' 속성 지정
    - ```python
        {% url 'app_name:path_name' %}