import os
from pathlib import Path

current_dir = Path.cwd()
if Path.cwd().name.endswith('PYTHON'):
    first_dir = Path(current_dir)
    solution_dir = (
        current_dir
        /'Python'
        /'IOfiles'
        /'solutions'
    )
    os.chdir(solution_dir)

with open(r"C:\Users\roxfo\OneDrive\PYTHON\Python\03.01.2024IOfiles\data\task1.txt") as file:
      print(file.read())

"""*******************************************"""
file = Path('foo.txt')#создаем файл foo.txt"""
file.open('w').write('Some text')

new=Path('bar.txt')
"""соэдаем новый файл """
file.replace(new)#
"""заменяем на bar.txt файл"""
print(new.open().read())

 
print(__file__)
file=Path(__file__)
print(file.resolve())
"""resolve()--показывает полный путь к 
к файлу в котором работаем"""


"""создаем новый файл и добавляем запись"""
new = Path('new.py')
new.touch()
new.open('w').write('This is my my hjhbsnrjfs')
"""unlink() -- это удаление файла"""
new.unlink()
#for file in solutions.glob('**/*.py'):
#     print(file)