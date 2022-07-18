import os
import shutil
import re
import numpy as np

default_latex_template = r"""

\documentclass{standalone}
\usepackage[utf8]{inputenc}
\usepackage{physics}
\usepackage{amssymb}
\usepackage{amsmath}


"""


def generate_pdf_from_tex(expression, outfile, tempfolder = False, usepackages=None, preamble=None, colour = None):
    with open(outfile, 'w') as file:
        file.write(default_latex_template)
        if usepackages != None:
            for pack in usepackages:
                file.write(r"\usepackage{" + pack +"}")
        if preamble!=None:
            file.write(preamble + " \n")
        if colour != None:
            if isinstance(colour, list) or isinstance(colour, (np.ndarray, np.generic)):
                file.write(r"\usepackage{xcolor}")
                file.write(r"\definecolor{custcolour}{RGB}{" + f'{colour[0]}, {colour[1]}, {colour[2]}' + r"}" )
                expression = (r"\textcolor{custcolour}{" + expression + r"}")
            else:
                file.write(r"\usepackage{xcolor}")
                expression = (r"\textcolor{" + colour + "}{" + expression + r"}")

        file.write(r"\begin{document}")
        file.write(expression)
        file.write(r"\end{document}")

    # Compiling
    if tempfolder:
        command = f"pdflatex -output-format=pdf -interaction=batchmode -output-directory=tempfolder {outfile}"
    else:
        command = f"latex {outfile}"
    os.system(command)


def dvi_to_svg(infile, outfile):
    command = f'pdf2svg {infile} {outfile}'
    # --verbosity = 0
    os.system(command)



def latex_expression(expression, usepackages=None, preamble=None, cleanup = True, colour=None):
    '''returns an svg string of the LaTeX expression'''
    if os.path.exists('tempfolder'):
        shutil.rmtree('tempfolder')
        os.system('mkdir tempfolder')
    else:
        os.system('mkdir tempfolder')
    generate_pdf_from_tex(expression, r'tempfolder/outfile.tex', tempfolder=True, usepackages=usepackages, preamble=preamble, colour=colour)
    dvi_to_svg(r'tempfolder/outfile.pdf', r'tempfolder/outfile.svg')
    with open(r'tempfolder/outfile.svg', 'r') as svgfile:
        list_of_lines = svgfile.readlines()[1:]
    if cleanup:
        shutil.rmtree('tempfolder')
    # os.remove('outfile.svg')
    ## Get width and height
    first_line = list_of_lines[0]
    properties = first_line.split(" ")
    width = re.findall('"([^"]*)"', properties[3])[0][:-2]
    height = re.findall('"([^"]*)"', properties[4])[0][:-2]
    return  ('\n'.join(list_of_lines), 1.33333*float(width), 1.33333*float(height))


