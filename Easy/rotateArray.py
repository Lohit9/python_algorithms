def rotateArray(a, b):
        if len(a)>b:
            result = a[b:]+ a[:b]
        elif len(a) == b:
            result = a
        else:
            rem = b - len(a)
            return rotateArray(a,rem)
        return result

print rotateArray([1,2,3,4,5,6],10)
