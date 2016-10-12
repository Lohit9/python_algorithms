#general solution
def fibS(n):
  if n <= 1: return 1
  ans = fibS(n-1)+fibS(n-2)
  return ans

#dynamic programming solution
MEM = [0]*1000
def fib(n):
  global MEM
  if n <= 1: return 1
  elif n in MEM: return MEM[n]
  else:
    res = fib(n-1)+fib(n-2)
    MEM[n] = res
    return res

print fibS(5)#8
print fib(5)#8
