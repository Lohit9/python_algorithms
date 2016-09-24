# Implement an algorithmn to check whether a string has all unique characters.
#What if you cannot use any other data structures?

def isUnique(str):
    resList = set(list(str))
    diff_counter = len(str) - len(resList)
    if diff_counter > 0:
        print "Not unique"
    else:
        print "Unique yay"



isUnique("stringi")
