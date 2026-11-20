from string import ascii_lowercase

s = input().strip()

max_count = 0
a = ''

for i in ascii_lowercase:
    cnt = s.count(i)
    if cnt > max_count:
        max_count = cnt
        a = i

print(s.replace(a, ''))
