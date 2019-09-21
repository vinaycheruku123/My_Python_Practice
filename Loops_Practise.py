print('Welcome to Loop Practise Code ')
print('===============================')

name = ''

while not name:
    name = input('Who are you? ')

    if name != 'Vinay':
        continue
    else:
        print('Hello Vinay Kumar Cheruku. What is the Password? ')
        password = input()

        if password == 'welcome':
            break;
        else:
            continue
print('Access Granted !!! ')
    
