class Father:
    def __init__(self, name):
        self.name = name
        self.gender = "Male"
        self.__money = 0  # encapsulation

    # def add_money(self, amount):
    #     self.__money += amount

    # def spend_money(self, amount):
    #     if amount < 10:
    #         self.__money -= amount
    #     else:
    #         print("I don't have money")

    @property
    def money(self):
        return self.__money - 1000
    
    @money.setter
    def money(self, amount):
        if amount > 0:
            self.__money = amount
        return self.__money

    def say_hello(self):
        print(f"hello i'm {self.name} and i'm father")


class Mother:
    def __init__(self, name):
        self.name = name
        self.gender = "Female"

    def say_hello(self):
        print(f"hello i'm {self.name} and i'm mother")


class Student(Father, Mother):
    def __init__(self, n, id):
        self.studen_id = id
        # super(Father,self).__init__(n)     python 2 way of calling a parent
        # super() refers to the parent class
        # everything in parent's init function is inhereted
        Mother.__init__(self, n)

    def say_hello(self):
        print(
            f"hello i'm {self.name} and i'm a {'boy' if self.gender=='male' else 'girl' }")


f = Father("mohammad")
m = Mother("mahdieh")
s = Student("ali", 123)

# s.say_hello()

# f.add_money(210)
f.money = -2000
print(f.money)