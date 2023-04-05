example = '1+2'
example = example.replace(' ', '')

for i in range(len(example)):
    if example[i] == '+':
        begin1 = i - 1
        end1 = i - 1
        while begin1 > 0 and example[begin1 - 1] in '0123456789':
            begin1 -= 1
        begin2 = i + 1
        end2 = i + 1
        while end2 < len(example) - 1 and example[end2 + 1] in '0123456789':
            end2 += 1
        print(begin1, end1, begin2, end2)
        number1 = int(example[begin1:end1+1])
        number2 = int(example[begin2:end2+1])
        print(number1, number2)
        result = number1 + number2


print(result)
