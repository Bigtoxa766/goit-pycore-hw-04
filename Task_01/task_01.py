from pathlib import Path

base_path = Path('D:\Woolf\PyhthonProjects\goit-pycore-hw-04\Task_01')
salary_file_path = base_path / 'salary_file.txt'


def total_salary(path):
    try:
        total = 0

        with open(path, 'r', encoding="utf-8") as file:
            res = file.readlines()
            total_emploee = len(res)

            for empl in res:
                salary = int(empl.split(',')[1])
                total +=  salary

            print(f'Total salary: {total}')
            print(f'Average salary: {total / total_emploee}')
    except:
        print('There is no such path')

total_salary(salary_file_path)