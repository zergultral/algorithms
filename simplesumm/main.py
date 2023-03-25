a1 = str(int(input()))
a2 = str(int(input()))
s = ''

def makearray(x1, x2):
    y1 = [x1[i] for i in range(-1, -1 * len(x1) - 1, -1)]
    y2 = [x2[i] for i in range(-1, -1 * len(x2) - 1, -1)]
    for i in range(len(x1) - len(x2)):
        y2.append(0)
    return y1, y2

if len(a1) > len(a2):
    b1, b2 = makearray(a1, a2)
else:
    b2, b1 = makearray(a2, a1)

s0 = [0 for i in a1]
s0.append(0)

for i in range(len(s0)):
    s0[i] += int(b1[i]) + int(b2[i])
    if s0[i] >= 10:
        s0[i+1] = 1
        s0[i] -= 10

for i in range(-1, -1 * len(s0) - 1, -1):
    s += str(s0[i])

print(s)

print(int(a1) + int(a2))