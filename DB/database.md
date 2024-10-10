데이터베이스: 데이터를 저장하고 조작(CRUD)
- 관계형 데이터베이스: 데이터 간에 관계가 있는 데이터 항목들의 모음
    - 서로 관련된 데이터 포인터를 저장하고 이에 대한 액세스를 제공, 이 관계로 인해 두 테이블을 사용하여 데이터를 다양한 형식으로 조회할 수 있음
    - 각 데이터에 고유한 식별 값 부여 -> 기본 키(Primary Key)
    - 다른 테이블에 고유한 식별 값 저장 -> 외래 키(Foreign Key)
    - RDBMS(Relational Database Management System)
        - SQLite, MySQL, Oracle Database, PostgreSQL 등
- SQL(Structure Query Language): 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
    - SQL 키워드 대문자 작성 권장, 세미콜론으로 문장 종료
    - SQL Statements
        1. DDL(Data Definition Language) - 데이터 정의 - CREATE, DROP, ALTER
        2. DQL(Data Query Language) - 데이터 검색 - SELECT
        3. DML(Data Manipulation Language) - 데이터 조작 - INSERT, UPDATE, DELETE
        4. DCL(Data Control Language) - 데이터 제어 - COMMIT, ROLLBACK, GRANT, REVOKE