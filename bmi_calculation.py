def bmi(weight, height):
    index = weight / (height * height)
    return index

p6 = bmi(79, 1.73)
print(p6 < 18.5)
