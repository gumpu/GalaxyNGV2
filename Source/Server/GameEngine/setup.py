from setuptools import setup, find_packages

setup(name='ngengine',
      version='0.0.2',
      description='GalaxyNG Engine',
      url='',
      scripts=['bin/galaxy.py'],
      author='Frans Slothouber',
      author_email='rfsber@xs4all.nl',
      license='GPL',
      packages=find_packages(),
      install_requires=['docopt'],
      zip_safe=False)

