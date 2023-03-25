import time
import sys
print(sys.argv)

f = open('C:\\Users\\user\\Desktop\\names2.txt')
command = sys.argv[1]

start = time.time()

if True:
    """
    n = ''
#    x = [command[i] for i in range(4, len(command))]
#    for i in command:
#        n += i
    n = int(command)

    line = f.readlines()[n-1]
    name = line.split('\t')[1]

    print(name)"""

    age, numbers, names = int(command), [], []
    while True:
        line = f.readline()
        if not line:
            break
        if not line.strip():
            break
        notint= line.split('\t')[2]
        if int(notint) == age:
            numbers.append(line.split('\t')[0])
            names.append(line.split('\t')[1])

    print(len(numbers))

end = time.time()

print(start)
print(end)
print(end - start)