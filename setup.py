#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

__author__ = 'Ryan McGrath <ryan@venodesigns.net>'
__version__ = '1.0.1'

setup(
    # Basic package information.
    name='jTransliterate',
    version=__version__,
    packages=find_packages(),

    # Packaging options.
    include_package_data=True,

    # Metadata for PyPI.
    author='Ryan McGrath',
    author_email='ryan@venodesigns.net',
    license='MIT License',
    url='http://github.com/ryanmcgrath/twython/tree/master',
    keywords='japanese translation transliterate katakana hiragana latin',
    description='Transliterate [Hirag/Katak]ana to Latin/English and back. Convert half/full-width Japanese text.',
    long_description=open('readme.md').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet'
    ]
)
