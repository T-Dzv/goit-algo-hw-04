# option2: working with Exceptions inside main function

def total_salary(path):
    try:
        raw_data = load_data(path)
        salary_list = make_salary_list(raw_data)
        total_salary = sum(salary_list)
        average_salary = int(total_salary / len(salary_list))
        return (total_salary, average_salary)
    except FileNotFoundError:
        return "File is not found"
    except ValueError:
        return "Data in the file is in wrong format"

# read the file and returns a list of lines in the file. 
# if file not found returns "not found" string
def load_data(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()

# convirting raw data list to the list of salaries
# in case if data in original file waan't in expected format, returns "wrong format" string
def make_salary_list(raw_data: list[str]) -> list[int]:
    salaries = []
    for line in raw_data:
        salary = line.split(",")[-1].strip()
        salaries.append(int(salary))
    return salaries
    
# Test cases are below:

# MAIN test case#1 to check if total_salary() function works. Uncomment to check
# path = "task1_test.txt"
# if type(total_salary(path)) != tuple:
#     print(total_salary(path))
# else:
#     total, average = total_salary(path)
#     print(f"Total salary is {total}, average salary is {average}")

# test case#2 - "file not found"
# path = "task_test.txt"
# if type(total_salary(path)) != tuple:
#     print(total_salary(path))
# else:
#     total, average = total_salary(path)
#     print(f"Total salary is {total}, average salary is {average}")

# test case #3 - "wrong format"
# path = "task1_test5.txt"
# if type(total_salary(path)) != tuple:
#     print(total_salary(path))
# else:
#     total, average = total_salary(path)
#     print(f"Total salary is {total}, average salary is {average}")
