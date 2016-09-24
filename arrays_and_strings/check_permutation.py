'''
Given 2 strings check if a one is a permutation of the other

'''
# Using set , time complexity - O(n)
def is_permutaion(s1,s2):
    if len(s1) is len(s2):
        set1 = set(list(s1))
        set2 = set(list(s2))
        if set1 == set2 :
            print("Is a permuation")
            return
        else:
            print "not a permuation"

    else:
        print("Not a permuation as different lengths")





is_permutaion("abcd","cbad")
is_permutaion("aasde", "saaed")
