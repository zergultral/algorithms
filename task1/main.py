dirs = [0, 1, 2, 3]
file = open('text.txt', 'w')

maxsize = int(input())
for size in range(maxsize + 1):
    steps = []

    for n in range(1000):
        field = [[0 for j in range(size)] for i in range(size)]
        x = y = 0
        step = 1
        counter = size * size
        import random
        import statistics
        #while field != [[1 for j in range(size)] for i in range(size)]:
        while counter > 0:
            if field[x][y] == 0:
                counter -= 1
            field[x][y] = 1
            dir = random.choice(dirs)
            if dir == 0 and x < size - 1:
                x += 1
                step += 1
            elif dir == 1 and y < size - 1:
                y += 1
                step += 1
            elif dir == 2 and x > 0:
                x -= 1
                step += 1
            elif dir == 3 and y > 0:
                y -= 1
                step += 1
        steps.append(step)

    print(statistics.mean(steps))
    file.write(str(size) + '\t' + str(statistics.mean(steps)) + '\n')

file.close()