from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='dataset_filelist',
      version='0.0.1',
      description='Simple class to make Pytorch dataset object creation easier and more flexible.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Danilo Weber Nunes',
      author_email='danilownunes@gmail.com',
      url='https://github.com/danilown/FileListDataset',
      license='BSD-3',
      install_requires=['pytorch >= 1.2.0',
                        'torchvision >= 0.4.0'
                        ],
      packages=find_packages())