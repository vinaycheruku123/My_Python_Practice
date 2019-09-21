def returnDivision(divideBy):
    
    try:
    
        return 40/divideBy
    
    except ZeroDivisionError:
        
        print('Invalid Argument')

print(returnDivision(10))
print(returnDivision(0))
print(returnDivision(20))
