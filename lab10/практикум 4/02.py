n = int(input())
dress = list(map(int, input().split()))

s = [False, False, False]
ans = n

for i in range(n):
    dress_num = dress[i]
    s[dress_num - 1] = True  
    
    if s[0] and s[1] and s[2]:
        ans = i + 1
        break

print(ans)
