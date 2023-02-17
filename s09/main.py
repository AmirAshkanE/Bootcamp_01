# overloading operators

# class Date:

#     origin_day_of_week = 4  # 0 is Saturday

#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day

#     def __str__(self):
#         return f"Date(year={self.year},month={self.month},day={self.day})"

#     def get_days(self):
#         return self.day+self.month*30+self.year*360

#     def day_of_week(self):
#         # try to write this yourself
#         return (self.get_days() - Date.origin_day_of_week) % 7

#     def __add__(self, obj):
#         if isinstance(obj, Date):
#             day = self.get_days() + obj.get_days()
#             year = day // 360
#             day = day % 360
#             month = day//30
#             day = day % 30
#             result = Date(0, 0, 0)
#             return Date(year, month, day)

#     def __sub__(self, other):
#         pass


# date1 = Date(1370, 1, 3)
# date2 = Date(1440, 3, 12)
# date3 = Date(10, 3, 1)

# result = date1 + date3

# print(result)

# from datetime import date

# d1 = date(1991,3,23)
# d2 = date(2003,5,10)

# delta_date = d2 - d1
# print(delta_date)

class Card:
    
    _hokm = 0
    _active_suit = 0
    _suits2num = {"♥":0,"♦":1,"♣":2,"♠":3}
    _num2suits = {0:"♥",1:"♦",2:"♣",3:"♠"}
    def __init__(self,number,suit):
        self.number = number
        self.suit = suit
    
    #class method
    @classmethod
    def number_to_suit(cls,number):
        return cls._num2suits[number]
    
    @classmethod
    def suit_to_number(cls,suit):
        return cls._suits2num[suit]
   
    @classmethod
    def set_hokm(cls,hokm):                     # setter def
        if 0 <= hokm < 4:
            cls._hokm = hokm
        else:
            raise Exception("Hokm must be between 0 and 3")
    
    @classmethod
    def set_active_suit(cls,suit):                     # setter def
        if 0 <= suit < 4:
            cls._active_suit = suit
        else:
            raise Exception("Suit must be between 0 and 3")
        
    def __gt__(self,other):
        if self.suit == Card._hokm and other.suit != Card._hokm:
            return True
        elif self.suit == Card._hokm and other.suit == Card._hokm:
            return True if self.number > other.number else False
            # return self.number > other.number
        elif self.suit != Card._hokm and other.suit == Card._hokm:
            return False
        elif self.suit != Card._hokm and other.suit != Card._hokm:
            if self.suit == Card._active_suit and other.suit !=Card._active_suit:
                return True
            elif self.suit == Card._active_suit and other.suit ==Card._active_suit:
                return self.number > other.number
            elif self.suit != Card._active_suit and other.suit ==Card._active_suit:
                return False
            elif self.suit != Card._active_suit and other.suit !=Card._active_suit:
                return self.suit > other.suit
    def __lt__(self,other):
        pass
    
    
# Inheritance

class Father:
    def __init__(self,name):
        self.name = name
        self.gender = "Male"
    
    
    def say_hello(self):
        print(f"hello i'm {self.name} and i'm father")

class Mother:
    def __init__(self,name):
        self.name = name
        self.gender = "Female"

    def say_hello(self):
        print(f"hello i'm {self.name} and i'm mother")
    
class Student(Father,Mother):
    def __init__(self,n,id):
        self.studen_id = id
        # super(Father,self).__init__(n)     python 2 way of calling a parent
        # super() refers to the parent class
        # everything in parent's init function is inhereted
        Mother.__init__(self,n)
    
    def say_hello(self):
        print(f"hello i'm {self.name} and i'm a {'boy' if self.gender=='male' else 'girl' }")
    
    
    
p1 = Father("mohammad")
p2 = Mother("mahdieh")
s = Student("ali", 123)

# print(p1.__dict__)
# print(p2.__dict__)
# print(s.__dict__)
# print(Student.__mro__)              # multiple resolution order method, the order of parents which the class inherits from

s.say_hello()
p1.say_hello()
p2.say_hello()