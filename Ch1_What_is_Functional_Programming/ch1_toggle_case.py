"""
Toggle Case
===========

We need to add a feature to Doc2Doc that switches the capitalization of all 
the words in a line.

Assignment
----------
Complete the toggle_case function using string methods. It takes a string as input 
line, and returns a string.

* If line is in titlecase, convert it to all uppercase and add three "!" to 
  the end.
* If line is all uppercase, convert it to all lowercase except for the first 
  letter and remove all trailing "!".
* If line is all lowercase or only the first letter is capitalized, convert it 
  to title case.
* Otherwise, just return line unchanged.

Tips
----
You will have to use the link to the official Python documentation to find the 
right string methods. Reading documentation is a skill all developers need to 
master.
"""

def toggle_case(line):
    if line.istitle():
        return line.upper() + "!!!"
    if line.isupper():
        return line.lower().capitalize().rstrip('!')
    if len(line) > 0 and line[1:].islower():
        return line.title()
    return line
