#use f and {} in order to format strings
#{} act as empty holes that will be filled in with the input

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder '
msg = f'{first} [ {last} ] is a coder '
print( msg )