# setup.py

from setuptools import setup, find_packages

setup(
    name='CoolUtils',
    version='1.0.0',
    description='A collection of cool and useful utilities.',
    author='kingsmile',
    author_email='wusicheng@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.0',
        'numpy>=1.21.0',
    ],
)
