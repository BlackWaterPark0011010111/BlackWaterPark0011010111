import os
from pathlib import Path

# print(os.getcwd())
# if os.getcwd().endswith("DCI"):
#     os.chdir("Excercises/IOExcercises/python-basics-io-files/src/solution")

current_dir = Path.cwd()
if Path.cwd().name.endswith("DCI"):
    first_dir = Path(current_dir)
    solution_dir = (
        current_dir
        / "Excercises"
        / "IOExcercises"
        / "python-basics-io-files"
        / "src"
        / "solution"
    )

    os.chdir(solution_dir)


path = "../data/task1.txt"
with open(path) as file:
    print(file.read())