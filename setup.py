# Copyright (c) 2021 - Itz-fork
# Project: py-trans
import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

if os.path.isfile('requirements.txt'):
  with open('requirements.txt') as req:
    reques = req.read().splitlines()
else:
  reques = ['requests==2.22.0', 'aiohttp==3.7.4.post0', 'fake_useragent==0.1.11']

if os.path.isfile('README.md'):
  with open(('README.md'), encoding='utf-8') as readmeh:
    big_description = readmeh.read()
else:
  big_description = "py_trans is a free python library to translate text to different languages."


setup(name='py-trans',
version='v0.5',
description='Free python library to translate text to different languages.',
url='https://github.com/Itz-fork/py-trans',
author='Itz-fork',
author_email='itz-fork@users.noreply.github.com',
license='MIT',
packages=find_packages(),
download_url=f"https://github.com/Itz-fork/py-trans/releases/tag/py-trans-pypi-{pyt_version}",
keywords=['python', 'translator', 'py-trans'],
long_description=big_description,
long_description_content_type='text/markdown',
install_requires=reques,
classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
  ],
)
