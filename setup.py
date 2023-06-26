from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Science/Research',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

with open("README.txt", "r") as f:
    long_description = f.read()

setup(
  name='PureFlow',
  version='0.0.1',
  description='Data Cleaning Tool',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/iMoHd8/PureFlow',  
  author='Mohammed Mahameed',
  author_email='iMoHd8@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['Data', 'DataCleaning', 'Cleaning', 'Machine Learning', 'Data Cleaning', 'Data Process'], 
  packages=find_packages(),
  install_requires=['pandas'] 
)