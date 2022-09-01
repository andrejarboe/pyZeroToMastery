user = input('Username: ')
password = input('Password: ')

password_length = len(password)
hidden_password = password_length * '*'

print(f'{user}, your password {hidden_password} is {password_length} characters long. ')