def test_collatz( n, expected ) :
    result = collatz( n )
    if result == expected :
        print( "passed" )
    else:
        print( "failed for n" )

def collatz( n ) :
    if n == 1 :
        return 1

def main() :
    test_collatz( n, expected )

def n() :
    n == 1

def expected() :
    expected == n

if __name__ == '__main__' :
    main()