
import re

global name,username,final_username

name =input('hello user enter  your name : \n')
username=None
user_choice = input(f"{name}, your default username will be set as '{name}'. "
                        f"Press 'n' to change or 'y' to continue:\n")
if user_choice.lower() == 'n':
    print(f"welcome{final_username}")
elif user_choice.lower() == 'y':
    final_username = name
def change_name():
    global temp_name
    temp_name = input("do you want to change the username? if yes then please enter below :\n")
    return temp_name

final_username =change_name()

def validate_details(final_username, email, password):
    # Define patterns
    username_pattern = r'^[a-zA-Z0-9_]{3,20}$'
    pw_pattern = r'^[a-zA-Z0-9_ @.]{8,20}$'
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check against the patterns
    check_email = re.match(email_pattern, email)
    check_username = re.match(username_pattern, username)
    check_password = re.match(pw_pattern, password)

    if check_email and check_password and check_username:
        print('Login successful')
    else:
        print('Something is wrong. Check your login details.')


    validate_details(final_username, email, password)

    
