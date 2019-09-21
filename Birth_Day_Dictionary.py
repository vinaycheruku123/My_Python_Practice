print('I am going to practise Birthday Dictionaries')

birthdays = {'Sahithi': 'Jan28', 'Vinay' : 'Mar6', 'Vishali': 'Apr12'}

for v in birthdays.values():
    print(v)

while True:
    name = input('Enter Name ')
    if name == '':
        break

    if name in birthdays:
        print(name+' birthday is at '+birthdays[name])
    else:
        print('I dont have that name in the dictionary. ')
        date = input('What is their birthday date ')
        birthdays[name] = date
        print('Birthday stored in database ')
        
