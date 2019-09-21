def Comma_Code(spam):
    print('Practising displaying list with and condition')
    final = ''
    
    for i in range(len(spam)):
        if i == len(spam)-2:
            final += spam[i]+', and '
        elif i == len(spam)-1:
            final += spam[i]
        else:
            final += spam[i]+', '
    print(final)

Comma_Code(['apples', 'bananas', 'tofu', 'cats', 'tvs', 'bags', 'fans', 'chairs'])
