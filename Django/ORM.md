ORM(Object-Relational-Mapping)
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술
- 역할: Django와 DB간에 사용하는 언어가 다르기 때문에 소통 불가, Django에 내장된 ORM이 중간에서 이를 해석
- QuerySet API
  - ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는 데 사용하는 도구
  - API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리
  - 구문: Model class / Manager / Queryset API
    - ex. Article.objects.all() - 전체 게시글 조회
    - Query
      - 데이터베이스에 특정한 데이터를보여달라는 요청
      - 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달
        - QuerySet
          - 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
          - 순회가 가능한 데이터로써 1개 이상의 데이터를불러와 사용 가능
          - Django ORM을 통해 만들어진 자료형
          - 데이터베이스가 단일 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환
          - QuerySet API: python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장(C), 조회(R), 수정(U), 삭제(D)하는 것
            - CRUD: 소프트웨어가 가지는 기본적인 데이터 처리 기능. Create(저장), Read(조회 - 단일/전체), Update(갱신), Delete(삭제)
            - Django shell: Django 환경 안에서 실행되는 python shell(입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침)
              - save(): 객체를 데이터베이스에 저장하는 인스턴스 메서드
              - all(): 전체 데이터 조회
              - filter(): 주어진 매개변수와 일치하는 객체를 포함하는 QuerySet 반환(값 없어도 QuerySet으로 반환)
              - get(): 주어진 매개변수와 일치하는 객체를 반환(결과가 여러개면 반환 x)
                - primary key와 같이 고유성을 보장하는 조회에서 사용해야 함(id(pk))
              - delete(): 객체를 데이터베이스에서 삭제(Django는 삭제된 id를 재사용x)
              - Field lookups: Query에서 조건을 구성하는 방법, filter, exclude, get에 대한 키워드 인자로지정됨
- ORM, QuerySet API 사용 이유
  - 1. 데이터베이스 추상화: 개발자는 특정 데이터베이스 시스템에 종속되지 않고 일관된 방식으로 데이터를 다룰 수 있음
    2. 생산성 향상: 복잡한 SQL 쿼리를 직접 작성하는 대신 Python 코드로 데이터베이스 작업을 수행할 수 있음
    3. 객체 지향적 접근: 데이터베이스 테이블을 Python 객체로 다룰 수 있어 객체 지향프로그래밍의 이점을 활용할 수 있음