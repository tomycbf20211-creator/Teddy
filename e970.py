n = int(input())#n則留言數
seq = list(map(int,input().split()))
indi = seq[len(seq)-1]#基數
yepp = 0


for i,v in enumerate(seq,start = 1):
    if i % indi == 1:
        yepp += v
res = yepp % n


if res == 0:
    print(n,end = " ")
    print(indi)
else:
    print(res,end = " ")
    print(seq[res-1])
