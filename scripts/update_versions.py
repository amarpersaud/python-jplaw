import os
from setuptools import setup, find_packages
from distutils.util import convert_path
import json

main_ns = {}
ver_path = convert_path('jplaw/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)
    
VER = "v" + main_ns['__version__']

data={}

with open('./docs/VERSIONS.json', 'r+') as f:
    data = json.load(f)
    if(VER not in data["Versions"]):
        data["Versions"].append(VER)
    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate()     # remove remaining part