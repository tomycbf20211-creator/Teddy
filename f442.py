n = int(input())
chik = list(map(int, input().split()))

findd = {}
for i in range(len(chik)):
    findd[chik[i]] = i

eagle = int(input())
q = int(input())
caught = list(map(int, input().split()))

for w in caught:
    i = findd[w]   # 被抓到的小雞目前的位置

    # swap
    temp = chik[i]
    chik[i] = eagle
    eagle = temp

    # 更新位置資訊
    del findd[w]
    findd[chik[i]] = i

print(*chik)
