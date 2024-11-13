SOP(Same-origin policy): 동일 출처 정책
- 어떤 출처(Origin)에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용하는 것을 제한하는 보안 방식
  - 출처(Origin): URL의 Protocol, Host, Post / 세 영역이 일치하는 경우 동일 출처(Same-origin)
- 웹 애플리케이션의 도메인이 다른 도메인의 리소스에 접근하는 것을 제어하여 사용자의 개인 정보와 데이터의 보안을 보호하고, 잠재적인 보안 위협을 방지
- CORS policy: 웹 서버가 리소스에 대한 서로 다른 출처 간 접근을 허용하도록 선택할 수 있는 기능을 제공
  - CORS(Cross-Origin Resource Sharing): 교차 출처 리소스 공유
    - 특정 출처에서 실행중인 웹 애플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제
    - 서버에서 설정되며, 브라우저가 해당 정책을 확인하여 요청이 허용되는지 여부를 결정  
     => 다른 출처의 리소스를 불러오러면 그 출처에서 올바른 CORS header를 포함한 응답을 반환해야 함  
     => 서버에서 CORS header를 만들어야 함
     ``` python
      pip install django-cors-headers

      // settings.py
      INSTALLED APPS = ['corsheaders']

      MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware']

      CORS_ALLOWED_ORIGINS = [
      'http://127.0.0.1:5173',
      'http://localhost:5173',
      ]