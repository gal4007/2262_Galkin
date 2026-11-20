def f(n):
    for i  in range(2, int(n**0.5) + 1):
        if(n%i == 0):
            return False
    return True

a = int(input())

cnt = 0
prime  = 1
while (cnt < a):
    prime+=1
    if f(prime):
        cnt+=1

print(prime)