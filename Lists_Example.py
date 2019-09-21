print('WOrking with List Types')

catNames = []

while True:
    name = input('Enter cat name else leave it ')

    if name == '':
        break
    else:
        catNames += [name]

print('Here are the cat Names')

for name in catNames:
    print(name, sep = ',')
