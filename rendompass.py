'''This is a simple pasword generator'''
import string,random
def validate_guess(user_choice):
    if len(user_choice) != 1:
        print('Please Enter Only Single Letter')
        return False
    elif not user_choice.isalpha():
        print('Please Enter a Letter')
        return False
    elif user_choice.lower() not in ['y','n']:
        print('please enter only "y" or "n"')
        return False
    else:
        return True
def password_generator():
    password_set = string.ascii_uppercase+string.digits+string.ascii_lowercase+string.punctuation+string.ascii_letters
    password=''.join(random.choice(password_set) for i in range(12))
    return password

def main_pass(passgen):
    generated_password=password_generator()
    while True:
        view_password =input('Do you want to view generated password? \n input-y/n : >>')
        if not validate_guess(view_password):
            continue
        if view_password == 'y':
            print(f'The Generated password is >>  {generated_password}')
            print(f'you are generating total{passgen} number of password')
            pass_genmore = input('Do you want generated more password? \n input-y/n : >>')
            if validate_guess(pass_genmore) == True:
                if pass_genmore == 'y':
                    main_pass(passgen+1)
                else:
                    print('Thank you for your choice')
                    print(f'you are generating total{passgen} number of password')
                    break
            else:
                validate_guess(input('Invalid Input? \n input-y/n : >>'))
        else:
            print('thank you for your concern')
            print(f'you are generating total{passgen} number of password')
            break
            
main_pass(1)