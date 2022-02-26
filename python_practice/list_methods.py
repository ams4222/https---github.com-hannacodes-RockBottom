#there are different methods for lists that can be used with the dot operator function

numbers = [ 2, 2, 4, 6, 3, 6, 4 ]
uniques = []
for number in numbers :
    if number not in uniques :
        uniques.append( number )
print( uniques )