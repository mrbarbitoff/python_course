def euclid(n, m):
    if max(n, m) % min(n, m) == 0:
        return min(n, m)
    return euclid(min(n, m), max(n, m) % min(n, m))


hcd = euclid(*(int(x) for x in input().split()))
print(hcd)
