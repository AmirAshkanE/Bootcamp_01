# oop

class Student:                                          # since all classes inherit from the base object class init constructor will be called by default if not made manually.

    country = "Iran"

    def __init__(self,name,id) -> None:
        self.name1 = name
        self.id1 = id

    def __repr__(self) -> str:
        return f"student object"
    
    def __str__(self) -> str:
        return f"str method from object "

    def say_hello(self):
        # print(self)
        return f"hello! {self.name1}"
    
 
    def say_goodbye(self):
        return f"good bye!"

a = Student("ashkan","1234")
b = Student("tina","4321")



print(a.say_hello())
print(b.say_hello())

# print(hex(id(a)))
# print(hex(id(b)))

print(str(a))
print(a)