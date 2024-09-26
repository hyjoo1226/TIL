Static Files: 정적 파일
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일(이미지, JS, CSS 파일 등)
- 웹 서버의 기본동작은 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서 응답(HTTP response)을 처리하고 제공하는 것 -> 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공 -> 정적 파일을 제공하기 위한 경로(URL) 필요
- 경로
  - STATIC_URL: 기본 경로 및 추가 경로에 위치한 정적 파일을 참초하기 위한 URL, 실제 파일이나 디렉토리경로가 아니며 URL로만 존재(settings.py에서 설정)
    - URL + STATIC_URL + 정적파일 경로(http://127.0.0.1:8000/static/articles/sample-1.png)
  - 기본 경로: app폴더/static/
    - static tag 사용: {% load static %}
    - 해당 페이지에서만 적용, 부모템플릿에 했다 해서 자식도 적용x
  - 추가 경로: STATICFILES_DIRS에 문자열 값으로 추가 경로 설정(settings.py에서 설정)
    - STATICFILES_DIRS: 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트

- Media Files: 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
  - ImageField(): 이미지 업로드에 사용하는 모델 필드, 이미지 객체가 직접DB에 저장되는 것이 아닌 이미지 파일의 경로 문자열이 저장됨(pip install pillow 해야 사용 가능)
  - 사전 준비: settings.py에 MEDIA_ROOT, MEDIA_URL 설정, 작성한MDEIA_ROOT, MEDIA_URL에 대한 URL 지정
  - MEDIA_ROOT: 미디어 파일들이 위치하는 디렉토리의 절대 경로
  - MEDIA_URL: MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성(STATIC_URL과 동일한 역할)