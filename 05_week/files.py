def hide( file, hidden_word ) :
    for current_word in file :
        if current_word.strip() == hidden_word :
            print("---")
    else:
        print( current_word, end="" )

def hide_using_file_name( file_name, hidden_word ) :
    hide( open( file_name) , hidden_word )

def test_hide() :
    print( "Testing hide_using_file_name and hide text that is not there " )
    hide_using_file_name( "words1.txt" , "word 0" )

    print( "Testing hide_using_file_name and hide text that is there once ")
    hide_using_file_name( "words2.txt" , "word 1" )

    print( "Testing hide_using_file_name and hide text that is there twice ")
    hide_using_file_name( "words3.txt" , "word 2" )


if __name__ == "__main__" :
    test_hide()