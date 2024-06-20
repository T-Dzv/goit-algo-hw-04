# option1: working with Exceptions inside partial functions (which could be in separate module in real project)

def total_salary(path):
    raw_data = load_data(path)
    if type(raw_data) != list:
        return raw_data
    salary_list = make_salary_list(raw_data)
    if type(salary_list) != list:
        return salary_list
    total_salary = sum(salary_list)
    average_salary = int(total_salary / len(salary_list))
    return (total_salary, average_salary)

# read the file and returns a list of lines in the file. 
# if file not found returns "not found" string
def load_data(path: str) -> list[str]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return "File is not found"

# convirting raw data list to the list of salaries
# in case if data in original file waan't in expected format, returns "wrong format" string
def make_salary_list(raw_data: list[str]) -> list[int]:
    salaries = []
    try:
        for line in raw_data:
            salary = line.split(",")[-1].strip()
            salaries.append(int(salary))
        return salaries
    except ValueError:
        return "Data in the file is in wrong format"

#Test cases are below:

# test case#1 to check if total_salary() function works. Uncomment to check
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
