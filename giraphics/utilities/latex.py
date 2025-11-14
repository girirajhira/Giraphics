import os
import shutil
import re
import subprocess
import numpy as np
import pathlib as pl
from functools import lru_cache, cache
from giraphics.utilities.colour import ColourObj

default_latex_template = r"""
\documentclass[preview,border=10pt]{standalone}
\usepackage[utf8]{inputenc}
\usepackage{physics}
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{amsfonts}

"""

def generate_pdf_from_tex(expression, outfile, tempfolder = False, usepackages=None, preamble=None, colour = None, cur_dir=None):
    '''
    :param expression: Latex expression to be rendered (string)
    :param outfile: location of output file (string)
    :param tempfolder: whether a temperorary folder should be made (bool)
    :param usepackages
    :param preamble:
    :param colour:
    :return:
    '''
    with open(outfile, 'w') as file:
        file.write(default_latex_template)
        if usepackages is not None:
            for pack in usepackages:
                file.write(r"\usepackage{" + pack +"}")
        if preamble is not None:
            file.write(preamble + " \n")
        if colour is not None:
            if isinstance(colour, list) or isinstance(colour, (np.ndarray, np.generic)):
                file.write(r"\usepackage{xcolor}" + '\n')
                file.write(r"\definecolor{custcolour}{RGB}{" + f'{colour[0]}, {colour[1]}, {colour[2]}' + r"}" + '\n' )
                expression = (r"\textcolor{custcolour}{" + expression + r"}" + '\n')
            else:
                file.write(r"\usepackage{xcolor}")
                expression = (r"\textcolor{" + colour + "}{" + expression + r"}" + '\n' )

        file.write(r"\begin{document}" + '\n')
        file.write(expression)
        file.write( '\n'+ r"\end{document}")

    # Compiling
    folder = pl.Path.cwd()/'tempfolder'
    if tempfolder:
        command = f"pdflatex -output-format=pdf -interaction=batchmode -output-directory={str(folder)} {outfile}"
    else:
        command = f"latex {outfile}"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    return None

def dvi_to_svg(infile, outfile):
    command = f'pdf2svg {infile} {outfile}'
    # --verbosity = 0
    os.system(command)



def latex_expression(expression, usepackages=None, preamble=None, cleanup = True, colour=None, current_dir= None):
    '''returns an svg string of the LaTeX expression'''
    folder_name = 'tempfolder'
    folder = pl.Path.cwd()/folder_name

    if os.path.exists(folder):
        shutil.rmtree(str(folder))
        folder.mkdir()
    else:
        folder.mkdir()

    # if current_dir is None:
    #     current_dir = os.path.dirname(os.path.abspath(__file__))
    # folder_name = "tempfolder"
    #
    # # Create the full path for the folder
    # folder_path = os.path.join(current_dir, folder_name)
    #
    # # Check if the folder exists
    # if os.path.exists(folder_path):
    #     shutil.rmtree(folder_path)  # Remove the folder and its contents
    #     os.makedirs(folder_path)  # Recreate the folder
    # else:
    #     os.makedirs(folder_path)  # Create the folder if it doesn't exist

    generate_pdf_from_tex(expression, r'tempfolder/outfile.tex', tempfolder=True, usepackages=usepackages, preamble=preamble, colour=colour)
    dvi_to_svg(rf'{str(folder)}/outfile.pdf', fr'{str(folder)}/outfile.svg')
    with open(rf'{str(folder)}/outfile.svg', 'r') as svgfile:
        list_of_lines = svgfile.readlines()[1:]
    if cleanup:
        shutil.rmtree(str(folder))
    # os.remove('outfile.svg')
    ## Get width and height
    first_line = list_of_lines[0]
    properties = first_line.split(" ")
    width = re.findall('"([^"]*)"', properties[3])[0][:-2]
    height = re.findall('"([^"]*)"', properties[4])[0][:-2]
    return  ('\n'.join(list_of_lines), 1.33333*float(width), 1.33333*float(height))


