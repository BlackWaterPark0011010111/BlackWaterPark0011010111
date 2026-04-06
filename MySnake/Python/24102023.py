users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]

def get_user(username, password):
    for user in users:
        if user['name'] == username and user['password'] == password:
            break
        else:
            print(' An error occurred. You are not authorized.')
            return None
    
username = input('What is your username? ')
password = input(f"Type the password for username {username}:")

get_user(username, password)

