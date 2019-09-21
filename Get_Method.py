print('Working on Get Method ')

picnicItems = {'apples':5, 'cups':2}

for a,b in picnicItems.items():
    print('Key '+a+' Value '+str(b))

print('I am bringing '+str(picnicItems.get('water', 0))+' cups for the party')
