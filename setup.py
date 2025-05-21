from setuptools import find_packages
from distutils.core import setup
import os

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
	# Name of the package 
	name='fastargs-harvard-visionlab',
	# Packages to include into the distribution 
	packages=find_packages('.'),
	# Start with a small number and increase it with 
	# every change you make https://semver.org 
	version='1.1.2',
	# Chose a license from here: https: // 
	# help.github.com / articles / licensing - a - 
	# repository. For example: MIT 
	license='MIT',
	# Short description of your library 
	description='Python library for argument and configuration management ',
	# Long description of your library 
	long_description=long_description,
	long_description_content_type='text/markdown',
	# Your name 
	author='Harvard Vision Lab, original by Guillaume Leclerc',
	# Your email 
	author_email='alvarez@wjh.harvard.edu',
	# Either the link to your github or to your website 
	url='https://github.com/harvard-visionlab/fastargs',
	# Link from which the project can be downloaded 
	download_url='',
	# List of keywords 
	keywords=['parameters', 'configuration', 'decorators'],
	# List of packages to install with this one 
	install_requires=[],
	# https://pypi.org/classifiers/ 
	classifiers=['Development Status :: 5 - Production/Stable', 'Environment :: Console']
)
