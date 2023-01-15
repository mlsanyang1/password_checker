#input('mlsanyang')
#input('@marine')

#print('{username}, your password {*******}, is {7} letters long')

#print('*' * 7)
#user_name =('mlsanyang')
#password =('@marine')
#pass_length = len(password)

user_name = input ('what is your username?')
password = input('what is your password?')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{user_name} your password, {hidden_password}, is {password_length} letters long')