#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='tdemo',
    description='Sample Troposphere to CloudFormation Demo project',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'boto3',
        'troposphere',
        'nose',
        'mock',
        'argparse'
    ],
    entry_points={
        'console_scripts': [
            'tdemo = tdemo.core.main:main',
        ],
    },
    zip_safe=False,
)
