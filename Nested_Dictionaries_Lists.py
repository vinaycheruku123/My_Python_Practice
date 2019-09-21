print('Going to practise Nested Dictionaries and lists')

allGuests = {'Alice':{'apples':5, 'pretzels':12},
             'Bob':{'chicken sandwiches':3, 'apples':2},
             'Carol':{'cups':3, 'apple pies':1}}

def totalBrought(guests, item):

    numBrought = 0

    for k,v in guests.items():

        numBrought += v.get(item,0)

    return numBrought

print('Number of things being brought: ')

print(' - Apples    '+str(totalBrought(allGuests, 'apples')))
print(' - Cups    '+str(totalBrought(allGuests, 'cups')))
print(' - Cakes    '+str(totalBrought(allGuests, 'cakes')))
print(' - chicken sandwiches    '+str(totalBrought(allGuests, 'chicken sandwiches')))
