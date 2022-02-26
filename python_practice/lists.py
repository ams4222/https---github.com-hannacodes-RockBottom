#lists are written with [] and each item is a string ''
#can index certain things from the list by including the [] with index value in print function

numbers = [ 3, 6, 2, 8, 4, 10 ]
max = numbers[ 0 ]
for number in numbers :
    if number > max :
        max = number
print( max )