'''
Write a program to replace all spaces in a given string with '%20'. You are also given the true length of the string
ignoring the space at the end of the string

Ex:
Input:"Mr John Smith    ", 13
Output:"Mr%20John%20Smith"
'''

def urlify(s,len):
    l = list(s)
    for each in range(len):
        if(l[each] == " "):
            l[each] = "%20"

    print "".join(l)
    return

urlify("Mr John Smith    ", 13)
