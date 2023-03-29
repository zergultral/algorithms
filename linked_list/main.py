import random

n = random.randint(0, 1000)
print('Input 1st number.\nChose', n, '?')
num = input()
number1 = n if num == '' else int(num)

n = random.randint(0, 1000)
print('Input 2nd number.\nChose', n, '?')
num = input()

number2 = n if num == '' else int(num)


def makenode(n):
    node = makenode(n // 10) if n > 10 else None
    return {'value': n % 10, 'next': node}

def summ(n, m, o):
    value = ((n['value'] + m['value'] + o) % 10)
    o = 1 if (n['value'] + m['value'] + o) >= 10 else 0
    if n['next'] is not None and m['next'] is not None:
        node = summ(n['next'], m['next'], o)
    elif n['next'] is None and m['next'] is not None:
        node = summ({'value': 0, 'next': None}, m['next'], o)
    elif n['next'] is not None and m['next'] is None:
        node = summ(n['next'], {'value': 0, 'next': None}, o)
    elif o == 1:
        node = summ({'value': 0, 'next': None}, {'value': 0, 'next': None}, o)
    else:
        node = None
    return {'value': value, 'next': node}

def makenumber(n):
    nextnumber = 10 * makenumber(n['next']) if n['next'] is not None else 0
    return n['value'] + nextnumber

node1 = makenode(number1)
node2 = makenode(number2)

result = makenumber(summ(node1, node2, 0))

print(number1, number2)
print(result)
