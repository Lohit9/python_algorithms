def isBipartite(matrix):
		A = []
		B = []
		i = 0
		for row in matrix:
			i += 1
			if (i not in A and i not in B):
				partition(i, matrix, A, B)
		return True

def partition(i, matrix, A, B):
		for j, each in enumerate(row):
			if( each == 1) :
				if i in B or j in A:
					False
				A.append(i)
				B.append(j)
				partition(j, matrix, B, A)

M = [
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0]
]

# M = [
#     [0,1],
#     [1,0]
# ]

print isBipartite(M)
