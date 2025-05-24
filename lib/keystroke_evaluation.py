evaluate_keystrokes('abcde<fg<h')

evaluate_keystrokes('abcd<<<fg<h')

evaluate_keystrokes('fg<h')

# A solution that doesn't use a stack might look like this

def evaluate_keystrokes(string):
    i = len(string) - 1
    result = ""
    skip = 0

    while i >= 0:
        if string[i] == "<":
            skip += 1
            i -= 1
        else:
            if skip > 0:
                i -= skip
                skip = 0
            else:
                result = string[i] + result
                i -= 1

# How to solve the problem using the stack method
def evaluate_keystrokes(string):
    stack = []
    for char in string:
        if char == "<":
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(char)

    result = ""
    while stack:
        result = stack.pop() + result

    return result