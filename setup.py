# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in nextqr/__init__.py
from nextqr import __version__ as version

setup(
	name='nextqr',
	version=version,
	description='QR Code generate',
	author='Bhavesh Maheshwari',
	author_email='info@nesscale.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
