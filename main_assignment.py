import my_func
from my_func import print_stars

print("Using only import")
for _ in range(5):
    my_func.print_stars()

print("Using from")
for _ in range(5):
    print_stars()

help(my_func)



