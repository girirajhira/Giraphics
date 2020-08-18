import os

def math_to_svg(expression, outfile):
    command = r"/usr/local/lib/node_modules/mathjax-node-cli/bin/tex2svg '%s' > %s" % (expression, outfile)
    os.system(command)

# math_to_svg('e^{i\pi} = -1', os.getcwd()+'/ste.svg')
