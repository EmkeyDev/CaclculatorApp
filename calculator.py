def calculate(expression):
    try:
        allowed = "0123456789+-*/(). "
        for char in expression:
            if char not in allowed:
                return "Error: invalid symbol"
        return eval(expression)
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except:
        return "Error"