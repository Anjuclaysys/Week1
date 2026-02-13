from api_fetch import fetch_users
from formatter import format_users

def main():
    user_json = fetch_users()[0:5]
    if not user_json:
        print("no user fetched")
        return
    
    users = format_users(user_json)

    for user in users:
        print(user)
        print(user.get_details())
        print('----------------------')

if __name__ == "__main__":
    main()

