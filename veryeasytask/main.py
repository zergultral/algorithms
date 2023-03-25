N = int(input()) - 1
x = int(input())
y = int(input())
t = 0

while N > 0:
    t += 1
    if t % x == 0:
        N -= 1
    if t % y == 0:
        N -= 1

if x > y:
    t += y
else:
    t += x

print(t)