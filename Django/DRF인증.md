- Authentication(인증): 수신된 요청을 해당 요청의 사용자 또는 자격 증명과 연결하는 메커니즘 - 누구인지를 확인하는 과정
  - 응답
    - HTTP 401 Unauthorized: 요청된 리소스에 대한 유효한 인증 자격 증명이 없음
    - HTTP 403 Forbidden(Permission Denied): 서버에 요청이 전달되었지만 권한 때문에 거절, 서버는 클라이언트가 누구인지 알고 있음
  - 인증 정책 설정: 전역 설정(DEFAULT_AUTHENTICATION_CLASSES 사용), View 함수 별 설정(authentication_classes 데코레이터)
  - 인증 체계: BasicAuthentication, TokenAuthentication, SessionAuthentication, RemoteUserAuthentication
    - TokenAuthentication: 서버가 인증된 사용자에게 토큰을 발급하고 사용자는 매 요청마다 발급받은 토큰을 요청과 함께 보내 인증 과정을 거침 - 기본 데스크톱 및 모바일 클라이언트와 같은 클라이언트-서버 설정에 적합
      1. 사용자 로그인(클라이언트 -> 서버)
      2. 사용자 확인(서버 <-> DB)
      3. Token 발급(서버)
      4. 응답(서버 -> 클라이언트)
      5. 데이터 요청(+ Token)(클라이언트 -> 서버)
      6. Token 검증(서버)
      7. 응답(+ 요청 데이터)(서버 -> 클라이언트)
  - Dj-Rest-Auth: 회원가입, 인증(소셜미디어 인증 등), 비밀번호 재설정, 사용자 세부 정보 수정, 회원 정보 수정 등 다양한 인증 관련 기능을 제공하는 라이브러리

- Permissions(권한): 요청에 대한 접근 허용 또는 거부 여부를 결정
  - 순서 상 인증이 먼저 진행. 인증 자체로는 들어오는 요청을 허용하거나 거부할 수 없으며, 단순히 요청에 사용된 자격 증명만 식별
  - 권한 정책 설정: 전역 설정(DEFAULT_PERMISSION_CLASSES 사용), View 함수 별 설정(permission_classes 데코레이터)
  - 권한 정책: IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly ...
    - IsAutenticated: 인증되지 않은 사용자에 대한 권한을 거부하고 그렇지 않은 경우 권한을 허용 - 등록된 사용자만 API에 액세스할 수 있도록 하려는 경우 적합