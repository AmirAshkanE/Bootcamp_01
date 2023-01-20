username1 = "ashkan"
password1 = "1371"

username2 = "tina"
password2 = "6289"

user_input = input("input the username: ")
pass_input = input("input the password: ")

# if user_input == username1:
#     if pass_input == password1:
#         print("Login succesful!")
#     else
#         print("Login failed!")
# else:
#     print("Login Failed!")

# if (user_input == username1 and pass_input == password1) or (user_input == username2 and pass_input == password2):
#     print(f"Welcome User {user_input}")
# else:
#     print("Invalid User ID")
    
if user_input == username1 and pass_input == password1:
    print(f"Welcome User {user_input}")
elif user_input == username2 and pass_input == password2:
    print(f"Welcome User {user_input}")
else:print("Invalid User ID")
    
