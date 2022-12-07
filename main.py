import json

def capture_user():
    users = []

    name = input("Please enter your name:")
    last_name = input("Please enter your last name:")
    age = int(input("Please enter your age:"))

    user_info = {
        "name": name,
        "last_name": last_name,
        "age": age
    }

    users.append(user_info)

    return users

    
def main():

    users = capture_user()

    with open("user_info.json", "w") as file:
        json.dump(users,file)


if __name__ == "__main__":
    main()
