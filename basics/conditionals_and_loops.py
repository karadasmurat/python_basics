# Python, unlike those other languages, uses two things to denote blocks:
#   a colon (:)
#   indentation

import os

os.system("python --version")

def main():
    
    # Generate a sequence of numbers
    # Syntax range([start,] stop [, step]) -> range object
    x = range(5)    # [0, 1, 2, 3, 4] - len=5
    print(type(x), x, list(x))  # <class 'range'> range(0, 5) [0, 1, 2, 3, 4]

    # infinite_menu()
    # for_loop_v1()
    # askAndCheck()
    # print(square(5))
    # askAndCheckRange()

    minx = min_of_three(110, 90, 99)
    print("\nmin:", minx)

    score= 65
    res= exam_result(score)
    print(score, ":", res)

    # match_code("408")
    # iterate_list()

    print(sum_all_positive_numbers([1, 9, -5, 10, -1, 5]))  # 25
    print(sum_all_positive_numbers(range(-4, 5)))           # 10

def infinite_menu():

    n = 0
    while True:
        n = int(input("Select an option [1-9]: "))
        #check for negatives to give a message.
        if n < 1 or n > 9:
            print("Not a valid option.")
        #break on the positive
        else:
            break
    
    for i in range(n):
        print("*", end='')


# def keyword introduces a function definition.
def askAndCheck():
    resp = int(input("\n\nEnter a number: "))
    if resp < 0:
        print("why so negative?")
    elif resp == 0:
        print("zero? really?")
    else:
        print("positive vibes")


def square(x):
    return x**2


# one-liner for boolean return type
def isEven(x):
    # return conditional itself
    return x % 2 == 0

# return a conditional "expression"
def exam_result(score):
    return "Pass" if score >= 70 else "Fail"
    
def askAndCheckRange():
    x = int(input("Enter Test Score: "))
    if 90 <= x <= 100:          # RANGE COMPARISON, instead of if score >= 90 and score <= 100:
        print("Congrats. A")
    else:
        print("Sorry, not an A")

def match_code(http_code):
    match http_code:
        case "200":
            print("OK")
        case "404":
            print("Not Found")
        case "500":
            print("Internal Server Error")
        # underscore symbol: default case
        case _:
            print(http_code, "Desc not found")

    
def for_loop_v1():
    for i in [1,2,3]:
        print("loop through a list", i)

    for i in range(3): # [0, 1, 2]
        print("loop in range", i)

    fruits = ["banana", "apple", "strawberry", "melon"]
    for fruit in fruits :
        print("loop through a list", fruit)

    # non-pythonic to manually index
    for i in range(len(fruits)):
        print(f"loop using index, {fruits[i]=}")

    # Iterate over characters of a string
    name = "Bingo"
    for letter in name:
        print(letter)

def iterate_list():
    students = ["Harry", "Hermione", "Ron"]

    for s in students:
       print(s)

    for i in range(len(students)):
        print(i+1, students[i])
    
def sum_all_positive_numbers(arg):
    '''summing all positive numbers in the sequence'''
    sum = 0
    for n in arg:
        if n < 0:
            continue        # Skipping over items in a loop
        sum += n

    return sum

def min_of_three(x, y, z):
    min=x
    if y < min:
        min=y

    if z< min:
        min=z

    return min



############
main()
