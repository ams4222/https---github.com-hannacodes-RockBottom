
#define the variable with boolean
#anything in the indent under the if statement will be executed if True
#if boolean is False, it will execute the else statement
#elif means else if, so if it is neither True nor False, it will execute the elif

is_hot = False
is_cold = True

if is_hot:
    print( "It's a hot day" )
    print( 'Drink plenty of water' )

elif is_cold:
    print( "It's a cold day" )
    print( 'Wear warm clothes' )

else:
    print( "It's a lovely day" )

print( 'Enjoy your day' )