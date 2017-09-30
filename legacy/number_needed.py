'''
Thought: condition for anagram --
i) same length
ii) same frequency
'''
def checkFrequencyAndDelete(a,b):
    for each in a:
        if a.count(each) != b.count(each):
'''
get common elements, check  size of set, 
'''

def number_needed(a, b):
    lenA = len(a)
    lenB = len(b)
    deleteCount = 0
    if lenA >= lenB :
        for each in list(a):
            if each not in list(b):
                deleteCount += 1
                a.remove(each)
    else:
        for each in list(b):
            if each not in list(a):
                deleteCount += 1
                b.remove(each)

    print deleteCount
