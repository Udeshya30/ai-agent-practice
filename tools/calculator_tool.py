def calculator(expression):

    try:
        return eval(expression)

    except Exception as e:
        return str(e)