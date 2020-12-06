#collections.Counter()


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
N = Counter(map(int,input().split()))
xi = int(input())
total = []
for i in range(xi):
    size,cost = map(int,input().split())
    if N[size] > 0:
        total.append(cost)
        N.subtract(Counter([size]))
print (sum(total))