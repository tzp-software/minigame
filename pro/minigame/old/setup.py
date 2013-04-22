from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='minigame',
      version=version,
      description="python game library",
      long_description="""\
a game library written in python for users of mainly small devices that can install python but cannot install pygame.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='game python pygame embedded ios android',
      author='kyle roux',
      author_email='jstacoder@gmail.com',
      url='tzp',
      license='gpl2',
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
