"""
Registration Station project
"""

def read_file(file_name):

    with open(file_name, 'r') as file:
        contents = file.readlines()
    return contents
    


def input_user_name():
    
    username = input("Select username: ")
    return username 


def correct_or_incorrect():
    answer = input("Is this correct? (Y/n): ")
    if answer == "Y" or answer == "y":
        return "correct"
    elif answer == "N" or answer == "n":
        return "incorrect"
   

def correct_details():
    
    file = get_file_contents()
        
    user_details = str(input("Username - Date - Location - Experience: "))
    with open(file,"a") as main_file:
        
        main_file.write(user_details)
        word_list = user_details.split()
        word_list = ' '.join(word_list[2:])
        print(word_list)
        return user_details

   

def get_file_contents():
    return "bootcampers.txt"
    


def find_username(file_name):
    
    username = input_user_name()
    file_name = get_file_contents() 
    file = read_file(file_name)
   
      

    for line in file:
        user_data = line.strip().split(' ')
        if user_data[0] == username:
            data = ' '.join(user_data[2:])
            print(data)
            return data
          
    print("Please enter valid existing username")
    return find_username(file_name)


if __name__ == "__main__":
    registrations_file = get_file_contents()
    information = find_username(registrations_file)
    while True:
        answer = correct_or_incorrect()
        if answer == "correct":
            print(information)
            break
        else:
            correct_details()
