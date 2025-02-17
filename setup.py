import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="MRI_reconstruction",
    version="0.1",
    url="https://github.com/inbalalo/MRI_rec",
    license='MIT',

    author="Inbal Alon",
    author_email="inbala@mail.tau.ac.il",

    description="MRI machines are extremely expensive in part due to the perfect homogenic magnetic field that has to be generated inside them. In this project we create a pipeline that simulates a non-perfect MRI data by "spoiling" perfect data in a known manner, only to the try to reconstruct the true, "perfect" field using existing methods in the literature.",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
