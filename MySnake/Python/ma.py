import os

def print_directory_structure(path, depth=2, current_depth=0):
    if current_depth < depth:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            print('  ' * current_depth + item)
            if os.path.isdir(full_path):
                print_directory_structure(full_path, depth, current_depth + 1)

path = r"C:\Users\roxfo\Desktop\MySnake\Python\Melting\Melting_down_the_musical_fabric\intro"
print_directory_structure(path, depth=3)
"""
intro(environment.yml,package-lock.json,package.json,backend( app.py ,create_musicxml.py ,package-lock.json ,
requirements.txt ,test_music.py ,uploads folder ,users.db,  __pycache__),
frontend(.env ,.gitignore ,build ,node_modules ,package-lock.json ,package.json ,public ,README.md,src(components
(History.js,
Home.js,Login.js,Register.jsUpload.js),api.js,App.css,App.js,App.test.js,index.js, index.css,RegistrationFord.js,reportWebVitals.js,
setupTest.js )
  
)"""