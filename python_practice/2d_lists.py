#2D lists are lists inside of a list
#using two square brackets in the matrix will access individual strings in the inner lists
#can alsl use nested loops for the iterations

matrix = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
for row in matrix :
    for item in row :
        print( item )