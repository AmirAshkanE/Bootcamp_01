command_list = []
contact_list = []
find_count = 1
i = 0

for i in range(1,10):
    try:
        command_input = input()
        for command in command_list:
            action = command.split()
            data_base = {}
            if "Add" in action:
                user_name, user_gender, user_age, user_id = action[1:]
                if len(user_id) in range(5, 11):
                    data_base.update(
                        {"name": user_name, "gender": user_gender, "age": user_age, "id_number": user_id})
                    id_value = data_base["id_number"]
                    print(f"User {id_value} added successfully")
                    contact_list.append(list(data_base.values()))
                    contact_list.sort()
                else:
                    continue
            elif "Find" in action:
                c_count = 0
                search_criteria = action[1]
                search_count = 0
                for contact in contact_list:
                    for con in contact:
                        if search_criteria.capitalize() in con or search_criteria in con:
                            result = " ".join(contact)
                            if c_count < 10:
                                print(find_count, result)
                                c_count += 1
                            search_count += 1
                if search_count == 0:
                    print(f"{find_count} No user found")
                find_count += 1
    except:
        break