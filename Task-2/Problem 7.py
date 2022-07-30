from __future__ import division

def average(array):
    # your code goes here
    distint_height = set(array)
    aver = sum(distint_height)/len(distint_height)
    return aver
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
if __name__ == '__main__':
