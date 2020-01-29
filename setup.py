"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))
setup(
    name='bfx-hf-indicators',
    version='1.1.0',
    description='Official Bitfinex Indicator Library for Python',
    long_description='A collection of different trading indicators',
    long_description_content_type='text/markdown',
    url='https://github.com/bitfinexcom/bfx-hf-indicators',
    author='Bitfinex',
    author_email='support@bitfinex.com',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Stable',

        # Project Audience
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Project License
        'License :: OSI Approved :: Apache 2.0',

        # Python versions (not enforced)
        'Programming Language :: Python :: 2.0',
        'Programming Language :: Python :: 2.1.0',
        'Programming Language :: Python :: 2.2.0',
        'Programming Language :: Python :: 2.3.0',
        'Programming Language :: Python :: 2.4.0',
        'Programming Language :: Python :: 2.5.0',
        'Programming Language :: Python :: 2.6.0',
        'Programming Language :: Python :: 2.7.0',
        'Programming Language :: Python :: 2.8.0',
        'Programming Language :: Python :: 2.9.0',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1.0',
        'Programming Language :: Python :: 3.2.0',
        'Programming Language :: Python :: 3.3.0',
        'Programming Language :: Python :: 3.4.0',
        'Programming Language :: Python :: 3.5.0',
        'Programming Language :: Python :: 3.6.0',
        'Programming Language :: Python :: 3.7.0',
    ],
    keywords='bitfinex,trading',
    packages=find_packages(exclude=['tests', 'docs']),
    # Python versions (enforced)
    python_requires='>=2.0.0, <4',
    # deps installed by pip
    install_requires=[],
    project_urls={
        'Bug Reports': 'https://github.com/bitfinexcom/bfx-hf-indicators/issues',
        'Source': 'https://github.com/bitfinexcom/bfx-hf-indicators',
    },
)
