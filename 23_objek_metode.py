class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myFunc(self):
        print("Hello my name is " + self.name)
        
p1 = person("john", 36)
p1.myFunc()