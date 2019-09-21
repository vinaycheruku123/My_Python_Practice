def collatz(number):

    try:

        while number != 1:
            
            if number % 2 == 0:
                number = number // 2
                
            elif number % 2 == 1:
                number = 3 * number + 1
                
            print(number)
            
        return number
    except ZeroDivisionError:
        print('Invalid Number')

collatz(1004)
