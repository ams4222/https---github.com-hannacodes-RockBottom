#making a parent class/function that gets inherited into other functions by calling it

class Mammal :
    def walk( self ) :
        print( "walk" )

class Dog( Mammal ) :
    def bark( self ) :
        print( "bark" )
    

class Cat( Mammal ) :
    def meow( self ) :
        print( "meow" )


dog1 = Dog()
dog1.walk()