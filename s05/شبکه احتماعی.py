# SOLUTION 1

people = {}
find_counter=0
while True:
    command, *data = input().split()  # *data what ever is left is set to data
    if command == "Add":
        username, gender, age, id = data
        people.update({id:[username,gender,age]})
        print(f"User {id} added successfully")
    elif command == "Find":
        find_counter+=1
        id = data[0]
        if id in people.keys():
            pass
        
        else:
            sub_people={}
            for saved_id in people.keys():
                if saved_id.startswith(id):
                    if len(sub_people)>=10:
                        break
                    sub_people.update({saved_id:peopl[saved_id]})
            if len(sub_people)==0:
                print(f"{find_counter} No user found")
            for key in sorted(list(sub_people.keys())):
                print(f"{find_counter} {sub_people[key][0]} {sub_people[key][1]} {sub_people[key][2]}")
    elif command == "info":
        print(people)
# **************************************************************************
# SOLUTION 2
people = []
find_counter=0
while True:
    command, *data = input().split()  # *data what ever is left is set to data
    if command == "Add":
        username, gender, age, id = data
        people.append([username,gender,age,id])
        print(f"User {id} added successfully")
    elif command == "Find":
        find_counter+=1
        id = data[0]
        sub_people={}
        for saved_id in people.keys():
            if saved_id.startswith(id):
                if len(sub_people)>=10:
                    break
                sub_people.update({saved_id:peopl[saved_id]})
        if len(sub_people)==0:
            print(f"{find_counter} No user found")
        for key in sorted(list(sub_people.keys())):
            print(f"{find_counter} {sub_people[key][0]} {sub_people[key][1]} {sub_people[key][2]}")
    elif command == "info":
        print(people)