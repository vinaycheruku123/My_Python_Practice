print('Learning Local and Global Variables ')
print('=====================================')

a = 0

x = input('Enter a number')

if int(x) == 10:
    print ('Inside if condition ', end = '')
    print(a)

    a = 1
    print(a)

print(a)
