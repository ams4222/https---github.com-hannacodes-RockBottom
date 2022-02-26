#returns error as 0 = no errors, program ran successfully
#returns any number other than 0, program crashed
#exceptions return an error message and doesnt crash the program

try :
    age = int( input( 'Age: ' ) )
    print( age )
except ValueError :
    print( 'Invalid value' )
