from setuptools import setup, find_packages

requires = []

setup(
  name="pyflow",
  tests_require=['pytest', 'flake8'],
  packages=find_packages(include=['pyflow', 'pyflow.*']),
  include_package_data=True,
  install_requires=requires,
  zip_safe=False)
