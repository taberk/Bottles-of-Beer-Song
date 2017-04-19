
for item in range(99,-1, -1):
    if item > 2:
        print "%i bottles of beer on the wall, %i bottles of beer. Take one down, pass it around, %i bottles of beer on the wall.\n" % (item, item, item-1)
    elif item == 2:
        print "%i bottles of beer on the wall, %i bottles of beer. Take one down, pass it around, %i bottle of beer on the wall.\n" % (item, item, item-1)
    elif item == 1:
        print "%i bottle of beer on the wall, %i bottle of beer. Take one down, pass it around, no more bottles of beer on the wall.\n" % (item, item)
    else:
        print "No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall."
