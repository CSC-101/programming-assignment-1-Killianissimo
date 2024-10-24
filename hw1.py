import data
import math

# Write your functions for each part in the space below.

# Part 1
'''This function inputs a string and outputs an int. The function counts how many vowels are 
in the input str and outputs how many vowels there were in the input str. 
'''
def vowel_count(input:str) -> int:
    output = 0
    for n in input:
        if n in ["a","e","i","o","u","A","E","I","O","U"]:
            output += 1
    return output

# Part 2
'''This function inputs a list of lists and outputs a new list of lists of length 2. This function
checks the length of lists inside the input list and adds them to the output list if they have a 
length of 2. 
'''
def short_lists(input:list[list[int]]) -> list[list[int]]:
    output = []
    for i in range(len(input)):
        if len(input[i]) == 2:
            output.append(input[i])
    return output


# Part 3
'''This function inputs a list of lists and outputs a new list of lists. This function takes
each element in the input list of length 2 and puts the integers in each element in ascending
order.
'''
def ascending_pairs(input:list[list[int]]) -> list[list[int]]:
    for i in range(len(input)):
        if len(input[i]) == 2:
            if input[i][0] > input[i][1]:
                input[i].append(input[i][0])
                input[i].pop(0)
    return input

# Part 4
'''This function inputs two Prices and outputs one Price. This function takes the two input 
prices and adds them together to create a new price for the two objects.
'''
def add_prices(input1:data.Price, input2:data.Price) -> data.Price:
    newPrice = data.Price(0,0)
    newPrice.dollars = input1.dollars + input2.dollars
    newPrice.cents = input1.cents + input2.cents
    if newPrice.cents > 99:
        newPrice.cents -= 100
        newPrice.dollars += 1
    return newPrice

# Part 5
'''This function inputs a Rectangle and outputs an integer. This function inputs a Rectangle
object and calculates its area. It returns the area of the Rectangle. 
'''
def rectangle_area(input:data.Rectangle) -> int:
    base = input.bottom_right.x - input.top_left.x
    height = input.top_left.y - input.bottom_right.y
    return base * height

# Part 6
'''This function inputs a string and a list of Books. This function takes the input list of Books
and checks if they are written by the author (this is the given string). It adds Books written by 
this author to a new list, which the function returns as its output.
'''
def books_by_author(author:str, books:list[data.Book]) -> list[data.Book]:
    output = []
    for i in range(len(books)):
        if (author in books[i].authors):
            output.append(books[i])
    return output

# Part 7
'''This function inputs a Rectangle and outputs a Circle. This function takes the inputted Circle
and finds the smallest Circle that surrounds the Rectangle, such that all the corners of the 
Rectangle are on the Circle
'''
def circle_bound(input:data.Rectangle) -> data.Circle:
    rect_base = input.bottom_right.x - input.top_left.x
    rect_height = input.top_left.y - input.bottom_right.y
    center_x = input.top_left.x + (rect_base/2)
    center_y = input.bottom_right.y + (rect_height/2)
    radius = math.sqrt((rect_base/2)**2 + (rect_height/2)**2)
    return data.Circle(data.Point(center_x,center_y), radius)

# Part 8
'''This function inputs a list of Employees and outputs a list of Employees. This function takes
the inputted list of Employees and calculates their average pay. It then adds all the Employees
being paid less than average and adds them to a list. Then the function returns this new list. 
'''
def below_average_pay(input:list[data.Employee]) -> list[data.Employee]:
    average_pay = 0
    output = []
    i = 0
    for i in range(len(input)):
        average_pay = input[i].pay_rate + average_pay
        i += 1
    if i == 0:
        return "No list was provided."
    average_pay = average_pay/i
    for j in range(len(input)):
        if (input[j].pay_rate < average_pay):
            output.append(input[j])
    return output


