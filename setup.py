import os
from setuptools import setup, find_packages
import tomli

toml_file=[]
with open("pyproject.toml", mode="rb") as config:
    toml_file = tomli.load(config)

VER = toml_file['project']['version']

if(VER == ""):
    raise Exception("Failed to load version from toml file")

with open("VERSION", "w+") as f:
    # Reading from a file
    VER=f.write(VER)
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
