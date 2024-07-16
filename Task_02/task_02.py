from pathlib import Path

base_path = Path('D:\Woolf\PyhthonProjects\goit-pycore-hw-04\Task_02')
path_to_cats_file = base_path / 'cats_file.txt'

def get_cats_info(path):
    cats_info_dict = {}
    cats_info = []
    
    with open(path, 'r', encoding="utf-8") as file:
        res = file.readlines()

        for el in res:
            subject = el.split(',')
            cats_info_dict.update({'id': subject[0], 'name': subject[1], 'age': subject[2]})
            cats_info.append(cats_info_dict)
            
        print(cats_info)
          

get_cats_info(path_to_cats_file)