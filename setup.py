from setuptools import setup, find_packages
 
classifiers = [
  'Topic :: Scientific/Engineering',
  'Development Status :: 2 - Pre-Alpha',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.7',
  'Programming Language :: Python :: 3.8',
  'Programming Language :: Python :: 3.9',
  'Programming Language :: Python :: 3.10',
  'Natural Language :: English'
]

with open("README.txt", "r") as f:
    long_description = f.read()

setup(
  name='PureFlow',
  version='1.0.1',
  description='Data Cleaning Tool',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/iMoHd8/PureFlow',  
  author='Mohammed Mahameed',
  author_email='iMoHd8@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['PureFlow', 'Data', 'DataCleaning', 'Cleaning', 'Machine Learning', 'Data Cleaning','data science', 'Data Process'], 
  packages=find_packages(),
  install_requires=['pandas']
)