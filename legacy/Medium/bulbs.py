def flipBits(nums):
       res = [0]*1000
       i=0
       for each in nums:
          if each == 0:
              res[i] =  1
          else:
              res[i] =  0
          i+=1
       return res[:len(nums)]

def bulbs(A):
        i = 0
        count = 0
        while(0 in A and i<len(A)):
            if(A[i] == 0 and i<len(A)):
                count += 1
                A = A[:i+1]+flipBits(A[i+1:])
            i += 1
        return count

print bulbs([0,1,0,1])# 4
print bulbs([ 1, 1, 0, 0, 1, 1, 0, 0, 1])# 4
