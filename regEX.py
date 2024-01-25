#python code for  login verification
import  re #module is used in the validation of user name passwords and emails

username_pattern = r'^[a-zA-Z0-9_]{3,20}$'
pw_pattern =r'^[a-zA-Z0-9_ @.]{8,20}$'
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 

verify_details =re.match(username_pattern,pw_pattern,email_pattern)

def get_user_details():
    name =input('hello user, please enter your name :\n ') #name = default username 
    choice ='n'
    inp =input(f"{name}, will be set as your default name ,press 'n' to change\n:")
    if inp != None:
        new_user_name = input('Enter a new user_name youd like to use ') 
        print(f"welcome {new_user_name}")
    email= input("please enter your registered email address:\n ")
    pass
def validate_login(username,password):
    pass

def validate_details(): 
    pass
