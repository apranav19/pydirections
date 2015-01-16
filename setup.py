from setuptools import setup

setup(name='pydirections',
      version='0.0.1',
      description='Serving directions since 2015',
      url='https://github.com/apranav19/pydirections',
      author='Pranav Angara',
      author_email='apranav19@gmail.com',
      license='Apache',
      packages=['pydirections'],
       install_requires=[
          'requests',
      ]
      zip_safe=False)