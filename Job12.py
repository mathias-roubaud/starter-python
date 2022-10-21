file = open("data.txt", "r").readlines()
myresults = []
for i in range( 19 ):
    myresults.append( 0 )

myspeciallist = [ '-', '+', '!', '"', '(', ')', '?', ',', '.', ';', "'"]

for line in file:
    words = str.split( line )
    for word in words:
        if word not in myspeciallist:
            if word[ -1 ] not in myspeciallist :
                myresults[ len( word ) ] += 1
            else :
                myresults[ len(word ) -1 ] += 1
print( myresults )