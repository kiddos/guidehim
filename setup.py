from setuptools import setup
import os


setup(
  name='guidehim',
  version='0.1.0',
  author='kiddos',
  author_email='kiddo831007@gmail.com',
  packages=['guidehim', 'map'],
  package_data={'guidehim': ['images/*.png'], 'map': ['*.map']},
  install_requires=['numpy>=1.10.x', 'gym>=0.8.0', 'pygame>=1.9.3']
)
