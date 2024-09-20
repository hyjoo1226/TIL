Django Model
- DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
- 테이블 구조를 설계하는 청사진(blueprint)
- model class
    - ```python
        # articles/models.py
        from django.db import models

        class Article(models.Model):
            title = models.CharField(max_length=10)
            content = models.TestField()
    - 위 코드는 id, title, content 필드를 가진 테이블 구조를 만든다(id필드는 Django가 자동 생성)
    - django.db.models 모듈의 Model이라는 부모 클래스를 상속받음
    - 개발자는 가장 중요한 테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록
    - 클래스 변수명: 테이블의 각 필드(열) 이름(title, content ...)
    - Model Field
        - DB 테이블의 열을 나타내는 중요한 구성 요소, 데이터의 유형(Field types)과 제약조건(Field options)을 정의
        - Field Types
            - 데이터베이스에 저장될 테이터의 종류를 정의(models 모듈의 클래스로 정의되어 있음)
            - 주요 필드 유형: 문자열 필드, 숫자 필드, 날짜/시간 필드, 파일 관련 필드(models.CharField, IntegerField, DateField, FileField ...)
                - CharField(): 제한된 길이의 문자열을 저장, 필드의 최대 길이를 저장하는 max_length는 필수 옵션
                - TextField(): 길이 제한이 없는 대용량 텍스트를 저장(무한대는 아니며 사용하는 시스템에 따라 달라짐)
        - Field Options
            - 필드의 동작과 제약조건을 정의
            - 주요 필드 옵션
                - null: 데이터에비으세어 NULL 값을 허용할지 여부를 결정
                - blank: form에서 빈 값을 허용할지 여부를 결정
                - defalut: 필드의 기본값을 설정
                - DateTimeField
                    - auto_now: 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장(수정일)
                    - auto_now_add: 데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장(작성일)
            - 제약 조건(Constraint): 특정 규칙을 강제하기 위해 테이블의 열이나 행에 적용되는 규칙이나 제한사항(ex. 숫자만 저장되도록, 문자가 100자 까지만 저장되도록(max_length=100))

- Migrations
    - model 클래스의 변경사항(필드 생성, 수정, 삭제 등)을 DB에 최종 반영하는 방법
    - model class(설계도 초안) -(makemigrations)-> migration 파일(최종 설계도) -(migrate)-> db.sqlite3(DB)
        - ```python
            python manage.py makemigrations
            python manage.py migrate
    - model 클래스에 변경사항이 생겼다면 반드시 새로운 설계도를 생성하고, 이를 DB에 반영해야 한다
        - 기존 필드의 기본 값 설정이 필요
        - 새로 만든 설계도가 있다해서 기존 설계도를 삭제하면 안됨(반드시 설계도끼리 연결되는건 아니지만 기존 설계도에 덧붙여서 만들어진 설계도도 있으므로)
    - 기타 명령어
        - ```python
            python manage.py showmigrations

            # migrations 파일들이 migrate 됐는디 여부를 확인하는 명령어. x표시면 완료된 것
        - ```python
            python manage.py sqlmigrate articles 0001
            
            # 해당 migrations 파일이 SQL 언어로 어떻게 번역되어 DB에 전달되는지 확인하는 명령어
    - 데이터베이스 초기화
        - 1. migration 파일 삭제
          2. db.sqlite3 파일 삭제

- Automatic admin interface
    - Django가 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스
    - 데이터 확인 및 테스트 등을 진행하는데 매우 유용
    - migratins이 선행되어야 함(계정 저장을 위해서 테이블을 생성해야 하므로)
    - 1. admin 계정 생성
        - ```python
            python manage.py createsuperuser
        - auto_user 테이블에서 확인
      2. admin에 모델 클래스 등록
        - ```python
            # articles/admin.py
            from django.contrib import admin
            from .models import Article

            admin.site.register(Article)
