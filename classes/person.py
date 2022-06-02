class person:
    def __init__(self, _name, _age):
      self.name= _name
      self.age = _age

    def sayHi(self):
        print('Hello, my name is '  + self.name, ' i am ' + self.age + ' years old' )
person1 = person('kendi' ,str(18)) 
person1.sayHi()  

person2 = person('James' ,str(32))
person2.sayHi()