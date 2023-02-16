class Person:
    def __init__(self, name, number, address):
        self.person_name = name
        self.person_number = number
        self.person_add = address

    def info(self):
        return f"this is {self.person_name}, phone: {self.person_number}, address: {self.person_add}"

    def __repr__(self):
        return str((self.person_name,self.person_number,self.person_add))


class PhoneBook:
    def __init__(self, name):
        self.list_name = name
        self.contact_list = []

    def add_contact(self, person: Person):
        if not isinstance(person, Person):
            raise Exception("Input type must be person")
        self.contact_list.append(person)

    def remove_contact(self, name):
        # self.contact_list.remove(list(filter(lambda x:x.name == name,self.contact_list))[0])
        for i, p in enumerate(self.contact_list):
            if p.person_name == name:
                self.contact_list.pop(i)
                break

    def show_list(self):
        # for i, p in enumerate(self.contact_list):
        #     print(f"#{i} {p.info()}")
        print(self.contact_list)
    
    def call_person(self,name):
        print(f"calling {next(filter(lambda x:x.person_name == name, self.contact_list)).person_number}")


person_1 = Person("Ashkan", "1234", "Tehran")

my_phonebook = PhoneBook("First")

my_phonebook.add_contact(person_1)

my_phonebook.show_list()

my_phonebook.call_person("Ashkan")