#!/usr/bin/env python3
"""
Setup script for the Jasmin Pygments lexer.
"""

from setuptools import setup, find_packages

setup(
    name="jasmin-pygments-lexer",
    version="1.0.0",
    description="Pygments lexer for the Jasmin programming language",
    long_description="A Pygments lexer for syntax highlighting of Jasmin (.jazz) files used in the libjade cryptographic library.",
    author="libjade contributors",
    url="https://github.com/J08nY/libjade",
    packages=find_packages(),
    entry_points={
        'pygments.lexers': [
            'jasmin = jasmin_lexer:JasminLexer',
        ],
    },
    install_requires=[
        'Pygments>=2.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Text Processing :: Filters',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
)