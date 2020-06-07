try:
    #get input

    one = int(input('1st: '))
    two = int(input('2nd: '))

    #choose opperant

    op = input('Chose an opperand: ')

    #check for opperand

    if(op == '+' ):
        solution = (one + two)

    if(op == '-'):
        solution = (one - two)

    if(op == '*'):
        solution = (one * two)

    if (op == '/'):
        solution = (one / two)

    #see if not an operand / print solution

    if not op in ['+', '-', '*', '/']:
        print('Sorry, this is not an opperand.')
    else:
        print("The solution is: " + str(solution))

except:
    print('Pls insert integer.')

