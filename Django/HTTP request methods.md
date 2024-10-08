HTTP: 네트워크 상에서 데이터(리소스)를 주고 받기 위한 약속
- HTTP request methods
  - 데이터에 대해 수행을 원하는 작업(행동)을 나타내는 것
    - 서버에게 원하는 작업의 종류를 알려주는 역할
  - 클라이언트가 웹 서버에 특정 동작을 요청하기 위해 사용하는 표준 명령어
  - 대표 메서드: GET, POST
  - GET Method: 서버로부터 데이터를 요청하고 받아오는 데(조회) 사용
    - 검색 쿼리 전송, 웹페이지 요청, API에서 데이터 조회 등 
    1. 데이터 전송
      - URL의 쿼리 문자열(Query String)을 통해 데이터를 전송
      - https://127.0.0.1:8000/articles/create/?title=제목&content=내용
    2. 데이터 제한
      - URL 길이에 제한이 있어대량의 데이터 전송에는 적합하지 않음
    3. 브라우저 히스토리
      - 요청 URL이 브라우저 히스토리에 남음
    4. 캐싱
      - 브라우저는 GET 요청의 응답을 로컬에 저장할 수 있음
      - 동일한 URL로 다시 요청할 때, 서버에접속하지 않고 저장된 결과를 사용
      - 페이지 로딩 시간을 크게 단축 
  - POST Method: 서버에 데이터를 제출하여 리소스를 변경(생성, 수정,삭제)하는 데 사용 - DB조작
    - 로그인 정보 제출, 파일 업로드, 새 데이터 생성, API에서 데이터 변경 요청 등
    1. 데이터 전송
      - HTTP Body를 통해 데이터를 전송
    2. 데이터 제한
      - GET에 비해 더 많은 양의 데이터를 전송할 수 있음
    3. 브라우저 히스토리
      - POTST 요청은 브라우저 히스토리에 남지 않음 
    4. 캐싱
      - POST 요청은 기본적으로 캐시할 수 없다
      - POST 요청이 일반적으로 서버의 상태를 변경하는 작업을 수행하기 때문
   - Redirect: 서버는 데이터 저장 후 페이지를 응답하는 것이 아닌 사용자를 적절한 기존 페이지로보내야 한다
     - 서버가 클라이언트를 직접 다른 페이지로 보내는 것이 아니라 사용자가 GET 요청을 한번 더 보내도록 응답하는 것
     - redirect(): 클라이언트가 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수

HTTP responsestatus code
  - 서버가 클라이언트의 요청에 대한 결과를 나타내는 3자리 숫자
  - 역할: 클라이언트에게 요청 처리 결과를 명확히 전달, 문제 발생시 디버깅에 도움, 웹 애플리케이션의 동작을 제어하는 데 사용
  - 403 Forbidden: 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
  - CSRF(Cross-Site-Request-Forgery): 사이트간 요청 위조
    - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
    - 요청 시 인증을 위해 CSRF token 필요
      - Django 서버는 해당 요청이 DB에 영향을 주는 요청에 대해 Django가 직접 제공한 페이지에서 데이터를 작성하고 있는 것인지에 대한 확인 수단이 필요한 것
      - 요청 데이터 + 인증 토큰 -> 게시글 작성
      - POST일 때만 token 확인하는 이유
        - POST는 단순 조회를 위한 GET과 달리 특성 리소스에 변경(생성, 수정, 삭제)를 요구하는 의미와 기술적인 부분을 가지고 있기 때문
        - DB에 조작을가하는 요청은 반드시 인증 수단이 필요
        - 데이터베이스에 대한 변경사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것
- new & create view
  - 공통점: 데이터 생성을 구현하기 위함
  - new는 GET method 요청만을, create는 POST method 요청만을 처리
  - 2개의 view 함수를 하나로 구조화
- edit과 update view 함수 결합