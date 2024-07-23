# 딕셔너리를 변수 하나로 패킹했을 때 튜플의 형태
person = {'name' : 'Alice', 'age' : 25}
for item in person.items():
    print(item)                 
                                # ('name', 'Alice')
                                # ('age', 25)

# 변수를 두개 주면  각각을 얻을 수 있다.
for key, value in person.items():
    print(key)
    print(value)                    
                                    # name
                                    # Alice
                                    # age  
                                    # 25  
                                                                        