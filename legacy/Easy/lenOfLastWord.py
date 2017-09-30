def lengthOfLastWord(A):
    A = list(A.strip(' '))
    A.reverse()
    if(A == ''): return 0
    count = 0

    for index,char in enumerate(list(A)):
        if(char == ' '):
            return count
        count+=1
    return 0

print lengthOfLastWord("Hello World")
print lengthOfLastWord("Hello World    ")
