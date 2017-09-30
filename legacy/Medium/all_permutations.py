'''
Given a collection of distinct numbers, return all possible permutations.
Ex:

[1,2,3] => [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
res = []
def permute(head, tail=''):
    global res
    if len(head) == 0: print [list(tail)]
    else:
        for i in range(len(head)):
            permute(head[0:i] + head[i+1:], tail+head[i])

permute(['1','2','3'])
