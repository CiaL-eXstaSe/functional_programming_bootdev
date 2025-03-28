"""
===========
It's Math
===========

Functional programming tends to be popular amongst developers with a strong 
mathematical background. After all, a math equation isn't procedural: it's 
declarative. Take the following math equation:

avg = Σx/N

------------------------
Mathematical Explanation
------------------------
Σ is just the Greek letter Sigma, and it represents "the sum of a collection".
x is the collection of numbers we're averaging.
N is the number of elements in the collection.
avg is equal to the sum of all the numbers in collection "x" divided by the 
number of elements in collection "x".

So, the equation really just says that avg is the average of all the numbers in 
collection "x". This math equation is a declarative way of writing "calculate 
the average of a list of numbers".

--------------
Code Examples
--------------
Here's some imperative Python code that does the same thing:

def get_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

However, with functional programming, we would write code that's a bit more 
declarative:

def get_average(nums):
    return sum(nums) / len(nums)

Here we're not keeping track of state (the total variable in the first example 
is "stateful"). We're simply composing functions together to get the result we 
want.

===========
Assignment
===========
In the world of document conversion, we sometimes need to handle fonts and font 
sizes.

Complete the get_median_font_size function. Given a list of numbers representing 
font sizes, return the median of the list.

---------
Examples
---------
[1, 2, 3] => 2
[10, 8, 7, 5] => 7

Notice the second list is out of order. Order the list, then find the middle 
index, and return the middle number. If there is an even amount of numbers, 
return the smaller of the two middle numbers (I know it's not a true median, 
but good for our purposes). If the list is empty, just return None.

------------------
Helpful Functions
------------------
* sorted
* len
* // (floor division)

-------------
Requirements
-------------
To be a good little functional programmer, your code for this lesson should not:
* Use loops
* Mutate any variables (it's okay to create new ones)
"""

def get_median_font_size(font_sizes):
    if not font_sizes:
        return None
    sorted_font_sizes = sorted(font_sizes)
    middle_index = len(sorted_font_sizes) // 2
    if len(sorted_font_sizes) % 2 == 0:
        return sorted_font_sizes[middle_index - 1]
    else:
        return sorted_font_sizes[middle_index]
    
# Author's solution
def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2] # Method Chaining is used here


