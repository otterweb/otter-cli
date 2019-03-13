import os
import re
import json
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

version = '0.0.3'

setup(
        name='otter-cli',
        version=version,
        description='Command line interface for interacting with Otter Web API',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/chuck1/otter-cli',
        packages=['otter_cli'],
        zip_safe=False,
        scripts=['scripts/otter'],
        )




