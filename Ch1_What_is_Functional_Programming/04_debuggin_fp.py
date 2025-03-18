"""
Debugging FP
===========

It's nearly impossible, even for tenured senior developers, to write perfect code 
the first time. That's why debugging is such an important skill. The trouble is, 
sometimes you have these "elegant" (sarcasm intended) one-liners that are tricky 
to debug:

Example of Hard-to-Debug Code
----------------------------
def get_player_position(position, velocity, friction, gravity):
    return calc_gravity(calc_friction(calc_move(position, velocity), friction), gravity)

Breaking it down into more debuggable code:

def get_player_position(position, velocity, friction, gravity):
    moved = calc_move(position, velocity)
    slowed = calc_friction(moved, friction)
    final = calc_gravity(slowed, gravity)
    print("Given:")
    print(f"position: {position}, velocity: {velocity}, friction: {friction}, gravity: {gravity}")
    print("Results:")
    print(f"moved: {moved}, slowed: {slowed}, final: {final}")
    return final

Assignment
=========
Fix the format_line function. It should apply the following transformations in order:

1. Strip whitespace from the beginning and end of the line.
2. Capitalize every character in the line.
3. Remove any periods from the line.
4. Suffix the line with an ellipsis: words go here...

Run the code. You should see that some subtle bugs are present.

Debugging Instructions
--------------------
Break up the function to make it easier to debug. Use print() statements to see what's 
going on at each step.

Tips
----
Be careful about whitespace! It's easy to miss in console output. I sometimes add a 
character, like a | to the beginning and end of a string to make whitespace more 
obvious when print debugging.

Helpful String Methods:
* .replace(old, new) can be used to replace all instances of a character in a string
* .upper() capitalizes an entire string, .capitalize() capitalizes the first letter
* .strip() removes whitespace from the beginning and end of a string
* .lstrip() and .rstrip() remove whitespace from the left and right respectively
"""

# Create line for print debugging
line = "Hello, world!"

def format_line(line):
    return f"{line.strip().upper().replace('.', '')}..."

print(format_line(line))