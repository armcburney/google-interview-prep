def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    paren_count = 0
    bracket_count = 0
    brace_count = 0
    stack = []

    for c in s:
        if paren_count < 0 or bracket_count < 0 or brace_count < 0:
            return False

        if c is "(":
            paren_count += 1
            stack.append(c)
        elif c is ")":
            paren_count -= 1
            if len(stack) is not 0 and "(" is not stack.pop():
                return False
        elif c is "[":
            bracket_count += 1
            stack.append(c)
        elif c is "]":
            bracket_count -= 1
            if len(stack) is not 0 and "[" is not stack.pop():
                return False
        elif c is "{":
            brace_count += 1
            stack.append(c)
        elif c is "}":
            brace_count -= 1
            if len(stack) is not 0 and "{" is not stack.pop():
                return False

    if paren_count is not 0 or bracket_count is not 0 or brace_count is not 0:
        return False
    else:
        return True
