import json
from giraphics.utilities.latex2 import latex_expression
from giraphics.utilities.latex_svg_decoder import *
import numpy as np

###### All tick marker expressions
#
markers = []

decimal_markers1 = np.arange(-10, 10+1, 1)
for m in decimal_markers1:
    markers.append(f'{m}')

decimal_markers1 = np.arange(-10, 10+.1, .1)
for m in decimal_markers1:
    markers.append(f'{round(m,2)}')

decimal_markers1 = np.arange(-10, 10+1, 2)
for m in decimal_markers1:
    markers.append(f'{m}')

decimal_markers1 = np.arange(-10, 10+.2, .2)
for m in decimal_markers1:
    markers.append(f'{round(m,2)}')

decimal_markers1 = np.arange(-10, 10+.25, .25)
for m in decimal_markers1:
    markers.append(f'{round(m,3)}')

power10 = np.arange(-20, 21, 1)
decimal_markers1 = np.arange(-10, 10+1, 1)
for m in decimal_markers1:
    for p in power10:
        r = '{'+str(p)+'}'
        markers.append(f'${m}\times 10^{r}$')


power10 = np.arange(-20, 21, 1)
decimal_markers1 = np.arange(-10, 10+.1, .1)
for m in decimal_markers1:
    for p in power10:
        r = '{'+str(p)+'}'
        markers.append(f'${round(m,2)}\times 10^{r}$')

power10 = np.arange(-20, 21, 1)
decimal_markers1 = np.arange(-10, 10+.1, .2)
for m in decimal_markers1:
    for p in power10:
        r = '{'+str(p)+'}'
        markers.append(f'${round(m,2)}\times 10^{r}$')


marker_dict  = {}

for i, m in enumerate(markers):

    # creat latex code
    # save it in a dict with cc-i


    pass

# write the dict as json to tex_cache



#
# with open('file.txt', 'w') as file:
#      file.write(json.dumps(exDict)) # use `json.loads` to do the reverse
#
#
#
#
#
#
#
#
#
# expr_code, w_expr, h_expr = latex_expression(expr, colour=colour, preamble=preamble,
#                                              usepackages=usepackages,
#                                              cleanup=cleanup)
# # Data processing
# index = len(self.latex_history)
# symbols = get_svg_symbol_ids(expr_code)
# clips = get_svg_clip_ids(expr_code)
# for symb in symbols:
#     expr_code = expr_code.replace(symb, symb + f'-cc{index}')
# for clip in clips:
#     expr_code = expr_code.replace(clip, clip + f'-{index}')
#
# self.latex_history[expr] = [expr_code, w_expr, h_expr, colour]
#
# expr_code = expr_code.replace('fill-opacity:1', f'fill-opacity:{round(opacity, 3)}')