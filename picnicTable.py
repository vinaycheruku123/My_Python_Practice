picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':8000}

def printPicnic(itemDic, leftWidth, rightWidth):

    print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
    
    for k,v in itemDic.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))

printPicnic(picnicItems, 10, 5)
printPicnic(picnicItems, 20, 6)
