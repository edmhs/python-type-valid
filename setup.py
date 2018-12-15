from setuptools import setup, find_packages
import io
import os

# add readme to pip package readme information
dir_path = os.path.abspath(os.path.dirname(__file__))
readme = io.open(os.path.join(dir_path, 'README.md'), encoding='utf-8').read()

REQUIRES_PYTHON = '>=3.5.0'

setup(name='type_valid',
      version='0.1.5',
      description='Python Type validator with decorators',
      url='https://github.com/edmhs/python-type-valid',
      author='Eduards Marhelis',
      author_email='eduards.marhelis@gmail.com',
      license='MIT',
      long_description=readme,
      python_requires=REQUIRES_PYTHON,
      test_suite="tests",
      packages=find_packages(exclude=['tests']),
      classifiers=[
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
      ]
      )




