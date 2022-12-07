import json 

def capture_user_info():
    name = input("Please enter your name: ")
    last_name = input("Please enter your last name: ")
    age = int(input("Please enter your age: "))

    user_info = {
        "name": name,
        "last_name": last_name,
        "age": age
    }

    return user_info

def store_user_info(user_info):
    with open("user_info_json","r") as json_file:
        data = json.load(json_file)
        data.append(user_info)
    with open("user_info_json","w") as json_file:
        json.dump(data,json_file)  



while True:
     user_choice = input("Would you like to store your information in a JSON file (a), or exit the program(x): ")

     if user_choice == "a":
         user_info = capture_user_info()
         store_user_info(user_info)
     elif user_choice == "x":
            break
     else:
      print("Invalid option. Enter a or x")

    


    

