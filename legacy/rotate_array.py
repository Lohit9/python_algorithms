def array_left_rotation(a, n, k):
   a = a[k:] + a[:k]
   return a

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
