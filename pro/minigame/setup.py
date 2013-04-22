from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='minigame',
      version=version,
      description="Python game library for embedded devices",
      long_description="""\
python gaming library built for small, lom memory, embedded devices""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python game dice cards ios android players tools utils',
      author='Kyle Roux',
      author_email='jstacoder@gmail.com',
      url='tzpsoftware.com',
      license='bsd',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
