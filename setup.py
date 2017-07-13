#!/usr/bin/env python
try:
    from setuptools import setup
    args = {}
except ImportError:
    from distutils.core import setup
    print("""\
*** WARNING: setuptools is not found.  Using distutils...
""")

from setuptools import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(name='demo',
      version='0.0.0',
      description='',
      long_description=read_md('README.md'),
      author='Felicity Nielson',
      author_email='felicity.nielson@gmail.com',
      url='https://github.com/nielsonf/hello_world',
      license='MIT',
      install_requires=[
          "numpy",
          "termcolor",
          "pyparsing",
      ],
      packages=['demo'],
      scripts=[],
      classifiers=[
          'Development Status :: 1 - Prealpha',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'License :: OSI Approved :: MIT License',          
          'Operating System :: MacOS',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Scientific/Engineering :: Physics',
      ],
     )
