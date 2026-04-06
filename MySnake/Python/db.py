import sqlite3
import os
"""показывает полный путь расположения нашего,
файла в котором мы работаем """
print(__file__)

os.chdir(os.path.dirname(__file__))

print("Current working directory",os.getcwd())