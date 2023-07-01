import os
from setuptools import setup, find_packages
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('jplaw/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)
    
VER = main_ns['__version__']

setup(
    name='jplaw',
    version=VER,
    packages=['jplaw', 'jplaw/types'],
    description='A python wrapper for the lemmy HTTP API. Forked from plaw by Benjamin Jablonski (benja810)',
    author='Amar Persaud',
    author_email='amar.d.persaud@gmail.com',
    install_requires=["requests >=2.6.0, <3.0", "tomli >=2.0.0"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='lemmy plaw api jplaw',
    long_description=open('README.md').read(),
)
