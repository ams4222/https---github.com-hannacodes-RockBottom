#the and/or operator will run two conditions at the same time
#and: both or: at least one

has_criminal_record = False
has_good_credit = True

if has_good_credit and not has_criminal_record:
    print( 'Eligible for loan' )