#argument position order matters, called positional arguments
#ex: first argument is for first parameter second argument is for second parameter
#keyword argument is having the parameter followed by the argument

def greet_user( first_name, last_name ) :
    print( f'Hi {first_name} {last_name}!' )
    print( "Welcome aboard!" )

print( "Start" )
greet_user( last_name = "Smith", first_name = "John" )
print( "Finish" )