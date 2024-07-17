# 1. Positional Arguments(위치 인자)
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice', 25)
greet(25, 'Alice')

# 2. Default Argument Values(기본 인자 값)
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')
greet('Charlie', 40)

# 3. Keyword Arguments(키워드 인자)
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35)
greet(age=35, name='dave')
# greet(age=35, 'Dave') #실행안됨

# 4. Arbitrary Argument Lists(임의의 인자 목록) 여러개의 인자를 받아 tuple로 처리
def calculate_sum(*args):
    print(args)
    print(type(args))

calculate_sum(1, 100, 5000, 30)

# 5. Arbitrary Keyword Argument Lists(임의의 키워드 인자 목록) 여러개의 인자를 dictionary로 묶어 처리
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30) #{'name': 'Eve', 'age': 30}

# 인자의 모든 종류를 적용한 예시
# 위치 -> 기본 -> 가변 -> 가변 키워드의 순서가 대체로 좋다
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')