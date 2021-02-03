from distutils.core import setup
setup(
  name = 'giraphics',
  packages = ['giraphics'],
  version = '0.2',
  license='MIT',
  description = 'Lightweight graphing and animations',
  author = 'T. G. Hiranandani',
  author_email = 'giraphics@protonmail.com',
  url = 'https://github.com/tghira/giraphics',
  download_url = 'https://github.com/tghira16/Giraphics/archive/1.tar.gz',
  keywords = ['graphs', 'animations', 'graphics', 'vector-graphics'],
  install_requires=[
          'numpy',
          'IPython'

      ],
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Educators, Scientists',
    'Topic :: Graphics Animation :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',

  ],
)

