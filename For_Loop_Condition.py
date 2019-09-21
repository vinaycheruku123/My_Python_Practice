print('This is For Loop Condition Practise Code ')
print('==========================================')

i = 0

for i in range(1,-10,-1):
    
    if i == 7:
        
        print('You have entered number 7. ')
        print('Skipping Number 7 ')

        continue
    
    elif i == 9:

        print('You have entered number 9. ')
        print('Exiting ')

        break
    
    print('My Name is Vinay '+'('+str(i)+') ')

print('For loop completed ')
