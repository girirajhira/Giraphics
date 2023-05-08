from giraphics.utilities.latex2 import latex_expression



def typing_text(expr):
    if expr[0] == '$':
        if expr[1] == '$':
            expr = expr[2:-2]
            math_mode = 2
        else:
            expr = expr[1:-1]
            math_mode = 1
    else:
        math_mode = 0
    modes = ['', r'$', r'$$']
    len_expr = len(expr)
    def inner(t):
        if t < len_expr:
            return modes[math_mode] + expr[:t] + '|' + modes[math_mode]
        else:
            return modes[math_mode] + expr[:t] + modes[math_mode]
    return inner



