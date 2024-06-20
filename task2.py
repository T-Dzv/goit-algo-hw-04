def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw_data = f.readlines()
            cats_info = []
            for line in raw_data:
                id, name, age = line.strip().split(",")
                cats_info.append({
                    "id": id,
                    "name": name,
                    "age": age
                })
            return cats_info
    except FileNotFoundError:
        return "File is not found"
    except ValueError:
        return "Data in file is in wrong format"
    
# Test-case 1 to check if function works. Uncomment to check 
# path = "task2.txt"
# for cat in get_cats_info(path):
#     print(cat)

# test-case 2 - file not found
# path = "task.txt"
# print(get_cats_info(path))

#test-case 3 - wrong format
# path = "task2_test.txt"
# print(get_cats_info(path))