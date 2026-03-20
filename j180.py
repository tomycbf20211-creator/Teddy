while True:
    s = input().strip()

    if s == "-1":
        break

    N, E = map(int, s.split())

    # 沒有倉庫，或容量為 0，代表一開始就沒有糧食
    if N == 0 or E == 0:
        print(0)
        continue

    food = N * E
    days = 0

    while food > 0:
        guards = (food + E - 1) // E   # ceil(food / E)
        food -= guards
        days += 1

    print(days)
