from distutils.core import setup
setup(
  name = 'giraphics',
  version = '0.0.7',
  license='MIT',
  packages=['giraphics', 'giraphics.graphing', 'giraphics.animate', 'giraphics.svg', 'giraphics.graphing3d',
            'giraphics.utilities'],
  description = 'Lightweight graphing and animations',
  author = 'T. G. Hiranandani',
  author_email = 'giraphics@protonmail.com',
  url = 'https://github.com/tghira/giraphics',
  keywords = ['graphs', 'animations', 'graphics', 'vector-graphics'],
  install_requires=[
          'numpy',
          'IPython',
          'svgpath2mpl',
          'svg.path'
      ],

  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",

    "Topic :: Scientific/Engineering :: Astronomy",
    "Topic :: Scientific/Engineering :: Physics"]
)