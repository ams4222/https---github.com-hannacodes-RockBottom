#int stands for integer which is a whole number
#str stands for string
#int() converts string into an integer
#float() converts string into a float or a number with a decimal
#bool() converts string into a boolean value

birth_year = input( ' Birth year: ' )
print( type( birth_year ))
age = 2022 - int( birth_year )
print( type( age ))
print( age )
