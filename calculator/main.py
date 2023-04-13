# jopa = str(input())
#
# jopa2 = ''
# for i in range(len(jopa)):
#     if i == 0 and jopa[i] == '-' or jopa[i] == '-' and jopa[i - 1] in '+-*/':
#         jopa2 += '_'
#     elif jopa[i] != ' ':
#         jopa2 += jopa[i]

def simple_operation(example):
    for i in range(1, len(example)):
        if example[i] in '+-*/':
            operator = example[i]
            break
    operand1 = float(example[:i].replace('_', '-'))
    operand2 = float(example[i + 1:].replace('_', '-'))
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    return result


# if example[i] in '+-/*':
#     begin1 = i - 1
#     end1 = i - 1
#     while begin1 > 0 and example[begin1 - 1] in '_.0123456789':
#         begin1 -= 1
#     begin2 = i + 1
#     end2 = i + 1
#     while end2 < len(example) - 1 and example[end2 + 1] in '_.0123456789':
#         end2 += 1
#     number1 = int(example[begin1: end1 + 1])
#     number2 = int(example[begin2: end2 + 1])
#     if example[i] == '+':
#         result = number1 + number2
#     elif example[i] == '-':
#         result = number1 - number2
#     elif example[i] == '*':
#         result = number1 * number2
#     elif example[i] == '/':
#         result = number1 / number2
#     return result


def main(example):
    example = example.replace(' ', '')
    if not ('+' in example or '-' in example or '*' in example or '/' in example):
        return example
    for i in range(1, len(example)):
        if example[i] in '+-/*':
            end = i + 1
            while end < len(example) - 1 and example[end + 1] in '_.0123456789':
                end += 1
            break
    return float(main(str(simple_operation(example[:end + 1])) + example[end + 1:]))

# if end < len(example) - 1:
#     return main(str(simple_operation(operation)) + example[end + 1:])
# else:
#     return simple_operation(operation)


test = [
    ['1+1', 2],
    ['2*2*3', 12],
    ['2*2+2', 6],
    ['1000/100', 10],
    ['0.1/0.5', 0.2],
    ['10/5+1*4/12', 1]
]

error = False
for i in test:
    if main(i[0]) != i[1]:
        print('error:', i[0], '!=', main(i[0]), '; =', i[1])
        error = True
if not error:
    print('no errors found')

# print(main(jopa2))
