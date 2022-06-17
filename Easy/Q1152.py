list = list(map(int, input().split()))
r = 0
for i in list:
    r += i**2
print(r%10)