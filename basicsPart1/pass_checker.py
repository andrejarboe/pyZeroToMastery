user = input('Username: ')
password = input('Password: ')

scrambled_password = len(password) * '*'

print(f'{user}, your password {scrambled_password} is {len(scrambled_password)} characters long. ')