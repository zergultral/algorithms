# Work in progress...
# https://youtu.be/f5slLeCz7p8


n = 23 * 13 # int(input())

basis = 6
r = 1
while (basis ** r) % n != 1:
    r += 1
    print(r)

pred_euklid_multiplier = int(basis ** (r / 2) + 1)
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

print(denominator)
print((pred_euklid_multiplier - 1) % 13)
print((pred_euklid_multiplier - 1) % 23)
