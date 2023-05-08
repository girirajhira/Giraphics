from distutils.core import setup
setup(
  name = 'giraphics',
  version = '0.0.6',
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
      ],

  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Topic :: Scientific/Engineering :: Astronomy",
    "Topic :: Scientific/Engineering :: Physics"]
)