#to get out of a while loop break will terminate it

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit :
    guess = int( input( "Guess: " ) )
    guess_count += 1
    if guess == secret_number :
        print( "You've guessed it!" )
        break
else:
    print( "You lost" )