"""
=============
Immutability
=============

In FP, we strive to make data immutable. Once a value is created, it cannot be 
changed. Mutable data, on the other hand, can be changed after it's created.

-------------
Who Cares?
-------------

Immutable data is easier to think about and work with. When 10 different functions 
have access to the same variable, and you're debugging a problem with that 
variable, you have to consider the possibility that any of those functions could 
have changed the value.

When a variable is immutable, you can be sure that it hasn't changed since it was 
created. It's a helluva lot easier to work with.

Generally speaking, immutability means fewer bugs and more maintainable code.

------------------
Tuples vs. Lists
------------------

Tuples and lists are both ordered collections of values, but tuples are immutable 
and lists are mutable.

You can append to a list, but you can not append to a tuple. You can create a new 
copy of a tuple using values from an existing tuple, but you can't change the 
existing tuple.

-----------------
Lists Are Mutable
-----------------

ages = [16, 21, 30]
# 'ages' is being changed in place
ages.append(80)
# [16, 21, 30, 80]

-------------------
Tuples Are Immutable
-------------------

ages = (16, 21, 30)
more_ages = (80,) # note the comma! It's required for a single-element tuple
# 'all_ages' is a brand new tuple
all_ages = ages + more_ages
# (16, 21, 30, 80)

-----------
Assignment
-----------

The add_prefix function accepts 2 arguments:

    "document": a string
    "documents": the current tuple of strings

It should do 2 things:

    Add a prefix of X. to the beginning of the new document, where X is the next 
    index in the tuple. (The first document should be 0. , next should be 1. , 
    etc.)
    Return the documents tuple with the new document added to the end.

    Run the code to see the error. Whoever wrote this code assumed that documents 
    is a list, but it's a tuple!

    Fix the bug. Instead of attempting to mutate the input tuple, create a brand 
    new tuple with the new document added to the end and return that.
"""

def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    return documents + (new_doc,)