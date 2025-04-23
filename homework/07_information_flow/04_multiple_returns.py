def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address : str = input("What is your email address?: ")
    
    userinfo = {
        "first_name": first_name,
        "last_name": last_name,
        "email_address": email_address
    }

    return userinfo


    
def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
     main()
     