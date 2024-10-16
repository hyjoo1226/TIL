API(Application Programming Interface): 클라이언트-서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계
- 이렇게 요청을 보내면, 이렇게 정보를 제공해줄 것이다하는 메뉴얼
- 소프트웨어와 소프트웨어 간 지정된 정의(형식)으로 소통하는 수단
- Web API: 웹 서버 또는 웹 브라우저를 위한 API, 여러 Open API들을 활용하는 추세
- REST(Representational State Transfer): API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
    - RESTful API: REST 원리를 따르는 시스템. '자원(데이터)을 정의하고 '자원에 대한 주소를 지정'하는 전반적인 방법을 서술
    - REST API: REST라는 설계 디자인 약속을 지켜 구현한 API
        1. 자원의 식별: URL
            - URI(Uniform Resource Identifier): 통합 자원 식별자
                - 인터넷에서 리소스(자원)를 식별하는 문자열
                - 가장 일반적인 URL은 웹 주소로 알려진 URL
                - URL(Uniform Resource Locator): 통합 자원 위치
                    - 웹에서 주어진 리소스의 주소
                    - 네트워크 상에 리소스가 어디 있는지를 알려주기 위한 약속

            - ex. http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereinTheDocument
                - Schema(Protocol): 브라우저가 리소스를 요청하는 데 사용해야 하는 규약
                    - URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄
                    - 기본적으로 웹은 http(s)를 요구
                    - ex. http
                - Domain Name: 요청중인 웹 서버를 나타냄
                    - 어떤 웹 서버가 요구되는 지를 가리키며 직접 IP주소를 사용하는 것도 가능하지만, 사람이 외우기 어렵기 때문에 주로 Domain Name으로 사용
                    - ex. www.example.com
                - Port: 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
                    - HTTP 프로토콜의 표준 포트: 80(HTTP), 443(HTTPS)
                    - 표준 포트만 작성 시 생략 가능
                    - ex. 80
                - Path: 웹 서버의 리소스 경로
                    - 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만 오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현
                    - ex. /path/to/myfile.html
                - Parameters: 웹 서버에 제공하는 추가적인 데이터(GET method)
                    - '&' 기호로 구분되는 key-value 상 목록
                    - 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음
                    - ex. ?key1=value1&key2=value2
                - Anchor: 일종의 북마크를 나타내며 브라우저에 해당 지점에 있는 콘텐츠를 표시
                    - '#'(부분식별자) 이후 부분은 서버에 전송되지 않음
                    - 서버에 전달되지 않고 브라우저에게 해당 지점으로 이동하도록
                    - ex. #SomewhereinTheDocument
        2. 자원의 행위: HTTP Methods
            - HTTP Request Methods: 리소스에 대한 행위(수행하고자 하는 동작)를 정의. HTTP verbs
                - GET: 서버에 리소스의 표현을 요청, GET을 사용하는 요청은 데이터만 검색해야 함
                - POST: 데이터를 지정된 리소스에 제출, 서버의 상태를 변경
                - PUT: 요청한 주소의 리소스를 수정
                - DELETE: 지정된 리소스를 삭제
            - HTTP response status codes: 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄
                1. Informational responses(100 - 199)
                2. Successful responses(200 - 299)
                3. Redirection messages(300 - 399)
                4. Client error responses(400 - 499)
                5. Server error responses(500 -599)
            
        3. 자원의 표현: JSON 데이터(표현되는 데이터 결과물)