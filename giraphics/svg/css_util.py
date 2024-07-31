
def css_style(stylename, style_dict):
    txt = '<style>\n'
    txt += f'.{stylename}' + '{\n'
    for key, value in style_dict.items():
        txt += f'{key}: {value};\n'
    txt += '}\n</style>\n'

    return txt

#
# test_dict = {'font-size':10, 'color': 'red'}
#
# print(css_style('mystyle', test_dict))
