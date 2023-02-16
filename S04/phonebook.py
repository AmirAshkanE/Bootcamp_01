# is_running = True
# phonebook = []

# while is_running:
#     contact = input("Insert contact or quit: ")
#     if contact.lower() !="quit":
#         phonebook.append(contact)
#     else:
#         print(phonebook)
#         is_running = False
# phonebook = []
# temp_dic = {}
# while True:
#     contact_name = input()
#     if contact_name.lower() == "exit":
#         break
#     else:
#         phone_number = input()
#         temp_dic.update({contact_name : phone_number})
        

# phonebook = temp_dic.items()       
# print(phonebook)

phonebook = {}

while True:
    command = input("Please input instructions(add/ remove/ search/ show/ exit)")
    if command == "exit":
        break
    elif command == "add":
        name = input("Please enter new name: ")
        phone_number = input(f"Please enter {name}'s phone number: ")
        phonebook.update({name:phone_number})
    elif command == "show":
        print(phonebook)
    elif command == "remove":
        name = input("enter the the name of the contact you wish to remove: ")
        phonebook.pop(name)
    elif command == "search":
        name = input("enter the the name of the contact you wish to search: ")
        print(f"{name} : {phonebook[name]}")
