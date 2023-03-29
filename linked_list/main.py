import sys
import random

def makenode(n):
    node = makenode(n // 10) if n >= 10 else None
    return {'value': n % 10, 'next': node}

def summ(n, m, o=0):
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


def process_input():
    n = random.randint(0, 1000)
    print('Input 1st number.\nChose', n, '?')
    num = input()
    number1 = n if num == '' else int(num)

    n = random.randint(0, 1000)
    print('Input 2nd number.\nChose', n, '?')
    num = input()

    number2 = n if num == '' else int(num)
    node1 = makenode(number1)
    node2 = makenode(number2)
    result = makenumber(summ(node1, node2))
    print(number1, number2)
    print(result)

def process_test():
    test = [
        [0, 0, 0],
        [999, 1, 1000],
        [1000, 0, 1000],
        [9, 9, 18],
        [99, 99, 198]
    ]

    for testCase in test:
        result = makenumber(summ(makenode(testCase[0]), makenode(testCase[1])))
        if result != testCase[2]:
            return print("error ", testCase, result)
    print("no errors")

print(sys.argv)
if sys.argv[1] == 'test':
    process_test()
else:
    process_input()

