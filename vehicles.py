vehicle = 'motorbike'
print(vehicle[:5])

vehicle = 'airplane'
vehicle[:3] = 'water'  # This will cause an error because strings are immutable
print(vehicle)
