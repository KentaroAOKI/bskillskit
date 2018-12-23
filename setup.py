"""bskillskit setup module.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bskillskit',
    version='0.8.1',
    description='It is a helper tool with reference to box skills. It is not official.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/KentaroAOKI/bskillskit',
    author='Kentaro Aoki',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='bskillskit',
    packages=find_packages(),
    install_requires=['boxsdk'],
)