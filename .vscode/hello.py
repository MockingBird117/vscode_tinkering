
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

#see if not an operand
else:
    print('Sorry, this is not an opperand.')


#print solution
if(op == '+', '-', '*', '/'):
    print(solution)

