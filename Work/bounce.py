# bounce.py
#
# Exercise 1.5
height = 100
bounces = range(1, 11)
for bounce in bounces:
    height *= 3/5
    print(bounce, round(height, 4))

