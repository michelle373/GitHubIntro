# Michelle Patlan
# 8/6/2022
#create a program that prints multiples of 3, 5, or both
for multipleOf in range(51):
    if multipleOf % 3 == 0 and multipleOf % 5 == 0:
        print("Divisible by both")
        continue
    elif multipleOf % 3 == 0:
        print("Divisible by three")
        continue
    elif multipleOf % 5 == 0:
        print("Divisible by five")
        continue
    print(multipleOf)