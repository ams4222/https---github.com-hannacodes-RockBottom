#dictionaries can store key value pairs
#each key should be unique
#can access dictionary values with []
#can use .get() in order to get none for values that don't exist
#cn also add a a default value

customer = {
    "name" : "John Smith",
    "age" : "30",
    "is_verified" : True
}

print( customer[ "name" ] )

phone = input( "Phone: " )
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ""
for ch in phone :
    output += digits_mapping.get( ch, "!" ) + " "
print( output )