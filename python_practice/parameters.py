#parameters are inside functions 
#arguments are the values that are supplied for a function
#parameters are the holes or placeholders that are defined in a function

def greet_user( first_name, last_name ) :
    print( f'Hi {first_name} {last_name}!' )
    print( "Welcome aboard!" )


print( "Start" )
greet_user( "John", "Smith" )
print( "Finish" )