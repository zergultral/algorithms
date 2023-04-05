jopa = '-10 - 2'


def simple_operation(example):
    example = example.replace(' ', '')
    for i in range(1, len(example)):
        if example[i] in '+-/*':
            begin1 = i - 1
            end1 = i - 1
            while begin1 > 0 and example[begin1 - 1] in '-0123456789':
                begin1 -= 1
            begin2 = i + 1
            end2 = i + 1
            while end2 < len(example) - 1 and example[end2 + 1] in '-0123456789':
                end2 += 1
            number1 = int(example[begin1:end1 + 1])
            number2 = int(example[begin2:end2 + 1])
            if example[i] == '+':
                result = number1 + number2
            elif example[i] == '-':
                result = number1 - number2
            elif example[i] == '*':
                result = number1 * number2
            elif example[i] == '/':
                result = number1 / number2
    return result


print(simple_operation(jopa))
