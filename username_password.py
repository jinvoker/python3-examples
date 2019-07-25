username='user'
password='pass'
login=input('Login with username :')

if login==username:
    passentry=input('Enter password for '+username+' : ')
    if passentry==password:
        print('Access granted : ')

    else:
        print('wrong password try again ')

else:
    print('I dont know you.')
