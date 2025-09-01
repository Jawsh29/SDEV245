# This program demonstrates a simple user login program with defined admin and user accounts that have different
# levels of access

# Define user data
admin_user = "admin1"
admin_pass = "superdog"
user_name = "user1"
user_pass = "redsox"
admin_data = [1, 2, 3, 4, 5]
user_data = [0, 0, 0, 0, 0]

# Authorization Functions
def user_auth():
    """Function to authenticate username and password for 'user'"""
    ask_username = str(input("Enter username: "))
    if ask_username == user_name:
        print("User recognized ")
        ask_password = str(input("Enter password: "))
        if ask_password == user_pass:
            print("Login successful")
        else:
            print("Incorrect password")
            user_auth()
    else:
        print("Invalid username ")
        user_auth()


def admin_auth():
    """Function to authenticate username and password for 'admin'"""
    ask_username = str(input("Enter username: "))
    if ask_username == admin_user:
        print("User recognized ")
        ask_password = str(input("Enter password: "))
        if ask_password == admin_pass:
            print("Login successful")
        else:
            print("Incorrect password")
            admin_auth()
    else:
        print("Invalid username ")
        admin_auth()

# Login Function
def login():
    """Login function to determine type of login and display relevant data"""
    login_type = input("Type 'admin' for admin login or 'user' for user login: ")
    if login_type == "admin":
        admin_auth()
        print("Displaying Admin Data")
        for i in admin_data:
            print(i)
    elif login_type == "user":
        user_auth()
        print("Displaying User Data")
        for i in user_data:
            print(i)
    else:
        print("Invalid login")
        login()


login()
