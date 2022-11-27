import re

user_input = input('Login / Register: ')
user_password = ''
my_spl_str = '[@_!#$%^&*()<>?/\|}{~:]'
#Check user input is valid or Invalid
if user_input.lower() == 'login' or user_input.lower() == 'register':
    pass
else:
    print("Please enter the valid option(Login/Register) !!")
    exit(0)
#Function used for registration
def make_register():
    get_input_name_email = input('Enter UserName/Email: ')
    split_user_input = get_input_name_email.split('@')

    #Check '@' present in email id
    if split_user_input[0] != '@':
        #loop through email for validation
        for i in range(len(split_user_input[0])):
            #Check email id has special character
            if split_user_input[0][i] in my_spl_str:
                print("Invalid User Name or email id")
                exit(0)
        #Check email id not starting with number
        if re.search("^\d", split_user_input[0]):
            print("Invalid User Name or email id")
            exit(0)
        #Check email id is not empty
        if split_user_input[0] == '':
            print("Invalid User Name or email id")
            exit(0)
        #Check email id is not starts with '.' and also not followed immediate to '@'
        elif split_user_input[0].startswith(".") or split_user_input[1].startswith("."):
            print("Invalid User Name or email id")
            exit(0)
        elif re.search("\.", split_user_input[0]):
            print("Invalid User Name or email id")
            exit(0)
    else:
        print("Invalid User Name or email id")
        exit(0)
    check_password(get_input_name_email)

#Check User Password Function
def check_password(get_input_name_email):
    user_password = input("Enter the password: ")

    #Password should be more than 5 character and less than 16 character
    if len(user_password) < 5:
        print("Enter the Password greater than 5 Character")
        exit(0)
    elif len(user_password) > 16:
        print("Enter Password length less than 16 character")
        exit(0)
    count = 0

    #Check Password has Upper case
    if re.search("[A-Z]", user_password):
        # Check Password has Lower case
        if re.search("[a-z]", user_password):
            # Check Password has a digit
            if re.search("[0-9]", user_password):
                # Check Password has special character
                for i in range(len(user_password)):
                    user_password.split()
                    # print(user_password[i])
                    if user_password[i] in my_spl_str:
                        count += 1
                if count < 1:
                    print("Password does not contain Special Character")
                else:
                    login_file = open("Login_Details.txt", "a")
                    credentials_dict = {
                        get_input_name_email: user_password
                    }
                    # On Successful Password Validation write email id and password in Login_Details.txt file in dictionary format.
                    # Sample File details
                    #{'KK@gmail.com': 'Hello@123'},{'KK1@gmail.com': 'Hello@123'},{'KK1@gmail.com': 'Hello@123'},{'KK2@gmail.com': 'Hello@123'},
                    login_file.write(str(credentials_dict))
                    login_file.write(',')
                    login_file.close()
            else:
                print("Password does not contain number")
        else:
            print("Password does not contain lower case")
    else:
        print("Password does not contain upper case")


if user_input.lower() == 'register':
    make_register()
else:
    get_input_name_email = input('Enter UserName/Email: ')
    user_password = input("Enter the password: ")
    login_file = open("Login_Details.txt", "r")
    user_validation = login_file.read()

    my_tuple = eval(user_validation)
    count = 0
    new_count =0

    # Loop through the file to get the email id and password
    for i in my_tuple:
        count += 1
        for key, value in i.items():

            if get_input_name_email == key and user_password == value:
                print("Login Success")
                exit(1)
            elif len(my_tuple) == count:
                print("Invalid User Name/Password")
                user_new_input = input("Input 1 to opt Forgot Password, 2 for Register: ")

                # Forgot Password
                if user_new_input == '1':
                    get_input_name_email = input('Enter UserName/Email: ')

                    #Loop through the email id to confirm the existance.
                    for j in my_tuple:
                        new_count += 1
                        for new_key , new_val in j.items():

                            # Check the user given email id exist in Login_Details.txt. Then get the user password else new password can be set by user
                            if get_input_name_email == new_key:
                                print("Do you want us to get old Password? If yes type Y. Else you can enter new password")
                                old_new_pass_ques = input()
                                if old_new_pass_ques.lower() == 'y':
                                    print("Your Password: ", value)
                                    exit(0)
                                else:
                                    check_password(get_input_name_email)
                                    exit(0)

                            elif len(my_tuple) == new_count:
                                print("Invalid User Name or email id")
                                final_user_input = input("Do you want to register? (Y/N) :")
                                if final_user_input.lower() == 'y':
                                    make_register()
                                else:
                                    print("Note: Given UserName/Email id does not exists in system. Please go through new registration")
                else:
                        make_register()