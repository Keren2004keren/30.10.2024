# START
# 1
# 103 Students, 30 students in class, how many full classes and how many students in last class?
# 3 full classes and 13 students in the last class
# input the number of students and print how many full classes of 30 there are and how many students in the last class


STUDENTS: int = 30
number_of_students: int = int(input("How many students are there?: "))
print(f"The number of full classes is {number_of_students // STUDENTS}")
print(f"The number of students in the remaining class is {number_of_students % STUDENTS}")

# 2
try:
    asarot: int = None
    ahadot: int = None
    while True:
        legal_num: int = int(input("Enter a number: "))
        if legal_num < 10 or legal_num > 99:
            continue
        if 10 < legal_num < 99:
            asarot: int = legal_num // 10
            ahadot: int = legal_num % 10
            print(f"{legal_num}" if ahadot <= asarot else f"{ahadot * 10 + asarot}")
            break
except ValueError as e:
    print("Error, you must enter a number")

# 3
# Print all prime numbers from 1-200
for num in range(1, 201):
    if num < 2:
        continue
    is_prime: bool = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

# 4
answer_list: list[str] = []
counts: list[int] = [0, 0, 0, 0]
while True:
    answer: str = input("Enter your answer: ")
    if answer == "x":
        break
    if answer != "a" and answer != "b" and answer != "c" and answer != "d":
        continue
    if answer == "a":
        counts[0] += 1
    if answer == "b":
        counts[1] += 1
    if answer == "c":
        counts[2] += 1
    if answer == "d":
        counts[3] += 1
print(f"{counts[0]} students picked a,{counts[1]} students picked b,{counts[2]} students picked c,{counts[3]} students picked d.")
if max(counts) == counts[0]:
    print(f"a was the most popular answer, {counts[0]} students picked it")
elif max(counts) == counts[1]:
    print(f"b was the most popular answer, {counts[1]} students picked it")
elif max(counts) == counts[2]:
    print(f"c was the most popular answer, {counts[2]} students picked it")
else:
    print(f"d was the most popular answer, {counts[3]} students picked it")

if min(counts) == counts[0]:
    print(f"a was the least popular answer, {counts[0]} students picked it")
elif min(counts) == counts[1]:
    print(f"b was the least popular answer, {counts[1]} students picked it")
elif min(counts) == counts[2]:
    print(f"c was the least popular answer, {counts[2]} students picked it")
else:
    print(f"d was the least popular answer, {counts[3]} students picked it")


# STOP
