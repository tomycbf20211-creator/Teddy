n = int(input())
height = list(map(int, input().split()))
weight = list(map(int, input().split()))
minn = height[0] * weight[0]
indi = 0
for i in range(1,n):
    cur = height[i] * weight[i]
    if cur < minn:
        minn = cur
        indi = i
print(height[indi],end = " ")
print(weight[indi])
