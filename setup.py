# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]


requires = ['Flask', 'blockdiag']


setup(
    name='paddiag',
    version='0.1.0',
    description='paddiag generates PAD-diagram image from text',
    classifiers=classifiers,
    keywords=['diagram', 'generator'],
    author='Takeshi Komiya',
    author_email='i.tkomiya at gmail.com',
    url='https://bitbucket.org/tk0miya/paddiag',
    license='Apache License 2.0',
    packages=find_packages('paddiag'),
    package_dir={'paddiag': 'paddiag'},
    include_package_data=True,
    install_requires=requires,
    entry_points="""
       [console_scripts]
       paddiag = paddiag.paddiag:main
       flowchartdiag = paddiag.flowchartdiag:main
       paddiag_interactive_shell = paddiag.interactive:main
    """,
)
