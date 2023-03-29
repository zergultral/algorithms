# Work in progress...
# https://youtu.be/f5slLeCz7p8


n = 997 * 3571  # int(input())
print(n)

basis = 8
r = 1
while (basis ** r) % n != 1:
    r += 1
    # print(r, basis ** r, basis ** r // n, basis ** r % n)

pred_euklid_multiplier = int(basis ** (r // 2) - 1)
numerator = pred_euklid_multiplier
denominator = n

print('pred_euklid_multiplier: ', pred_euklid_multiplier)
while True:
    reminder = int(numerator % denominator)
    print(int(numerator), int(denominator), int(reminder))
    if reminder == 0:
        break
    numerator = denominator
    denominator = reminder

multiplier1 = denominator
multiplier2 = n // multiplier1

print(pred_euklid_multiplier % 13)
print(pred_euklid_multiplier % 23)
print(r)
print(multiplier1)
print(multiplier2)
