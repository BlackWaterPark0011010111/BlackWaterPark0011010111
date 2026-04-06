import os

def redir():
    print(os.getcwd())
    if os.getcwd().endswith('PYTHON'):
        os.chdir(r'C:\Users\roxfo\OneDrive\PYTHON\Python\IOfiles\solutions') 
