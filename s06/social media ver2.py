people = []
find_counter=0
for i in range(1,1000000):
    try:
        command, *data = input().split()  # *data what ever is left is set to data
        if command == "Add":
            username, gender, age, id = data
            people.append([username,gender,age,id])
            print(f"User {id} added successfully")
        elif command == "Find":
            find_counter+=1
            id = data[-1]
            result= sorted(list(filter(lambda x: x[-1].startswith(id), people)),key= lambda x: x[-1])[:10]
            if len(result) == 0:
                print(f"{find_counter} No user found")
            else:
                for p in result:
                    print(f"{find_counter} {p[0]} {p[1]} {p[2]} {p[3]}")    
            
        elif command == "info":
            print(people)
    except:
        break