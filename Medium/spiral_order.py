# # [
# #  [ 1, 2, 3 ],
# #  [ 4, 5, 6 ],       ==> [1, 2, 3, 6, 9, 8, 7, 4, 5]
# #  [ 7, 8, 9 ]
# # ]

# [[1,2,3],[4,5,6],[7,8,9]]
class Solution(object):
    def flatten(self,nums):
        res = []
        for each in nums:
            if (isinstance(each,list)):
                for n in each:
                    res.append(n)
            else: res.append(each)
        return res

    def spiralOrder(self,matrix):
        res = []
        while(matrix != [[]]):
            res.append(matrix.pop(0))
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix != [[]]:
                res.append(matrix[-1].pop())
            if matrix != [[]]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res


print spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
