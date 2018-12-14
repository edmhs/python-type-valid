from setuptools import setup
import io
import os

# add readme to pip package readme information
dir_path = os.path.abspath(os.path.dirname(__file__))
readme = io.open(os.path.join(dir_path, 'README.md'), encoding='utf-8').read()

setup(name='type_valid',
      version='0.1.1',
      description='Python Type validator with decorators',
      url='https://github.com/edmhs/python-type-valid',
      author='Eduards Marhelis',
      author_email='eduards.marhelis@gmail.com',
      license='MIT',
      long_description=readme,
      zip_safe=False)


# python setup.py sdist bdist_wheel
# twine upload --repository-url https://upload.pypi.org/legacy/ ./dist/*


# pytest --cov=./type_valid
# pytest --cov=./type_valid --cov-report html:coverage
