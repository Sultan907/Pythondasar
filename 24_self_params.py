class person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
        
    def myFunc(abc):
        print("Hello my name is " + abc.name)
        
p1 = person("john", 36)
p1.myFunc()